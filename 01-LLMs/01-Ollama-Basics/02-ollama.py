import ollama
import json

def o_chat_with_model(llm_name):
    message = [
        {
            'role': 'user',
            'content': 'How old the Indian History?'      
         }
    ]
    reply = ollama.chat(model=llm_name, messages=message, stream=False)
    print(reply)
    print(reply['content'])

def main():
    llm_name = 'mistral'
    mnames = o_chat_with_model(llm_name)
    
if(__name__ == "__main__"):
    main()