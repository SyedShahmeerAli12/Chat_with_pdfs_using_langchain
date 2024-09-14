import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
import os
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from html_templates import css, bot_template, user_template
from datetime import datetime
from langchain_huggingface import HuggingFaceEndpoint
load_dotenv()



def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    hf_embed = HuggingFaceEmbeddings(model_name=model_name)
    db = FAISS.from_texts(texts=text_chunks, embedding=hf_embed)
    return db


def get_conversation_chain(vectorstore):
    llm = HuggingFaceEndpoint(
            repo_id="mistralai/Mistral-7B-Instruct-v0.3",
            huggingfacehub_api_token="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"
        )

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain


def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    # Loop through chat history to display messages
    for i, message in enumerate(st.session_state.chat_history):
        timestamp = datetime.now().strftime("%I:%M %p")  # Current time format
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content).replace("{{TIME}}", timestamp), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content).replace("{{TIME}}", timestamp), unsafe_allow_html=True)


def main():
    st.set_page_config(page_title="Chat with multiple PDFs",
                       page_icon=":books:", layout="wide")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    # Display date divider
    today = datetime.now().strftime("%A, %B %d")
    st.markdown(f"<div class='date-divider'>{today}</div>", unsafe_allow_html=True)

    # Chat UI
    user_question = st.text_input("Type your message:", key="user_input", placeholder="Type a message...")
    if user_question:
        handle_userinput(user_question)

    # PDF Upload Section (Collapsible)
    with st.expander("Upload your PDFs"):
        pdf_docs = st.file_uploader("Upload your PDFs here:", accept_multiple_files=True)
        if st.button("Process PDFs"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vectorstore = get_vectorstore(text_chunks)
                st.session_state.conversation = get_conversation_chain(vectorstore)


if __name__ == '__main__':
    main()
