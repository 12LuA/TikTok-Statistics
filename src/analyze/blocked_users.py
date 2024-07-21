import utils.infos as infos
from typing import Dict, Any, List

def get_blocked_users(data: Dict[str, Any]) -> int:
	"""
	Get the number of blocked users.
	"""
	block_list: List[Any] = data.get("App Settings", {}).get("Block", {}).get("BlockList", {})
	blocked_users: int = len(block_list)
	return blocked_users