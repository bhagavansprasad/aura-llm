import ollama

res = ollama.chat(
	model="llava",
	messages=[
		{
			'role': 'user',
			'content': 'Describe this image:',
			'images': ['./qp.pdf']
		}
	]
)

print(res['message']['content'])