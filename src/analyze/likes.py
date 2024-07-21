import utils.infos as infos
from typing import Dict, Any, List

def get_likes(data: Dict[str, Any]) -> int:
	"""
    Get the count of likes.
    """
	like_list: List[Any] = data.get("Activity", {}).get("Like List", {}).get("ItemFavoriteList", [])
	likes: int = len(like_list)
	return likes