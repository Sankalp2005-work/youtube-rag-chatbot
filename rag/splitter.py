from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

def create_chunks(transcript):

    document = Document(page_content=transcript)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents([document])

    return chunks