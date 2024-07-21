import utils.infos as infos
from typing import Dict, Any

def get_videos_shared(data: Dict[str, Any]) -> int:
    """
    Get the number of videos shared on since account registration.
    """
    videos_shared = data.get("Activity", {}).get("Activity Summary", {}).get("ActivitySummaryMap", {}).get("videosSharedSinceAccountRegistration", 0)
    return videos_shared