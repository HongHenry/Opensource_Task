import os
import openai
from gensim.summarization.summarizer import summarize, keywords

openai.api_key = "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"
question = input("무엇을 물어볼까요?\n")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": question}
  ]
)

ksh_question = completion.choices[0].text
ksh_keyword = keywords(ksh_question, word_count=5)
ksh_strkeyword = ' ,'. join(ksh_keyword)

response = openai.Image.create(
  prompt=ksh_strkeyword,
  n=1,
  size="1024x1024"
)

image_url = response['data'][0]['url']

print(image_url)