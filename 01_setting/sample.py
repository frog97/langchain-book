import json
import os
# import openai  #← OpenAI에서 제공하는 Python 패키지 가져오기
from openai import AzureOpenAI



RESOURCE_NAME = "lge-chatgpt-020"
DEPLOYEMNT_NAME = "gpt-4"
client = AzureOpenAI(
  azure_endpoint = "https://"+RESOURCE_NAME+".openai.azure.com/", 
  api_key=os.getenv("AZURE_40OPENAI_KEY"),  
  api_version="2024-02-15-preview"
)


response = client.chat.completions.create(
  model=DEPLOYEMNT_NAME,
  messages=[
    {"role": "user", "content": "iPhone8 출시일을 알려주세요"}
  ],
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)

response_dict = response.dict()

print(json.dumps(response_dict, indent=2, ensure_ascii=False))