import os

# model = 'open-mistral-nemo'
# model2 = 'mistral-large-2411'
# model_code = 'codestral-2501'


class MultiAgentMistral:
    
    def __init__(self):
        
        self.__config_list = [
            {
                # Let's choose the Mixtral 8x22B model
                "model": "mistral-large-2411",
                # Provide your Mistral AI API key here or put it into the MISTRAL_API_KEY environment variable.
                "api_key": os.environ.get("yTP3OlllcDaiqmgcoxJghetYuF9Z05fj"),
                # We specify the API Type as 'mistral' so it uses the Mistral AI client class
                "api_type": "mistral",
            }
        ]
        
    