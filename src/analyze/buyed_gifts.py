import utils.infos as infos
from typing import Dict, Any, List

def get_buyed_gifts(data: Dict[str, Any]) -> int:
	"""
    Get the count of buyed gifts.
	"""
	buyed_gift_list: List[Any] = data.get("Activity", {}).get("Purchase History", {}).get("BuyGifts", {}).get("BuyGifts", [])
	buyed_gift_count: int = len(buyed_gift_list)
	return buyed_gift_count