
import streamlit as st
import traceback

from utils.youtube import get_youtube_video_id
from utils.transcript import get_transcript
from utils.video_info import get_video_info

from rag.splitter import create_chunks
from rag.embeddings import load_embedding_model
from rag.vector_store import create_vector_store
from rag.retriever import create_retriever
from rag.chain import create_rag_chain



# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="YouTube RAG Assistant",
    page_icon="🎥",
    layout="wide",
)

st.title("🎥 YouTube RAG Assistant")
st.caption("Chat with any YouTube video using Retrieval-Augmented Generation (RAG).")


# -------------------------------------------------------
# Session State Initialization
# -------------------------------------------------------

if "knowledge_ready" not in st.session_state:
    st.session_state.knowledge_ready = False

if "messages" not in st.session_state:
    st.session_state.messages = []

if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

if "video_info" not in st.session_state:
    st.session_state.video_info = None


# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------

with st.sidebar:

    st.title("⚙️ Settings")

    languages = {
        "English": "en",
        "Hindi": "hi",
        "Spanish": "es",
        "French": "fr",
        "German": "de",
        "Japanese": "ja",
        "Korean": "ko",
        "Portuguese": "pt",
        "Italian": "it",
        "Russian": "ru",
    }

    selected_language = st.selectbox(
        "Transcript Language",
        list(languages.keys())
    )

    st.divider()

    if st.session_state.knowledge_ready:

        st.success("✅ Knowledge Base Ready")

        st.metric(
            "Chunks",
            len(st.session_state.chunks)
        )

        st.metric(
        "Words",
        f"{len(st.session_state.transcript.split()):,}"
        )

        st.metric(
            "Characters",
            len(st.session_state.transcript)
        )


# -------------------------------------------------------
# Main UI
# -------------------------------------------------------

youtube_url = st.text_input(
    "🔗 Enter YouTube URL"
)

process = st.button(
    "🚀 Process Video",
    use_container_width=True
)


# -------------------------------------------------------
# Process Video
# -------------------------------------------------------

if process:

    if not youtube_url:

        st.warning("Please enter a YouTube URL.")

        st.stop()

    try:

        video_id = get_youtube_video_id(youtube_url)

        if video_id is None:

            st.error("Invalid YouTube URL.")

            st.stop()

        video_info = get_video_info(youtube_url)

        if video_info:

            col1, col2 = st.columns([1, 3])

            with col1:

                st.image(
                    video_info["thumbnail"],
                    use_container_width=True,
                )

            with col2:

                st.subheader(video_info["title"])

        # ----------------------------------------
        # Transcript
        # ----------------------------------------

        with st.spinner("Fetching transcript..."):

            transcript, detected_language = get_transcript(
                video_id,
                [languages[selected_language]],
            )

        st.success("Transcript Loaded")

        # ----------------------------------------
        # RAG Pipeline
        # ----------------------------------------

        with st.spinner("Building Knowledge Base..."):

            chunks = create_chunks(transcript)

            embeddings = load_embedding_model()

            vector_store = create_vector_store(
                chunks,
                embeddings,
            )

            retriever = create_retriever(
                vector_store
            )

            rag_chain = create_rag_chain(
                retriever
            )

        # ----------------------------------------
        # Save Everything
        # ----------------------------------------

        st.session_state.knowledge_ready = True

        st.session_state.video_info = video_info
        st.session_state.language = detected_language

        st.session_state.video_id = video_id

        st.session_state.transcript = transcript

        st.session_state.chunks = chunks

        st.session_state.retriever = retriever

        st.session_state.vector_store = vector_store

        st.session_state.rag_chain = rag_chain

        st.session_state.messages = []

        st.success("🎉 Knowledge Base Created Successfully!")
        st.info(f"📺 {video_info['title']}")

    except Exception as e:

        st.error(str(e))

        traceback.print_exc()

        # -------------------------------------------------------
# Chat Section
# -------------------------------------------------------

if st.session_state.knowledge_ready:

    st.divider()
    if st.button("🗑️ Clear Chat", use_container_width=True):
     st.session_state.messages = []
     st.rerun()

    st.header("💬 Chat with the Video")

    # Show previous messages

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    # User Input

    question = st.chat_input(
        "Ask anything about the video..."
    )

    if question:

        # Save User Message

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question,
            }
        )

        with st.chat_message("user"):

            st.markdown(question)

        # Generate Answer

        with st.chat_message("assistant"):

            with st.spinner("Analyzing video..."):

                try:

                   answer = st.session_state.rag_chain.invoke(question)

                   st.markdown(answer)

                   st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer,
                        }
                    )
                    

                except Exception as e:

                    st.error(e)