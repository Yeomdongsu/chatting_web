from flask import request
from flask_restful import Resource
import openai
from config import Config

openai.api_key = Config.OPENAI_API_KEY

class ChatgptResource(Resource) :
    def generate_text(self,prompt):
            response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt + "writing style:Cold, Cynical, Pessimistic, Sarcastic",
            temperature=0.7,
            max_tokens=500,
            frequency_penalty=0,
            presence_penalty=0)
            return response.choices[0].text
    
    def post(self) :
          data = request.get_json()
          
          res = self.generate_text(f'답변은 짧고 간결하게 존댓말 쓰지 말고 반말로 한글로 대답해. 질문 : {data["content"]}')
          print(res)
          return {"result" : "success", "ChatGPT" : res}, 200
    
class ChatgptDiaryResource(Resource) :
    def generate_text(self,prompt):
                response = openai.Completion.create(
                engine="gpt-3.5-turbo-instruct",
                prompt=prompt + "writing style:Conversational, Empathetic",
                temperature=0.7,
                max_tokens=1000,
                frequency_penalty=0,
                presence_penalty=0)
                return response.choices[0].text
    
    def post(self) :
          data = request.get_json()

          res = self.generate_text(f'오늘 하루를 일기로 남기고 싶어. 내용을 보며 어울리는 말들도 덧붙여서 정말 사람이 쓴 것 처럼 길게 써줘. 제목, 날짜, 내용 순서로 구분 지어서 한국어로 써줘. 제목 : {data["title"]}, 날짜 : {data["date"]}, 내용 : {data["content"]}, 기분 : {data["emotion"]}')
          print(res)
          return {"result" : "success", "ChatGPT" : res}, 200          