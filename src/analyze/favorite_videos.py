import utils.infos as infos
from typing import Dict, Any, List

def get_favorite_videos(data: Dict[str, Any]) -> int:
    """
    Get the count of favorite videos.

    :param data: The data to analyze. It should be a dictionary containing activity information.
    :return: The count of favorite videos.
    """
    favorite_videos_list: List[Any] = data.get("Activity", {}).get("Favorite Videos", {}).get("FavoriteVideoList", [])
    favorite_videos_count: int = len(favorite_videos_list)

    return favorite_videos_count