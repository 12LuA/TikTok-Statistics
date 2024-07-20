import json
import os
import zipfile
import traceback
import pyfiglet
import utils.infos
from src.translator import get_language, get_standard_language, check_language
from src.selection_menu import send_selection_menu

def print_ascii_banner():
	ascii_banner = pyfiglet.figlet_format("TikTok-Statistics")
	print(ascii_banner)

def search_for_file(language: str):
	json_path = input(get_language(language)["main"]["specify_path"])

	# Check if the provided path is a directory
	if os.path.isdir(json_path):
		json_path = os.path.join(json_path, 'user_data_tiktok.json')

	# Check if the path is a ZIP file
	if json_path.endswith('.zip'):
		try:
			with zipfile.ZipFile(json_path, 'r') as zip_ref:
				# Extract the JSON file from the ZIP archive
				json_file_name = 'user_data_tiktok.json'
				if json_file_name in zip_ref.namelist():
					zip_ref.extract(json_file_name)
					json_path = json_file_name
				else:
					print(get_language(language)["main"]["zip_has_no_json"])
					search_for_file(language)
		except zipfile.BadZipFile:
			print(get_language(language)["main"]["file_not_in_zip"])
			search_for_file(language)

	try:
		# Open and load the JSON file
		with open(json_path, 'r', encoding='utf-8') as file:
			data = json.load(file)
			print(utils.infos.dividing_lines)
			send_selection_menu(data, language)
			#print(data)
			

	except FileNotFoundError:
		print(get_language(language)["main"]["file_not_found"])
		search_for_file(language)
	except json.JSONDecodeError:
		print(get_language(language)["main"]["file_not_json"])
		search_for_file(language)
	except Exception as e:
		print(get_language(language)["main"]["unknown_error"].format(error=e))
		print(traceback.format_exc())
		search_for_file(language)

def main():
	language = input("Please enter your language. Press Enter for English: ")
	
	if language == "":
		language = get_standard_language()
	else:
		check = check_language(language)
		if check is True:
			language = language.lower()
		else:
			main()
			return
	
	search_for_file(language)
		

if __name__ == "__main__":
	print_ascii_banner()
	main()