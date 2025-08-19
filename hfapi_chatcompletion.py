from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

def completar_chat(mensagens):
    cliente = InferenceClient(model="meta-llama/Llama-3.2-3B-Instruct")

    resposta = cliente.chat_completion(mensagens)

    resposta_ia = resposta.choices[0]
    role_resposta = resposta_ia.message.role
    content_resposta = resposta_ia.message.content

    dicionario_resposta_ia = {"role": role_resposta, "content": content_resposta}
    mensagens.append(dicionario_resposta_ia)
    return mensagens

