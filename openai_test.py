import os
from openai import AzureOpenAI

RESOURCE_NAME = "lge-chatgpt-014"
DEPLOYEMNT_NAME = "gpt-35-turbo"
client = AzureOpenAI(
  azure_endpoint = "https://"+RESOURCE_NAME+".openai.azure.com/", 
  api_key=os.getenv("AZURE_OPENAI_KEY"),  
  api_version="2024-02-15-preview"
)


message_text = [{"role":"system","content":"You are an AI assistant that helps people find information."},{"role":"user","content":"안녕"},{"role":"assistant","content":"안녕하세요! 무엇을 도와드릴까요?"}]



completion = client.chat.completions.create(
  model=DEPLOYEMNT_NAME,
  messages = message_text,
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)

print(completion)