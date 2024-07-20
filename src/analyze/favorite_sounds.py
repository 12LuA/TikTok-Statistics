import utils.infos as infos
from typing import Dict, Any, List
from src.translator import get_language

def get_favorite_sounds(data: Dict[str, Any], language: str) -> str:
    """
    Get the favorite sounds summary.

    :param data: The data to analyze. It should be a dictionary containing activity information.
    :param language: The language code to use for translation.
    :return: The favorite sounds summary as a formatted string.
    """
    try:
        translation = get_language(language)["text_summary"]["favorite_sounds"]
    except KeyError:
        raise ValueError(f"Translation for language '{language}' not found.")

    favorite_sounds_list: List[Any] = data.get("Activity", {}).get("Favorite Sounds", {}).get("FavoriteSoundList", [])
    favorite_sounds_count: int = len(favorite_sounds_list)

    return translation.format(data=infos.number_with_commas(favorite_sounds_count))