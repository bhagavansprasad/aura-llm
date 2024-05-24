import ollama
import time
import os
import json

def parse_file(fname):
    with open(fname) as rfd:
        paragraphs= []
        buffer = []
        for line in rfd.readlines():
            line = line.strip()
            if line:
                buffer.append(line)
            elif len(buffer):
                paragraphs.append(" ".join(buffer))
        if len(buffer):
            paragraphs.append(" ".join(buffer))
    return paragraphs

def save_embeddings(fname, embeddings):
    print("1. Saving embeddings")
    if not os.path.exists("embeddings"):
        os.mkdir("embeddings")

    print("2. Saving embeddings")
    with open(f"embeddings/{fname}.json", "w") as wfd:
        json.dump(embeddings, wfd)
    print("3. Saving embeddings")

def load_embeddings(fname):
    print("1. Load")
    if not os.path.exists(f"embeddings/{fname}.json"):
        print("2. Load")
        return False
    
    print("2. Load")
    with open(f"embeddings/{fname}.json", "r") as rfd:
        print("3. Load")
        return json.load(rfd)
            
def get_embeddings(fname, modelname, chunks):
    embed_retval = []
    
    if (embeddings := load_embeddings(fname)):
        return embeddings

    for i, chunk in enumerate(chunks):
        retval = ollama.embeddings(model=modelname, prompt=chunk)
        embed_retval.append(retval)
        print(f"Finished embedded para: {i}")
    
    print("4. Before saving")    
    save_embeddings(fname, embed_retval)
    print("5. After saving")    
    
    return embed_retval

def main():
    fname = "peter-pan.txt"
    paragraphs = parse_file(fname)
   
    start_time = time.perf_counter()
    # embeddings = get_embeddings(fname, "mistral", paragraphs)
    embeddings = get_embeddings(fname, "mistral", paragraphs[1:5])
    end_time = time.perf_counter()
    print(f"Processing time :{end_time-start_time}")
    print(f"Embedding count :{len(embeddings)}")
    
if(__name__ == "__main__"):
    main()