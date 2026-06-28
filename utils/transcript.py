from youtube_transcript_api import (
    YouTubeTranscriptApi,
    NoTranscriptFound,
    TranscriptsDisabled,
    VideoUnavailable,
)

SUPPORTED_LANGUAGES = [
    "en",
    "hi",
    "es",
    "fr",
    "de",
    "ja",
    "ko",
    "pt",
    "it",
    "ru",
]


def get_transcript(video_id: str, languages=None):
    """
    Fetch transcript using a YouTube VIDEO ID.
    """

    if languages is None:
        languages = SUPPORTED_LANGUAGES

    try:
        api = YouTubeTranscriptApi()

        transcript = api.fetch(
            video_id,
            languages=languages
        )

        text = " ".join(snippet.text for snippet in transcript)

        return text, transcript.language

    except NoTranscriptFound:
        raise Exception("No transcript found in the selected language.")

    except TranscriptsDisabled:
        raise Exception("Transcripts are disabled for this video.")

    except VideoUnavailable:
        raise Exception("This video is unavailable.")

    except Exception as e:
        raise Exception(f"Failed to fetch transcript: {e}")
    
    