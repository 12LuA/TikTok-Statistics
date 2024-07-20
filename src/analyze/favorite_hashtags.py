import utils.infos as infos
from typing import Dict, Any, List
from src.translator import get_language

def get_favorite_hashtags(data: Dict[str, Any], language: str) -> str:
    """
    Get the favorite hashtags summary.
    :param data: The data to analyze.
    :param language: The language to use.
    :return: The favorite hashtags summary.
    """
    try:
        translation = get_language(language)["text_summary"]["favorite_hashtags"]
    except KeyError:
        raise ValueError(f"Translation for language '{language}' not found.")

    favorite_hashtags_list: List[Any] = data.get("Activity", {}).get("Favorite Hashtags", {}).get("FavoriteHashtagList", [])
    favorite_hashtags_count: int = len(favorite_hashtags_list)

    return translation.format(data=infos.number_with_commas(favorite_hashtags_count))