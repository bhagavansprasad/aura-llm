import streamlit as st

def streamlit_example():
    st.title("Ollama Python Chatbot")
    
    # initialize history
    if "messages" not in st.session_state:
        st.session_state["messages"] = []
    
    # display chat messages from history
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("What is up?")
    if prompt:
        # add latest message to history in format {role, content}
        data = {"role": "user", "content": prompt}
        st.session_state["messages"].append(data)
        with st.chat_message("user"): 
            st.markdown(prompt)

def main():
    streamlit_example()
    
if(__name__ == "__main__"):
    main()