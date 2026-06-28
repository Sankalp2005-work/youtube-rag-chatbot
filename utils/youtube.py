
from urllib.parse import urlparse, parse_qs


def get_youtube_video_id(url):
    if not url:
        return None

    url = url.strip()
    parsed = urlparse(url)

    hostname = (parsed.hostname or "").lower()

    if hostname in ["www.youtube.com", "youtube.com", "m.youtube.com"]:

        if parsed.path == "/watch":
            return parse_qs(parsed.query).get("v", [None])[0]

        if parsed.path.startswith("/shorts/"):
            return parsed.path.split("/")[2]

        if parsed.path.startswith("/embed/"):
            return parsed.path.split("/")[2]

    elif hostname == "youtu.be":
        return parsed.path.lstrip("/")

    return None