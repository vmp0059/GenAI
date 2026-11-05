import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
load_dotenv()

st.header("Research Tool")

paper_input = st.selectbox("Select Research Paper Name", [ "Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners",
    "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7,
    # max_tokens=200
)

template=load_prompt("template.json")

#fill the placeholders
# prompt=template.invoke({
#     'paper_input':paper_input,
#     'style_input':style_input,
#     'length_input':length_input
# })

# if st.button("Generate"):
#     if prompt:
#         with st.spinner("Generating response..."):
#             result = llm.invoke(prompt)

#         st.subheader("Generated Response")
#         st.write(result.content)
#     else:
#         st.warning("Please enter a prompt.")


if st.button("Generate"):
    chain=template| llm
    result=chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(result.content)
        
    