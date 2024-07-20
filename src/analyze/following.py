import utils.infos as infos
from typing import Dict, Any, List
from src.translator import get_language

def get_following(data: Dict[str, Any], language: str) -> str:
	"""
	Get the following summary.

	:param data: The data to analyze. It should be a dictionary containing activity information.
	:param language: The language code to use for translation.
	:return: The following summary as a formatted string.
	"""
	try:
		translation = get_language(language)["text_summary"]["following"]
	except KeyError:
		raise ValueError(f"Translation for language '{language}' not found.")

	following_list: List[Any] = data.get("Activity", {}).get("Following List", {}).get("FollowingList", [])
	following_count: int = len(following_list)

	return translation.format(data=infos.number_with_commas(following_count))