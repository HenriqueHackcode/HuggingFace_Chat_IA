from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

def resumir(texto):
    cliente = InferenceClient()
    resposta = cliente.summarization(texto, model="facebook/bart-large-cnn")
    return resposta.summary_text
