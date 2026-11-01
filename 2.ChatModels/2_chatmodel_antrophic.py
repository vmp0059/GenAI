from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model= ChatAnthropic(model='claude-3-opus-20241217',temperature=0.7, max_completion_tokens=10)

result=model.invoke("Write a poem about the beauty of nature.")
print(result.content)