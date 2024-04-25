import streamlit as st
from langchain_llm import get_db_chain

# Page title and layout settings
st.set_page_config(page_title="AtliQ T Shirts: Database Q&A 👕", layout="wide")

# Custom CSS styles to enhance appearance
st.markdown(
    """
    <style>
    .header-font {
        font-size: 36px;
        font-weight: bold;
        color: #1F2833;
        text-align: center;
        margin-bottom: 30px;
    }
    .question-input {
        width: 80%;
        padding: 10px;
        font-size: 18px;
        border: 2px solid #4CAF50;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    .answer-container {
        background-color: #F0F0F0;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        margin-top: 20px;
    }
    .answer-text {
        font-size: 20px;
        color: #1F2833;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1 class='header-font'>AtliQ T Shirts: Database Q&A 👕</h1>", unsafe_allow_html=True)

# Text input for user question
question = st.text_input("Question: ")

if question:
    # Get response from the model
    chain = get_db_chain()
    response = chain.run(question)

    # Display the answer
    st.markdown("<div class='answer-container'>", unsafe_allow_html=True)
    st.markdown("<p class='answer-text'><strong>Answer:</strong></p>", unsafe_allow_html=True)
    st.markdown(f"<p class='answer-text'>{response}</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
