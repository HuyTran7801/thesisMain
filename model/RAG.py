from langchain.document_loaders.pdf import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import DirectoryLoader, TextLoader


embedding_model_name = 'sentence-transformers/all-MiniLM-L6-v2'

class RAG:
    def __init__(self, persist_directory):
        self.persist_directory = persist_directory
        self.embedding_model = HuggingFaceEmbeddings(model_name=embedding_model_name)
        self.db = Chroma(persist_directory=self.persist_directory, embedding_function=self.embedding_model)
    
    def load_documents(self, directory):
        loader = PyPDFDirectoryLoader(directory) # oop, dsa
        documents = loader.load()
        return documents
    
    def split_documents(self,documents: list[Document]):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=80, length_function=len, is_separator_regex=False)
        texts = text_splitter.split_documents(documents)
        return texts
    
    def unique_chunk_id(self,chunks):
        map = dict()

        for chunk in chunks:
            chunk.metadata['id'] = 0
            # print(f"{chunk.metadata['source']}:{chunk.metadata['page']}")

        for chunk in chunks:
            # print(f"{chunk.metadata['source']}:{chunk.metadata['page']}:{chunk.metadata['id']}")
            text = chunk.metadata['source'] + ':' + str(chunk.metadata['page'])
            if text not in map.keys():
                map[text] = 0
            else:
                map[text] += 1
                chunk.metadata['id'] = map[text]

        # for chunk in chunks:
        #   print(f"{chunk.metadata['source']}:{chunk.metadata['page']}:{chunk.metadata['id']}")
        return chunks

    def add_to_chroma(self, chunks: list[Document]):
        # unique page id
        chunks_with_ids = self.unique_chunk_id(chunks)
        # print('Len of chunks with id: ', len(chunks_with_ids))
        # print(chunks_with_ids)

        # add or update documents
        existing_items = self.db.get(include=[])  # IDs are always included by default
        # print('Existing items: ', existing_items)

        existing_ids_set = set(existing_items["ids"]) # type string
        print(f"Number of existing documents in DB: {len(existing_ids_set)}")
        
        existing_ids = list(existing_ids_set)
        for i in range(len(existing_ids)):
            existing_ids[i] = int(existing_ids[i])
        existing_ids.sort()
        # print(existing_ids)

        start_id = -1
        if len(existing_ids) == 0:
            start_id = 0
        else:
            start_id = existing_ids[len(existing_ids)-1] + 1
        # print('Start id: ', start_id)

        # Only add documents that don't exist in the DB.
        new_chunks = []
        new_chunk_ids = []
        for chunk in chunks_with_ids:
            if str(start_id) not in existing_ids_set:
                new_chunks.append(chunk)
                start_id += 1
                new_chunk_ids.append(str(start_id))

        if len(new_chunks):
            print(f"Adding new documents: {len(new_chunks)}")
            # print(new_chunk_ids)
            # print(type(new_chunk_ids))
            self.db.add_documents(new_chunks, ids=new_chunk_ids) # all type should be string, ids should be unique
        else:
            print("No new documents to add")
            
    def semantic_search(self, query_text, k_relevant):
        results = self.db.similarity_search_with_score(query_text, k=k_relevant)
        context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])

        documents = dict()
        for doc, _score in results:
            source = doc.metadata['source']
            page = doc.metadata['page']
            if source not in documents:
                documents[source] = [page]
            else:
                documents[source].append(page)

        for key, value in documents.items():
            documents[key].sort()

        return context_text, documents
    
        