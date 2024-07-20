import yaml
import os
import json
import langcodes

def get_standard_language():
    with open("config.json", "r", encoding='utf8') as config_file:
        config = json.load(config_file)
        return config.get("standard_language")
    

def check_language(language: str) -> bool:
    try:
        normalized_language = langcodes.standardize_tag(language)
    except langcodes.tag_parser.LanguageTagError:
        normalized_language = get_standard_language()

    language_file = f"languages/{normalized_language}.yaml"
    
    if os.path.exists(language_file):
        return True

    return False


def get_language(language: str):
    try:
        normalized_language = langcodes.standardize_tag(language)
    except langcodes.tag_parser.LanguageTagError:
        normalized_language = get_standard_language()

    language_file = f"languages/{normalized_language}.yaml"
    
    if not os.path.exists(language_file):
        normalized_language = get_standard_language()
        language_file = f"languages/{normalized_language}.yaml"

    with open(language_file, "r", encoding='utf8') as lang_file:
        lang_list = yaml.load(lang_file, Loader=yaml.FullLoader)
        return lang_list
