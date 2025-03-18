from flask import Flask, render_template, redirect, url_for, json, session, request
from flask_session import Session

from model.LLM import *
from model.ReasoningLLM import *
from model.RAG import *
from model.Directory import *
from model.Handling import *
from model.CheckingFile import *
from model.MultiAgentDebate import *

from database.domainDB import *
from database.questionsDB import *
from database.userDB import *
from database.roleDB import *
from database.courseDB import *
from database.userQuestionDB import *

# import time
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

app = Flask(__name__, template_folder='./template')
app.secret_key = 'secret key'
app.config['UPLOAD_FOLDER'] = '' # need to fix
ALLOWED_EXTENSIONS = {'pdf'}  # Only allow PDF files
ALLOWED_EXTENSIONS_IMAGE = {'png', 'jpg', 'jpeg', 'gif'}

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def allowed_file_image(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS_IMAGE

    
@app.route('/')
def home():
    return redirect(url_for('intro'))

@app.route('/intro', methods=['GET', 'POST'])
def intro():
    click = request.form.get('click')
    if request.method == 'POST':
        if click == 'log in':
            return redirect(url_for('login'))
        elif click == 'sign up':
            return redirect(url_for('signup'))
    return render_template('intro.html')

@app.route('/service', methods=['GET', 'POST'])
def service():
    username = session.get('username')
    role = session.get('role')
    print('username ', username)
    click = request.form.get('click')
    choice = request.form.get('btn')
    print('role ', role)
    # greeting = ''
    
    # if username is not None:
    #     # greeting = f'Welcome {username}'
    #     return render_template('service.html')
        
    if request.method == 'POST':
        if click == 'service':
            return redirect(url_for('service'))
        elif click == 'log in':
            return redirect(url_for('login'))
        elif click == 'sign up':
            return redirect(url_for('signup'))
        elif click == 'about':
            return redirect(url_for('about'))
        elif click == 'contact':
            return redirect(url_for('contact'))
        
        if choice == 'MCQs generation':
            # print("GO")
            return redirect(url_for('courses'))
        elif choice == 'Add a course':
            return redirect(url_for('add_course'))
    return render_template('service.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    warning = ''
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        choose = request.form.get('btn')
        
        if choose == 'log in':
            user_db = UserDB()
            role_db = RoleDB()
            user = user_db.check_exist_user(username)
            # user_id = user_id[0]
            print('USER ', user)
            
            if user == None:
                warning = 'Wrong username or password'
                return render_template('login.html', warning=warning)
            else:
                session['user_id'] = user[0]
                session['username'] = username
                role_id = user[3]
                role_info = role_db.get_role_by_id(role_id)
                role = role_info[1]
                session['role'] = role
                if role == 'teacher':
                    return redirect(url_for('service'))
                else:
                    return redirect(url_for('courses'))
        elif choose == 'sign up':
            return redirect(url_for('signup'))
            
    return render_template('login.html', warning=warning)  

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    warning = ''
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role')
        choose = request.form.get('btn')
        
        if choose == 'sign up':
            if username == None or password == None or role == None:
                warning = 'Please full-fill the form !'
                return render_template('signup.html', warning=warning)
            
            user_db = UserDB()
            role_db = RoleDB()
            exist_user = user_db.check_exist_user(username)
            
            # Check exist
            if exist_user == None:
                role_info = role_db.get_role_by_name(role)
                role_id = role_info[0]
                user_db.create_user(username, password, role_id)
                warning = 'Sign up successfully!!'
                return render_template('signup.html', warning=warning)
            else:
                warning = 'Username has already been used!'
                return render_template('signup.html', warning=warning)
        elif choose == 'log in':
            return redirect(url_for('login'))
    return render_template('signup.html', warning='')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')



@app.route('/courses', methods=['GET', 'POST'])
def courses():
    course_db = CourseDB()
    courses = course_db.get_all_courses()
    role = session.get('role')
    
    if request.method == 'POST':
        click = request.form.get('click')
        
        if click == 'service':
            return redirect(url_for('service'))
        elif click == 'about':
            return redirect(url_for('about'))
        elif click == 'contact':
            return redirect(url_for('contact'))
        elif click == 'profile':
            return redirect(url_for('intro'))
        
        course_id = request.form.get('btn')
        
        # print('course id ', course_id)
        session['course_id'] = course_id
        
        course_info = course_db.get_course(course_id)
        course_name = course_info[0]
        code = course_info[1]
        
        session['course'] = course_name
        session['code'] = code
        
        if role == 'student':
            return redirect(url_for('options'))
        elif role == 'teacher':
            return redirect(url_for('options_teacher'))
    return render_template('courses.html', courses=courses)  

@app.route('/options', methods=['GET', 'POST'])
def options():
    btn = request.form.get('btn')
    code = session.get('code')
    user_id = session.get('user_id')
    
    if request.method == 'POST':
        directory = Directory(code, user_id)
        
        directory.create_directory()
        directory.create_file_directory()
        directory.create_file_temp_directory()
        if btn == 'attach file':
            # course = session.get('course')
    
            return redirect(url_for('attach_file'))
        elif btn == 'go quiz':
            return redirect(url_for('level'))
        elif btn == 'back':
            return redirect(url_for('courses'))
    return render_template('options.html')

@app.route('/options_teacher', methods=['GET', 'POST'])
def options_teacher():
    code = session.get('code')
    user_id = session.get('user_id')
    course_id = session.get('course_id')
    
    if request.method == 'POST':
        btn = request.form.get('btn')
        directory = Directory(code, user_id)
        
        directory.create_directory()
        directory.create_file_directory()
        directory.create_file_temp_directory()
        if btn == 'attach file':
            # course = session.get('course')
    
            return redirect(url_for('attach_file'))
        elif btn == 'go quiz':
            return redirect(url_for('level'))
        elif btn == 'back':
            return redirect(url_for('courses'))
        elif btn == 'delete':
            course_db = CourseDB()
            course_db.delete_course(course_id)
            
            return redirect(url_for('courses'))
    return render_template('options_teacher.html')

@app.route('/attach_file', methods=['GET', 'POST'])
def attach_file():
    # Check and create file
    # flag = 1  # 1 if update new, 0 is non-update
    # directory = session.get('directory')
    code = session.get('code')
    role = session.get('role')
    
    form = UploadFileForm()
    session['filename'] = None
    user_id = session.get('user_id')
    
    directory = Directory(code, user_id)
    
    pathDB = directory.get_vectorDB()
    path_file = directory.get_file()
    
    app.config['UPLOAD_FOLDER'] = f'./static/files{user_id}'
    app.config['UPLOAD_FOLDER_2'] = f'./static/filestemp{user_id}'
    
    if request.method == 'POST' and request.form.get('action') == 'back':
        # Redirect to previous page
        if role == 'student': 
            return redirect(url_for('options'))  # 
        elif role == 'teacher':
            return redirect(url_for('options_teacher'))
    
    if form.validate_on_submit():
        file = form.file.data  # Get the uploaded file
        print('FILE name ', file.filename, type(file.filename))

        if file and allowed_file(file.filename):  # Validate file extension
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file_path_2 = os.path.join(app.config['UPLOAD_FOLDER_2'], filename)

            # Check if the file already exists
            if os.path.exists(file_path):
                return "File already uploaded!", 400  # Return error if file exists

            file.save(file_path)  # Save file
            file.stream.seek(0)
            file.save(file_path_2)
            
            # Occured RAG process
            rag = RAG(pathDB)
            
            docs = rag.load_documents(path_file)
            chunks = rag.split_documents(docs)
            
            rag.add_to_chroma(chunks)

            directory.remove_file(filename)

            return redirect(url_for('attach_success'))  # Redirect on success

        return "Invalid file type! Only PDFs are allowed.", 400  # Return error if invalid file

    return render_template('attach_file.html', form=form)

@app.route('/attach_success', methods=['GET', 'POST'])
def attach_success():
    # btn = request.form.get('btn')
    if request.method == 'POST':
        return redirect(url_for('attach_file'))
    return render_template('attach_file_success.html')

@app.route('/level', methods=['GET', 'POST'])
def level(): # dont use currently
    course = session.get('course')
    # print('Course ', course)
    user_id = session.get('user_id')
    code = session.get('code')
    role = session.get('role')
    course_id = session.get('course_id')
    
    print('Role ', role)
    print('Course ', course)
    print('Code ', code)
    print('User id ', user_id)
    
    error_text = ''
    
    domain_db = DomainDB()
    domains = domain_db.get_all_domains(course_id)
    print('All domains ', domains)
    
    domain_lst=[]
    
    if domains == None:
        domains = ''
    else:
        for i in domains:
            domain_lst.append(i[0])
    
    if request.method == 'POST':
        options = request.form.get('options')
        topic = request.form.get('topic')
        choice = request.form.get('btn')
        print('topic : ', topic)
        
        num_of_questions, level_of_questions, questions, questions_from_db, reference = None, None, None, None, None
        string_of_questions = ''
        questions_lst = None
        QAs = []
        if options == 'mcqs':
            num_of_questions = int(request.form.get('num_of_mcqs'))
            level_of_questions = request.form.get('level_of_mcqs')
        elif options == 'fill':
            num_of_questions = int(request.form.get('num_of_fill'))
            level_of_questions = request.form.get('level_of_fill')
        elif options == 'coding':
            num_of_questions = int(request.form.get('num_of_coding'))
            level_of_questions = request.form.get('level_of_coding')
            
        session['options'] = options
        
        if choice == 'go':
            
            if num_of_questions == None or level_of_questions == None or topic == None or topic == '':
                return render_template('level.html', course=course, error_text='Please fullfill the form!')
            else:
                directory = Directory(code, user_id)
                path_DB = directory.get_vectorDB()
                
                rag = RAG(path_DB)
                multi_agent = MultiAgent()
                handling = Handling()
                llm = LLM()
                
                context, docs = rag.advanced_semantic_search(topic, 20)
                
                docs = docs.replace(f'static\\\\filestemp{user_id}\\\\',' - ')
                # docs = str(docs)
                reference = 'Documents: '
                reference += docs
                
                if role == 'teacher':
                    print('Role as ', role)
                    print('LLM GENERTED FOR TEACHER')
                    if options == 'mcqs':
                        if level_of_questions == 'easy':
                            multi_agent.generate_MCQs(course, num_of_questions, context, topic)
                            questions = multi_agent.get_MCQs()
                            
                        elif level_of_questions == 'hard':
                            multi_agent.generate_hard_MCQs(course, num_of_questions, context, topic)
                            questions = multi_agent.get_MCQs()
                            
                        if num_of_questions == 5:
                            questions_lst = handling.split_5_mcqs(questions)
                        elif num_of_questions == 10:
                            questions_lst = handling.split_10_mcqs(questions)
                        elif num_of_questions == 15:
                            questions_lst = handling.split_15_mcqs(questions)
                            
                        for i in questions_lst:
                            question, answer_lst, feedback_lst, corrected_ans = handling.split_QA(i)
                            qa = []
                            qa.append(question)
                            for answer in answer_lst:
                                qa.append(answer)
                            for feedback in feedback_lst:
                                qa.append(feedback)
                            qa.append(corrected_ans)
                            QAs.append(qa)
                                
                        # print('len QAs ', len(QAs))
                        print('----MCQs----')
                        print(questions)
                        print('------------')
                        session['QAs'] = QAs   
                        session['index'] = 0
                        session['total'] = len(QAs)
                        session['score'] = 0
                        session['wrong_questions'] = []
                        session['reference'] = reference
                        
                        session['questions'] = questions
                        session['num_of_questions'] = num_of_questions
                        session['level_of_questions'] = level_of_questions
                        session['topic'] = topic
                        
                        return redirect(url_for('mcqs_detail_teacher'))
                    
                elif role == 'student':
                # Check domain exists
                    print('Role as ', role)
                    domain = domain_db.get_domain(topic)
                    using_LLM = False
                    if domain != None:
                        if options == 'mcqs':
                            # Generate by DB if questions bank is existed
                            print('DB QUESTION BANK')
                            question_db = QuestionsDB()
                            if level_of_questions == 'easy':
                                questions_from_db = question_db.get_all_questions_with_topic(topic,1)
                            elif level_of_questions == 'hard':
                                questions_from_db = question_db.get_all_questions_with_topic(topic,2)
                            
                            len_of_questions = len(questions_from_db)
                            # In case easy question bank is available, but how about hard question bank
                            if questions_from_db == None or len_of_questions < num_of_questions:
                                using_LLM = True
                                print('LLM Generated')
                            else:
                                # Show full DB
                                user_question_db = UserQuestionDB()
                                print('SHOW FULL DB')
                                for i in questions_from_db:
                                    question_id, question, label1, label2, label3, label4, answer, explanation, appear = i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]
                                    user_question_db.create_user_question(user_id, question_id) # should add unique
                                    
                                questions_for_user = user_question_db.get_user_question(user_id)
                                
                                for i in questions_for_user:
                                    qa = []
                                    question_id, question, label1, label2, label3, label4, answer, explanation, appear = i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]
                                    
                                    string_of_questions += i[1] + 'A) ' + i[2] + 'B) ' + i[3] + 'C) ' + i[4] + 'D) ' + i[5] + i[7]
                                    qa.append(question)
                                    
                                    qa.append(label1)
                                    qa.append(label2)
                                    qa.append(label3)
                                    qa.append(label4)
                                    
                                    feedback_lst = handling.split_explanation(explanation)
                                    qa.append(feedback_lst[0])
                                    qa.append(feedback_lst[1])
                                    qa.append(answer)
                                    
                                    QAs.append(qa)
                                
                            session['QAs'] = QAs   
                            session['index'] = 0
                            session['total'] = len(QAs)
                            session['score'] = 0
                            session['right_questions'] = []
                            session['wrong_questions'] = []
                            session['reference'] = reference
                            
                            session['questions'] = string_of_questions # IMPORTANT
                            session['num_of_questions'] = num_of_questions
                            session['level_of_questions'] = level_of_questions
                            session['topic'] = topic
                            
                            return redirect(url_for('mcqs_detail'))
                    else:
                        using_LLM = True
                        print('LLM GENERATED')
                    if using_LLM == True:     
                        if options == 'mcqs':
                            if level_of_questions == 'easy':
                                multi_agent.generate_MCQs(course, num_of_questions, context, topic)
                                questions = multi_agent.get_MCQs()
                                # questions = llm.generate_MCQs(course, context, num_of_questions, topic)
                                
                            elif level_of_questions == 'hard':
                                multi_agent.generate_hard_MCQs(course, num_of_questions, context, topic)
                                questions = multi_agent.get_MCQs()
                                
                            if num_of_questions == 5:
                                questions_lst = handling.split_5_mcqs(questions)
                            elif num_of_questions == 10:
                                questions_lst = handling.split_10_mcqs(questions)
                            elif num_of_questions == 15:
                                questions_lst = handling.split_15_mcqs(questions)
                                
                            for i in questions_lst:
                                question, answer_lst, feedback_lst, corrected_ans = handling.split_QA(i)
                                qa = []
                                qa.append(question)
                                for answer in answer_lst:
                                    qa.append(answer)
                                for feedback in feedback_lst:
                                    qa.append(feedback)
                                qa.append(corrected_ans)
                                QAs.append(qa)
                                    
                            # print('len QAs ', len(QAs))
                            print('----MCQs----')
                            print(questions)
                            print('------------')
                            session['QAs'] = QAs   
                            session['index'] = 0
                            session['total'] = len(QAs)
                            session['score'] = 0
                            session['right_questions'] = []
                            session['wrong_questions'] = []
                            session['reference'] = reference
                            
                            session['questions'] = questions
                            session['num_of_questions'] = num_of_questions
                            session['level_of_questions'] = level_of_questions
                            session['topic'] = topic
                            return redirect(url_for('mcqs_detail'))
                        elif options == 'fill':
                            if level_of_questions == 'easy':
                                multi_agent.generate_FIBQs(course, num_of_questions, context, topic)
                                questions = multi_agent.get_FIBQs()
                                # questions = llm.generate_FIBQs(course, num_of_questions, context, topic)
                                # print(questions)
                            elif level_of_questions == 'hard':
                                multi_agent.generate_hard_FIBQs(course, num_of_questions, context, topic)
                                questions = multi_agent.get_FIBQs()
                                
                            if num_of_questions == 5:
                                questions_lst = handling.split_5_mcqs(questions)
                            elif num_of_questions == 10:
                                questions_lst = handling.split_10_mcqs(questions)
                            elif num_of_questions == 15:
                                questions_lst = handling.split_15_mcqs(questions)
                                
                            for i in questions_lst:
                                question, feedback_lst, corrected_answer = handling.split_QA_fill_in_the_blank(i)
                                qa = []
                                qa.append(question)
                                for j in feedback_lst:
                                    qa.append(j)
                                qa.append(corrected_answer)
                                QAs.append(qa)
                                
                            
                            session['QAs_fill'] = QAs   
                            session['index_fill'] = 0
                            session['total_fill'] = len(QAs)
                            session['score_fill'] = 0
                            session['right_questions_fill'] = []
                            session['wrong_questions_fill'] = []
                            session['reference_fill'] = reference
                            
                            session['questions_fill'] = questions
                            session['num_of_questions_fill'] = num_of_questions
                            session['level_of_questions_fill'] = level_of_questions
                            session['topic_fill'] = topic
                            
                            return redirect(url_for('fibqs_detail'))
        elif choice == 'back':
            return redirect(url_for('courses'))
    return render_template('level.html', course=course, error_text=error_text, hashtags=domain_lst)

@app.route('/mcqs_detail', methods=['GET', 'POST'])
def mcqs_detail():
    index = session.get('index')
    QAs = session.get('QAs')
    total = session.get('total')
    reference = session.get('reference')
    # score = session.get('score')
    right_questions = session.get('right_questions')
    wrong_questions = session.get('wrong_questions')
    
    print('QAs')
    print(QAs)
    print('ID ', index)
    corrected_text = ''
    feedback1 = ''
    feedback2 = ''
    feedback3 = ''
    # QAs = []
    question_db = QuestionsDB()
    user_question_db = UserQuestionDB()
    
    question_detail= question_db.get_question(QAs[index][0])
    question_id = question_detail[0]
    
    occur = user_question_db.get_question_occurence(question_id)
    user_question_id = occur[0]
    
    if request.method == 'POST':
        choice = request.form.get('btn')
        
        if choice == 'submit':
            user_ans = request.form.get('ans')
                # user_ans = user_ans.strip()
            question = QAs[index][0] # What is ...?
            corrected_ans = QAs[index][7] # A), B), C) or D)
            feedback1 = QAs[index][5] # The corrected answer is:
            feedback2 = QAs[index][6] # Explanation:
            feedback3 = reference # Documents: 
            
            
            if user_ans is not None and corrected_ans == user_ans.strip():
                right_questions.append(user_question_id)
                session['right_questions'] = right_questions
                
                corrected_text = 'CORRECT'
                session['score'] += 1
            else:
                # Update fail attempt when incorrect
                question_db.update_fail_attempt(question_id)
                
                corrected_text = 'INCORRECT'
                wrong_questions.append(question)
                session['wrong_questions'] = wrong_questions
            return render_template('mcqs_detail.html', appearance=len(occur), qa=QAs[index],
                            corrected_text=corrected_text, feedback1=feedback1,
                           feedback2=feedback2, feedback3=feedback3)
        elif choice == 'next':
            if index == total- 1:
                return redirect(url_for('result'))
            else:
                session['index'] += 1
            return redirect(url_for('mcqs_detail'))
            
    return render_template('mcqs_detail.html', appearance=len(occur), qa=QAs[index],
                           corrected_text=corrected_text, feedback1=feedback1,
                           feedback2=feedback2, feedback3=feedback3)
    
@app.route('/mcqs_detail_teacher', methods=['GET', 'POST'])
def mcqs_detail_teacher():
    index = session.get('index')
    QAs = session.get('QAs')
    total = session.get('total')
    reference = session.get('reference')
    course = session.get('course')
    topic = session.get('topic')
    level = session.get('level_of_questions')
    course_id = session.get('course_id')
    
    print('QAs')
    print(len(QAs))
    print('ID ', index)
    
    feedback = reference
    print('feedback 1 ', QAs[index][5])
    print('feedback 2 ', QAs[index][6])
    # QAs = []
    
    if request.method == 'POST':
        choice = request.form.get('btn')
        review = request.form.get('review')
        
        question_db = QuestionsDB()
        domain_db = DomainDB()
        
        question = QAs[index][0]
        option_a = QAs[index][1]
        option_b = QAs[index][2]
        option_c = QAs[index][3]
        option_d = QAs[index][4]
        feedback1 = QAs[index][5]
        feedback2 = QAs[index][6]
        
        string_of_questions = question + option_a + option_b + option_c + option_d + feedback1 + feedback2
        
        multi_agent = MultiAgent()
        handling = Handling()
               
        if choice == 'regenerate':
            print('Questions: ', string_of_questions, ' ', type(string_of_questions))
            multi_agent.generate_MCQs_human_in_the_loop(course, string_of_questions, review, topic)
            
            mcqs = multi_agent.get_MCQs()
            
            new_question, new_answer_lst, new_feedback_lst, new_corrected_answer = handling.split_QA(mcqs)
            
            QAs[index][0] = new_question
            
            QAs[index][1] = new_answer_lst[0]
            QAs[index][2] = new_answer_lst[1]
            QAs[index][3] = new_answer_lst[2]
            QAs[index][4] = new_answer_lst[3]
            
            QAs[index][5] = new_feedback_lst[0]
            QAs[index][6] = new_feedback_lst[1]
            
            return render_template('mcqs_detail_teacher.html', qa=QAs[index], feedback=feedback)
        elif choice == 'accept':
            # Add domainDB
            topic_edited = topic.lower().strip()
            print('TOPIC ADDED : ', topic_edited)
            domain_db.create_domain(topic_edited, course_id)
            
            domain = domain_db.get_domain(topic_edited)
            domain_id = domain[0]
            
            # add to DB
            string_of_questions = QAs[index][0]
            string_of_answer = QAs[index][7]
            string_of_explanation = QAs[index][5] + QAs[index][6]
            label1, label2, label3, label4 = QAs[index][1], QAs[index][2], QAs[index][3], QAs[index][4]
            
            if level == 'easy':
                question_db.create_question(string_of_questions, label1, label2, label3, label4,
                                            string_of_answer, string_of_explanation, 0, 0, 1, domain_id)
            elif level == 'hard':
                question_db.create_question(string_of_questions, label1, label2, label3, label4,
                                            string_of_answer, string_of_explanation, 0, 0, 2, domain_id)
            
            if index == total- 1:
                return redirect(url_for('level'))
            else:
                session['index'] += 1
            return redirect(url_for('mcqs_detail_teacher'))
            
    return render_template('mcqs_detail_teacher.html', qa=QAs[index], feedback=feedback)

@app.route('/fibqs_detail', methods=['GET', 'POST'])
def fibqs_detail():
    index = session.get('index_fill')
    QAs = session.get('QAs_fill')
    total = session.get('total_fill')
    reference = session.get('reference_fill')
    wrong_questions = session.get('wrong_questions_fill')
    
    print('ID ', index)
    print('QAs ', QAs)
    
    question = QAs[index][0]
    corrected_text = ''
    feedback1 = ''
    feedback2 = ''
    feedback3 = ''
    
    if request.method == 'POST':
        choice = request.form.get('btn')
        
        if choice == 'submit':
            user_ans = request.form.get('ans')
            
            print('QUESTION ', question)
            feedback1 = QAs[index][1]
            feedback2 = QAs[index][2]
            feedback3 = reference
            corrected_answer = QAs[index][3]
            
            if user_ans is not None:
                ok = False
                if ',' in corrected_answer:
                    user_ans = user_ans.split(",")
                    corrected_answer = corrected_answer.split(",")
                    
                    for j in range(len(corrected_answer)):
                        if '/' in corrected_answer[j]:
                            corrected_answer[j] = corrected_answer[j].split('/')
                    for j in range(len(corrected_answer)):
                        user_cur_ans = user_ans[j].lower().strip()
                        if isinstance(corrected_answer[j], list) is True:
                            for k in corrected_answer[j]:
                                answer = k.replace('`', '').lower().strip()
                                answer = k.replace('.', '').lower().strip()
                                if user_cur_ans == answer:
                                    cnt +=1 
                                    break
                        else:
                            answer = corrected_answer[j].replace('`', '').lower().strip()
                            answer = corrected_answer[j].replace('.', '').lower().strip()
                            if user_cur_ans == answer:
                                cnt += 1
                    if cnt == len(corrected_answer):
                        ok = True
                    # for j in range(len(corrected_answer)):
                    #     cur_len = len(corrected_answer[j])
                        
                else:
                    user_ans = user_ans.lower().strip()
                    if '/' in corrected_answer:
                        corrected_answer = corrected_answer.split('/')
                        for j in range(len(corrected_answer)):
                            corrected_answer[j] = corrected_answer[j].replace('`', '').lower().strip()
                            corrected_answer[j] = corrected_answer[j].replace('.', '').lower().strip()
                        for j in corrected_answer:
                            if user_ans == j:
                                ok = True
                                break
                    else:
                        # None
                        corrected_answer = corrected_answer.replace('`', '').lower().strip()
                        corrected_answer = corrected_answer.replace('.', '').lower().strip()
                        if user_ans == corrected_answer:
                            ok = True
                print('CORRECTED ANS ', corrected_answer)
                print('---------')
                if ok == True:
                    corrected_text = 'CORRECT'
                    session['score_fill'] += 1
                else:
                    corrected_text = 'INCORRECT'
                    wrong_questions.append(question)
                    session['wrong_questions_fill'] = wrong_questions
                # print('____')
            else:
                corrected_text = 'INCORRECT'
                wrong_questions.append(question)
                session['wrong_questions_fill'] = wrong_questions
            
            return render_template('fibqs_detail.html', question=question, corrected_text=corrected_text,
                           feedback1=feedback1, feedback2=feedback2, feedback3=feedback3)
        elif choice == 'next':
            if index == total - 1:
                return redirect(url_for('result'))
            else:
                session['index_fill'] += 1
                return redirect(url_for('fibqs_detail'))
    return render_template('fibqs_detail.html', question=question, corrected_text=corrected_text,
                           feedback1=feedback1, feedback2=feedback2, feedback3=feedback3)

@app.route('/result', methods=['GET', 'POST'])
def result():
    score = session.get('score')
    total = session.get('total')
    wrong_questions = session.get('wrong_questions')
    wrong_questions = str(wrong_questions)
    topic = session.get('topic')
    options= session.get('options')
    # reference = session.get('reference')
    user_id = session.get('user_id')
    questions = session.get('questions')
    level = session.get('level_of_questions')
    # options = 
    
    print('wrong questions ', wrong_questions, ' - ', type(wrong_questions))
    print('---questions---')
    print(questions)
    print('-----END questions----')
    # llm = ReasoningLLM(course, context)
    res = (score / total) * 10
    response = None
    if res >= 8.0:
        response = "GOOD"
    else:
        response = "BAD"
    # res = int(res)
    if request.method == 'POST':
        choose = request.form.get('btn')
        new_questions, questions_from_db = None, None
        string_of_questions_from_db = ''
        QAs = []
        
        multi_agent = MultiAgent()
        handling = Handling()
        # llm = LLM()
        user_question_db = UserQuestionDB()
        
        if choose == 'stop':
            user_question_db.delete_all()
            return redirect(url_for('level'))
        elif choose == 'level up':
            # level-up mcqs
            multi_agent.level_up_MCQs(questions, total, topic)
            new_questions = multi_agent.get_MCQs()
            # new_questions = llm.level_up_MCQs(questions, total, topic)
            print('QUESTIONS LEVEL-UP')
            print(new_questions)
            print('-----------')
            session['questions'] += new_questions
            
        elif choose == 'retake':
            # using_LLM = False
            questions_from_db = user_question_db.get_user_question(user_id)
                
            len_of_questions = len(questions_from_db)
            
            if len_of_questions < total:
                # LLM 
                # retake the test
                multi_agent.retake_MCQs(questions, total, topic, wrong_questions)
                new_questions = multi_agent.get_MCQs()
                # new_questions = llm.retake_MCQs(questions, wrong_questions, total,  topic)
                print('QUESTIONS RETAKE')
                print(new_questions)
                print('-----------')
                session['questions'] = new_questions
            
                if total == 5:
                    questions_lst = handling.split_5_mcqs(new_questions)
                elif total == 10:
                    questions_lst = handling.split_10_mcqs(new_questions)
                elif total == 15:
                    questions_lst = handling.split_15_mcqs(new_questions)
                    
                for i in questions_lst:
                    question, answer_lst, feedback_lst, corrected_ans = handling.split_QA(i)
                    qa = []
                    qa.append(question)
                    for answer in answer_lst:
                        qa.append(answer)
                    for feedback in feedback_lst:
                        qa.append(feedback)
                    qa.append(corrected_ans)
                    QAs.append(qa)
            else:
                # show full DB
                for i in questions_from_db:
                    qa = []
                    question_id, question, label1, label2, label3, label4, answer, explanation, appear = i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]
                    
                    string_of_questions_from_db += i[1] + 'A) ' + i[2] + 'B) ' + i[3] + 'C) ' + i[4] + 'D) ' + i[5] + i[7]
                    
                    qa.append(question)
                    
                    qa.append(label1)
                    qa.append(label2)
                    qa.append(label3)
                    qa.append(label4)
                    
                    feedback_lst = handling.split_explanation(explanation)
                    qa.append(feedback_lst[0])
                    qa.append(feedback_lst[1])
                    qa.append(answer)
                    
                    QAs.append(qa)
            
                session['questions'] = string_of_questions_from_db
        # print('-----QAs----')
        # print(QAs)
        # print('------------')
        # wrong_questions = []
        session['wrong_questions'] = []
        session['index'] = 0
        session['QAs'] = QAs
        session['score'] = 0
        return redirect(url_for('mcqs_detail'))
    return render_template('result.html', result=score, total=total, response=response)

@app.route('/add_course', methods=['GET', 'POST'])
def add_course():
    app.config['UPLOAD_FOLDER_IMAGE'] = './static/photos'
    if request.method == 'POST':
        course_db = CourseDB()
        course = request.form.get('course')
        code = request.form.get('code')
        
        if course == None or code == None:
            return 'Please full-fill the form!'
        
        # Check if the post request has the file part
        if 'image' not in request.files:
            return 'No file part'
        
        file = request.files['image']
        
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return 'No selected file'
        
        # Get file extension and check if allowed
        file_ext = file.filename.rsplit('.', 1)[1].lower()
        allowed = file_ext in ALLOWED_EXTENSIONS_IMAGE
        
        if file and allowed:
            # Create a new filename using just the course code
            new_filename = f"{code}.{file_ext}"
            new_filename = secure_filename(new_filename)  # Use new_filename, not file.new_filename
            
            # Make sure the upload directory exists
            os.makedirs(app.config['UPLOAD_FOLDER_IMAGE'], exist_ok=True)
            
            file_path = os.path.join(app.config['UPLOAD_FOLDER_IMAGE'], new_filename)
            file.save(file_path)
            
            # Update database
            course_db.create_course(course, code)
            return f'Course "{course}" added with image: {new_filename}'
        else:
            return f"File type not allowed. Allowed image types are: {', '.join(ALLOWED_EXTENSIONS_IMAGE)}"
    
    return render_template('add_course.html')

if __name__ == '__main__':
    app.run(debug=True)
    