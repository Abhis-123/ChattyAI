from chat import ChatBot
from flask import Flask, render_template, request

app = Flask(__name__)
chatbot = ChatBot(model_name = "microsoft/DialoGPT-medium")

@app.route("/chatbot")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot.process(userText)
app.run(debug = True)