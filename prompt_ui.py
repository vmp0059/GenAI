import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

st.header("Research Tool")

user_input = st.text_input("Enter your prompt")

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7,
    max_tokens=200
)

if st.button("Generate"):
    if user_input:
        with st.spinner("Generating response..."):
            result = llm.invoke(user_input)

        st.subheader("Generated Response")
        st.write(result.content)
    else:
        st.warning("Please enter a prompt.")