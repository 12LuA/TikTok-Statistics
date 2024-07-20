import utils.infos as infos
from typing import Dict, Any

def get_videos_commented(data: Dict[str, Any]) -> int:
    """
    Get the number of videos commented on since account registration.
    """
    videos_commented = data.get("Activity", {}).get("Activity Summary", {}).get("ActivitySummaryMap", {}).get("videosCommentedOnSinceAccountRegistration", 0)
    return videos_commented