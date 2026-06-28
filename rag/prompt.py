from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
"""
You are an expert AI assistant.

Answer ONLY using the provided transcript context.

If the answer is not in the transcript, reply:

"I couldn't find that information in the video."

------------------------


------------------------
Transcript Context

{context}

------------------------
Current Question

{question}

------------------------
Answer
"""
)