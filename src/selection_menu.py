import json
import utils.infos
from src.translator import get_language, get_standard_language, check_language
from src.text_summary.summary import analyze_data
from src.constants import UNDERLINE_START, UNDERLINE_END


def send_selection_menu(data, language: str):
    title_before = get_language(language)["selection_menu"]["title"]
    title = f"{UNDERLINE_START}{title_before}{UNDERLINE_END}"
    option_1 = get_language(language)["selection_menu"]["option_1"]
    option_2 = get_language(language)["selection_menu"]["option_2"]

    text = f"{title}\n{option_1}\n{option_2}\n{utils.infos.dividing_lines}\n"

    selection = input(text)
    if selection == "1":
        analyze_data(data, language)
       