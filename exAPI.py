import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)
modelo_alvo = "gemini-2.5-flash-lite"
chat = client.chats.create(model=modelo_alvo)

while True:
    pergunta = input("Você: ")

    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Encerrando o chat. Até mais!")
        break

    try:
        resposta = chat.send_message(pergunta)
        print("Gemini:", resposta.text)
        print("-" * 30)

    except Exception as e:
        print(f"\n[ERROR] Ocorreu um erro: {e}")

        