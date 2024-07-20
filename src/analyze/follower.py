import utils.infos as infos
from typing import Dict, Any, List

def get_followers(data: Dict[str, Any]) -> int:
	"""
	Get the count of followers.

	:param data: The data to analyze. It should be a dictionary containing activity information.
	:return: The count of followers.
	"""
	followers_list: List[Any] = data.get("Activity", {}).get("Follower List", {}).get("FansList", [])
	followers_count: int = len(followers_list)

	return followers_count