import os
from openai import OpenAI
OPENAI_API_KEY="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"
OPENAI_API_KEY="sk-proj-4tO8UNyNDD9tF5rcGgHtT3BlbkFJQMJn51gYjqfnQOC68qDV"
client = OpenAI(
    # api_key = os.getenv("OPENAI_API_KEY"),
    api_key = OPENAI_API_KEY,
)

prompt = "Tell me a joke"

completion = client.completions.create(
  model = "gpt-3.5-turbo-instruct",
  prompt = prompt,
  max_tokens = 7,
  temperature = 0
)

print(completion.choices[0].text.strip())
