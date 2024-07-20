import utils.infos as infos
from typing import Dict, Any
from src.translator import get_language, get_standard_language, check_language

def get_videos_commented(data: Dict[str, Any], language: str) -> str:
    """
    Get the number of videos commented on since account registration.
    """
    translation = get_language(language)["text_summary"]

    videos_commented = data.get("Activity", {}).get("Activity Summary", {}).get("ActivitySummaryMap", {}).get("videosCommentedOnSinceAccountRegistration", 0)
    return translation["videos_Commented_On_Since_Account_Registration"].format(data=infos.number_with_commas(videos_commented))