import json
import utils.infos as infos
from typing import Dict, Any
from src.translator import get_language, get_standard_language, check_language
from src.analyze.videos_commented import get_videos_commented
from src.analyze.videos_shared import get_videos_shared
from src.analyze.favorite_effects import get_favorite_effects
from src.analyze.favorite_hashtags import get_favorite_hashtags
from src.analyze.favorite_sounds import get_favorite_sounds
from src.analyze.favorite_videos import get_favorite_videos
from src.analyze.follower import get_followers
from src.analyze.following import get_following
from src.analyze.likes import get_likes
from src.analyze.send_gifts import get_sended_gifts
from src.analyze.buyed_gifts import get_buyed_gifts
from src.analyze.interests import get_interests
from src.analyze.blocked_users import get_blocked_users

def analyze_data(data: Dict[str, Any], language: str):
    """
    Analyze the data and return the summary.
    """

    translation = get_language(language)["text_summary"]

    # ActivitySummary
    videos_commented = get_videos_commented(data)
    videos_shared = get_videos_shared(data)
    videos_Watched_To_The_End_Since_Account_Registration = data["Activity"]["Activity Summary"]["ActivitySummaryMap"]["videosWatchedToTheEndSinceAccountRegistration"]

    videos_commented = translation["videos_Commented_On_Since_Account_Registration"].format(data=infos.number_with_commas(videos_commented))
    videos_shared = translation["videos_Shared_Since_Account_Registration"].format(data=infos.number_with_commas(videos_shared))
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
    likes = get_likes(data)

    print(translation["followers"].format(data=followers))
    print(translation["following"].format(data=following))
    print(translation["likes"].format(data=infos.number_with_commas(likes)))

    # sendet items

    sendet_gifts = get_sended_gifts(data)
    buyed_gifts = get_buyed_gifts(data)

    print(translation["sendet_gifts"].format(data=infos.number_with_commas(sendet_gifts)))
    print(translation["buyed_gifts"].format(data=infos.number_with_commas(buyed_gifts)))


    # Interests
    interests = get_interests(data)
    print(translation["interests"].format(data=interests))

    # Block
    blocked_users = get_blocked_users(data)
    print(translation["blocked_users"].format(data=infos.number_with_commas(blocked_users)))
