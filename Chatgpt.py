from flask import request
from flask_restful import Resource
import openai
from config import Config

openai.api_key = Config.OPENAI_API_KEY

class ChatgptResource(Resource) :
    def generate_text(self,prompt):
            response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0)
            return response.choices[0].text.replace("\n", "")
    
    def post(self) :
          data = request.get_json()
          
          res = self.generate_text(data["content"])
          print(res)
          return {"result" : "success", "ChatGPT" : res}, 200