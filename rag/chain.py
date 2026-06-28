from html import parser


from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough,
    RunnableLambda,
)
from langchain_core.output_parsers import StrOutputParser

from rag.llm import load_llm
from rag.prompt import prompt


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def create_rag_chain(retriever):

    llm = load_llm()

    parser = StrOutputParser()

    parallel = RunnableParallel(
    {
        "context": retriever | RunnableLambda(format_docs),
        "question": RunnablePassthrough(),
        
    }
)

    chain = parallel | RunnableLambda(lambda x: (print(x), x)[1]) | prompt | llm | parser


    return chain

      