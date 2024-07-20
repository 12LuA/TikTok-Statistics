import utils.infos as infos
from typing import Dict, Any, List
from src.translator import get_language

def get_favorite_videos(data: Dict[str, Any], language: str) -> str:
    """
    Get the favorite videos summary.

    :param data: The data to analyze. It should be a dictionary containing activity information.
    :param language: The language code to use for translation.
    :return: The favorite videos summary as a formatted string.
    """
    try:
        translation = get_language(language)["text_summary"]["favorite_videos"]
    except KeyError:
        raise ValueError(f"Translation for language '{language}' not found.")

    favorite_videos_list: List[Any] = data.get("Activity", {}).get("Favorite Videos", {}).get("FavoriteVideoList", [])
    favorite_videos_count: int = len(favorite_videos_list)

    return translation.format(data=infos.number_with_commas(favorite_videos_count))