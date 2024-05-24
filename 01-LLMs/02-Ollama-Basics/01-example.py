from openai import OpenAI

client = OpenAI(api_key='your-api-key')
prompt = "Once upon a time, in a faraway kingdom, there was a brave knight named Sir Lancelot. He embarked on a quest to..."
response = client.completions.create(engine="text-davinci-003")  # GPT-3 model you want to use
prompt=prompt,
max_tokens=100  # Adjust the length of the generated text)
generated_text = response.choices[0].text.strip()
print(generated_text)
