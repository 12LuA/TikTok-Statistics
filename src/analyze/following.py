import utils.infos as infos
from typing import Dict, Any, List

def get_following(data: Dict[str, Any]) -> int:
	"""
	Get the count of following.

	:param data: The data to analyze. It should be a dictionary containing activity information.
	:return: The count of following.
	"""
	following_list: List[Any] = data.get("Activity", {}).get("Following List", {}).get("Following", [])
	following_count: int = len(following_list)

	return following_count