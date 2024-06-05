import json
import os
# import openai  #← OpenAI에서 제공하는 Python 패키지 가져오기
from openai import AzureOpenAI


RESOURCE_NAME = "lge-chatgpt-014"
DEPLOYEMNT_NAME = "gpt-35-turbo"
client = AzureOpenAI(
  azure_endpoint = "https://"+RESOURCE_NAME+".openai.azure.com/", 
  api_key=os.getenv("AZURE_OPENAI_KEY"),  
  api_version="2024-02-15-preview"
)

response = client.completions.create(  #←OpenAI API를 호출하여 언어 모델을 호출합니다.
    model=DEPLOYEMNT_NAME,  #← 호출할 언어 모델의 이름
    messages=[
        {
            "role": "user",
            "content": "iPhone8 출시일을 알려주세요"  #←입력할 문장(프롬프트)
        },
    ]
)
response_dict = response.dict()

print(json.dumps(response_dict, indent=2, ensure_ascii=False))
