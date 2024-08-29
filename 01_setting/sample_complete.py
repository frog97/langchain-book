import json
import os
import openai

from openai import AzureOpenAI

RESOURCE_NAME = "lge-chatgpt-020"
DEPLOYEMNT_NAME = "gpt-4"
client = AzureOpenAI(
  azure_endpoint = "https://"+RESOURCE_NAME+".openai.azure.com/", 
  api_key=os.getenv("AZURE_40OPENAI_KEY"),  
  api_version="2024-02-15-preview"
)


response = client.completions.create(  #←ChatCompletion 대신 Completion을 사용
    model=DEPLOYEMNT_NAME,
    prompt="오늘 날씨가 매우 좋고 기분이",  #←prompt를 지정
    stop=".",  #←문자가 나타나면 문장 종료
    max_tokens=100,  #← 최대 토큰 수
    n=2,  #← 생성할 문장 수
    temperature=0.5  #←다양성을 나타내는 매개변수
)   

# Convert the response to a dictionary before serializing it to JSON
response_dict = response.dict()

print(json.dumps(response_dict, indent=2, ensure_ascii=False))


# RESOURCE_NAME = "lge-chatgpt-014"
# DEPLOYEMNT_NAME = "gpt-35-turbo"
# client = AzureOpenAI(
#   azure_endpoint = "https://"+RESOURCE_NAME+".openai.azure.com/", 
#   api_key=os.getenv("AZURE_35OPENAI_KEY"),  
#   api_version="2024-02-15-preview"
# )


# response = client.completions.create(  #←ChatCompletion 대신 Completion을 사용
#     model=DEPLOYEMNT_NAME,
#     prompt="오늘 날씨가 매우 좋고 기분이",  #←prompt를 지정
#     stop=".",  #←문자가 나타나면 문장 종료
#     max_tokens=100,  #← 최대 토큰 수
#     n=2,  #← 생성할 문장 수
#     temperature=0.5  #←다양성을 나타내는 매개변수
# )   

# # Convert the response to a dictionary before serializing it to JSON
# response_dict = response.dict()

# print(json.dumps(response_dict, indent=2, ensure_ascii=False))