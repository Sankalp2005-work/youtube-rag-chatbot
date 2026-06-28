from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint

from dotenv import load_dotenv
load_dotenv()
def load_llm():
 llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    max_new_tokens=512,
    temperature=0.3,
)
 model=ChatHuggingFace(llm=llm)
 return model







