import json
import utils.infos as infos
from typing import Dict, Any
from src.translator import get_language, get_standard_language, check_language
from src.analyze.videos_commented import get_videos_commented
from src.analyze.favorite_effects import get_favorite_effects
from src.analyze.favorite_hashtags import get_favorite_hashtags
from src.analyze.favorite_sounds import get_favorite_sounds
from src.analyze.favorite_videos import get_favorite_videos
from src.analyze.follower import get_followers
from src.analyze.following import get_following

def analyze_data(data: Dict[str, Any], language: str):
    """
    Analyze the data and return the summary.
    """

    translation = get_language(language)["text_summary"]

    # ActivitySummary
    videos_Commented_On_Since_Account_Registration = data["Activity"]["Activity Summary"]["ActivitySummaryMap"]["videosCommentedOnSinceAccountRegistration"]
    videos_Shared_Since_Account_Registration = data["Activity"]["Activity Summary"]["ActivitySummaryMap"]["videosSharedSinceAccountRegistration"]
    videos_Watched_To_The_End_Since_Account_Registration = data["Activity"]["Activity Summary"]["ActivitySummaryMap"]["videosWatchedToTheEndSinceAccountRegistration"]

    videos_commented = translation["videos_Commented_On_Since_Account_Registration"].format(data=infos.number_with_commas(videos_Commented_On_Since_Account_Registration))
    videos_shared = translation["videos_Shared_Since_Account_Registration"].format(data=infos.number_with_commas(videos_Shared_Since_Account_Registration))
    videos_watched = translation["videos_Watched_To_The_End_Since_Account_Registration"].format(data=infos.number_with_commas(videos_Watched_To_The_End_Since_Account_Registration))

    print(videos_commented)
    print(videos_shared)
    print(videos_watched)

    # Favorites
    favorite_effects = get_favorite_effects(data)
    favorite_hashtags = get_favorite_hashtags(data)
    favorite_sounds = get_favorite_sounds(data)
    favorite_videos = get_favorite_videos(data)

    print(translation["favorite_effects"].format(data=favorite_effects))
    print(translation["favorite_hashtags"].format(data=favorite_hashtags))
    print(translation["favorite_sounds"].format(data=favorite_sounds))
    print(translation["favorite_videos"].format(data=favorite_videos))

    # Social
    followers = get_followers(data)
    following = get_following(data)

    print(translation["followers"].format(data=followers))
    print(translation["following"].format(data=following))
