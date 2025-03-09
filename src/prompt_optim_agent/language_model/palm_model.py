import google.generativeai as palm
import time

class PaLMModel():
    def __init__(
        self,
        model_name: str,
        api_key: str,
        temperature: float,
        **kwargs):
        
        self.model = model_name
        self.temperature = temperature
        self._api_key_config(api_key)
        
        self.batch_forward_func = self.batch_forward_chatcompletion_palm
        
    def _api_key_config(self, api_key):
        # set up key from command
        if api_key is not None:
            print(f'Set PaLM2 API: {api_key}')
            palm.configure(api_key=api_key.strip())
        else:
            raise ValueError(f"api_key error: {api_key}")
    
    def batch_forward_chatcompletion_palm(self, batch_prompts):
        """
        Input a batch of prompts to PaLM chat API and retrieve the answers.
        """
        responses = []
        for prompt in batch_prompts:
            response = self.generate(prompt=prompt)

            if response is None:
                responses.append("N/A: no answer")
                continue

            responses.append(response)
        return responses

    def generate(self, prompt):
        backoff_time = 1
        while True:
            try:
                return palm.chat(messages=prompt, 
                                 temperature=self.temperature, 
                                 model=self.model).last.strip()
            except:
                print(f' Sleeping {backoff_time} seconds...')
                time.sleep(backoff_time)
                backoff_time *= 1.5

        
    
        
        