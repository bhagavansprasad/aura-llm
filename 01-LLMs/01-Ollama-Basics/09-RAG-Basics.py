import ollama
import time

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

def get_embeddings(modelname, chunks):
    embed_retval = []
    for i, chunk in enumerate(chunks):
        retval = ollama.embeddings(model=modelname, prompt=chunk)
        # print(type(retval))
        # print(retval)
        # print (retval["embedding"])
        embed_retval.append(retval)
        print(f"Finished embedded para: {i}")

    return embed_retval
    
def main():
    fname = "peter-pan.txt"
    paragraphs = parse_file(fname)
    # print(paragraphs[:10])
    
    start_time = time.perf_counter()
    embeddings = get_embeddings("mistral", paragraphs[1:10])
    end_time = time.perf_counter()
    print(f"Processing time :{end_time-start_time}")
    print(f"Embedding count :{len(embeddings)}")
    
if(__name__ == "__main__"):
    main()