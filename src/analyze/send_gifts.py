import utils.infos as infos
from typing import Dict, Any, List

def get_sended_gifts(data: Dict[str, Any]) -> int:
	"""
	Get the count of sent gifts.
	"""
	sent_gift_list: List[Any] = data.get("Activity", {}).get("Purchase History", {}).get("SendGifts", {}).get("SendGifts", [])
	sent_gift_count: int = len(sent_gift_list)
	return sent_gift_count