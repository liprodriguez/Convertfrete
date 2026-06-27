from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Flask on Vercel! This is a placeholder for your Streamlit app."})

# Este é o ponto de entrada que o Vercel espera para um aplicativo Python.
# O Streamlit não é um aplicativo WSGI/ASGI como o Flask, então ele não pode ser servido diretamente aqui.
# Para rodar o Streamlit no Vercel, seria necessário um setup mais complexo (ex: proxy reverso).
