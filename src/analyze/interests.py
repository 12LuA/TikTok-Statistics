import utils.infos as infos
from typing import Dict, Any, List

def get_interests(data: Dict[str, Any]) -> int:
	"""
    Get the interests.
    """
	interests = data["Ads and data"]["Ad Interests"]["AdInterestCategories"]
	return interests