import utils.infos as infos
from typing import Dict, Any, List

def get_favorite_effects(data: Dict[str, Any]) -> int:
    """
    Get the count of favorite effects.

    :param data: The data to analyze. It should be a dictionary containing activity information.
    :return: The count of favorite effects.
    """
    favorite_effects_list: List[Any] = data.get("Activity", {}).get("Favorite Effects", {}).get("FavoriteEffectsList", [])
    favorite_effects_count: int = len(favorite_effects_list)

    return favorite_effects_count