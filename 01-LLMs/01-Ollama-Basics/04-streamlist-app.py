import streamlit as st

def streamlit_example():
    st.title("Ollama Python Chatbot")
    
    prompt = st.chat_input("What is up?")
    if prompt:
        with st.chat_message("user"): 
            st.markdown(prompt)

def main():
    streamlit_example()
    
if(__name__ == "__main__"):
    main()