import utils.infos as infos
from typing import Dict, Any, List

def get_favorite_hashtags(data: Dict[str, Any]) -> int:
    """
    Get the count of favorite hashtags.

    :param data: The data to analyze. It should be a dictionary containing activity information.
    :return: The count of favorite hashtags.
    """
    favorite_hashtags_list: List[Any] = data.get("Activity", {}).get("Favorite Hashtags", {}).get("FavoriteHashtagList", [])
    favorite_hashtags_count: int = len(favorite_hashtags_list)

    return favorite_hashtags_count