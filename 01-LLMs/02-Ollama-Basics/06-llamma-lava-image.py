import requests
import json
import base64
import codecs
import numpy as np
import cv2

image_path= "./images/nvk-lavanya.jpg"
image_path= "./images/group.jpg"

# data = cv2.imread(image_path, 0)
# fd = codecs.open(image_path, "r", "utf-16")
fd = codecs.open(image_path, "rb")

# with open(image_path, "rb") as image_fd:
data = fd.read()
image_base64 = base64.b64encode(data)
# image_base64 = base64.b64encode(image_fd.read())

url = "http://localhost:11434/api/generate"

print(type(image_base64))
# payload = {
#         "model": "llava",
#         "prompt": "What is in this picture?",
#         "stream": False,
#         "images": [image_base64.decode("utf-8")]
# }

# response = requests.post(url, data=json.dumps(payload))
# print(response.text)


payload = {
        "model": "llava",
        "prompt": "can you genrate sample twitter data in json format?",
        "stream": False,
        "images": [image_base64.decode("utf-8")]
}

response = requests.post(url, data=json.dumps(payload))
print(response.text)
