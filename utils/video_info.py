import requests


def get_video_info(video_url):
    """
    Fetch YouTube video title and thumbnail.
    """

    endpoint = f"https://www.youtube.com/oembed?url={video_url}&format=json"

    try:
        response = requests.get(endpoint, timeout=10)

        if response.status_code == 200:
            data = response.json()

            return {
                "title": data["title"],
                "thumbnail": data["thumbnail_url"]
            }

    except Exception:
        pass

    return video_url, None