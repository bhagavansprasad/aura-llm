import ollama
import json

def o_show_model_details(mnames):
    print(mnames)
    for name in mnames:
        details = ollama.show(name)
        print(json.dumps(details, sort_keys=True, indent=4))
    
def o_list_models():
    data  = ollama.list()
    print(json.dumps(data, sort_keys=True, indent=4))
    
    for m in ollama.list()['models']:
        print(json.dumps(m, sort_keys=True, indent=4))

    for m in ollama.list()['models']:
        print(m['model'])

    localModels = [m['model'] for m in ollama.list()['models']]
    ModelNames = [m['name'] for m in ollama.list()['models']]
    
    print(localModels)
    print(ModelNames)
    return (ModelNames)

def main():
    mnames = o_list_models()
    o_show_model_details(mnames)
    
if(__name__ == "__main__"):
    main()