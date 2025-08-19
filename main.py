import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from hfapi_summarization import resumir
from hfapi_textgeneration import gerar_texto
from hfapi_chatcompletion import completar_chat

cliente = InferenceClient()

def gerador_texto(prompt):
    st.markdown("##### Peça para o sistema gerar um texto para você")
    if prompt:
        texto_resposta = gerar_texto(prompt)
        st.write(texto_resposta)

def resumidor_texto(prompt):
    st.markdown("##### Cole na caixa de prompt o texto que deseja resumir")
    if prompt:
        texto_resposta = resumir(prompt)
        st.write(texto_resposta)

def abrir_chat(prompt):
    st.markdown("##### Converse com a IA da Hashtag")

    if "mensagens" not in st.session_state:
        mensagens = [
            {"role": "system", "content": "Responda as perguntas de forma correta e precisa"},
        ]
        st.session_state["mensagens"] = mensagens
    else:
        mensagens = st.session_state["mensagens"]

    if prompt:
        mensagem_usuario = {"role": "user", "content": prompt}
        mensagens.append(mensagem_usuario)
        mensagens = completar_chat(mensagens)
        
        for dic_mensagem in mensagens:
            role = dic_mensagem["role"]
            content = dic_mensagem["content"]
            if role != "system":
                with st.chat_message(role):
                    st.write(content)



def main_app():
    
    st.header("HashIAs", divider=True)
    #
    st.markdown("#### Selecione a IA que mais te ajuda, envie seu prompt e seja feliz")
   
    opcoes = ["Gerar Texto", "Resumir Texto", "Abrir Chat"]
    ferramenta_selecionada = st.selectbox("Selecione a ferramenta de IA que você vai usar", options=opcoes)
    
   
    prompt = st.chat_input("Digite aqui seu prompt")

    if ferramenta_selecionada:
        if ferramenta_selecionada == opcoes[0]:
            gerador_texto(prompt)
        elif ferramenta_selecionada == opcoes[1]:
            resumidor_texto(prompt)
        else:
            abrir_chat(prompt)


main_app()