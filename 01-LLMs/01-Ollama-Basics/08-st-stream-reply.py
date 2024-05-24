import ollama
import streamlit as st

def model_response_generator():
    stream = ollama.chat(
        model = st.session_state["model"],
        messages = st.session_state["messages"],
        stream=True
    )
    for chunk in stream:
        yield chunk["message"]["content"]
    
def streamlit_example():
    st.title("Ollama Python Chatbot")
    
    # initialize history
    if "messages" not in st.session_state:
        st.session_state["messages"] = []
    
    # init models
    if "model" not in st.session_state:
        st.session_state["model"] = ""
        
    models = [m['name'] for m in ollama.list()['models']]
    st.session_state["model"] = st.selectbox("Choose your model", models)
    model = st.session_state["model"]

    # display chat messages from history
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("What is up?")
    if not prompt:
        return 0 
        
    # add latest message to history in format {role, content}
    data = {"role": "user", "content": prompt}
    st.session_state["messages"].append(data)
    with st.chat_message("user"): 
        st.markdown(prompt)

    # communicate with llm
    with st.chat_message("assistant"):
        reply = st.write_stream(model_response_generator())
        st.session_state["messages"].append(reply)

def main():
    streamlit_example()
    
if(__name__ == "__main__"):
    main()