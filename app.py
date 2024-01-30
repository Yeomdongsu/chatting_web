from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from Chatgpt import ChatgptResource
from TextToSpeech import TextToSpeechResource
from config import Config

app = Flask(__name__)

# 환경변수 세팅
app.config.from_object(Config)
# JWT 매니저를 초기화
jwt = JWTManager(app)

api = Api(app)

api.add_resource(ChatgptResource, "/gpt")
api.add_resource(TextToSpeechResource, "/tts")

if __name__ == "__main__" : 
    app.run()
