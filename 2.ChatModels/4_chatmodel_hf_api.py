
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv


load_dotenv()



llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen3.5-4B",
    task="text-generation",
   
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Write a poem about the beauty of nature.")
print(result.content)
