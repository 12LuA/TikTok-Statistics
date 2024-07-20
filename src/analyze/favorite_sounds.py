import utils.infos as infos
from typing import Dict, Any, List

def get_favorite_sounds(data: Dict[str, Any]) -> int:
    """
    Get the count of favorite sounds.

    :param data: The data to analyze. It should be a dictionary containing activity information.
    :return: The count of favorite sounds.
    """
    favorite_sounds_list: List[Any] = data.get("Activity", {}).get("Favorite Sounds", {}).get("FavoriteSoundList", [])
    favorite_sounds_count: int = len(favorite_sounds_list)

    return favorite_sounds_count