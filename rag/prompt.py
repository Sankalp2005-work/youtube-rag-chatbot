from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert AI assistant.

Use ONLY the transcript context.

Context:
{context}
"""
    ),
    MessagesPlaceholder("chat_history"),
    ("human", "{question}")
])