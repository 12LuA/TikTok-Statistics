import utils.infos as infos
from typing import Dict, Any, List
from src.translator import get_language

def get_followers(data: Dict[str, Any], language: str) -> str:
	"""
	Get the followers summary.

	:param data: The data to analyze. It should be a dictionary containing activity information.
	:param language: The language code to use for translation.
	:return: The followers summary as a formatted string.
	"""
	try:
		translation = get_language(language)["text_summary"]["followers"]
	except KeyError:
		raise ValueError(f"Translation for language '{language}' not found.")

	followers_list: List[Any] = data.get("Activity", {}).get("Follower List", {}).get("FansList", [])
	followers_count: int = len(followers_list)

	return translation.format(data=infos.number_with_commas(followers_count))