import requests
import json

swapi_url = "https://swapi.dev/api/"


def swapi_get_people():
    """Получаем name/films по main персонажу"""
    main_people_url = f"{swapi_url}people/4/"
    main_character_get = requests.get(main_people_url).json()
    print(f"Персонаж: {main_character_get['name']}")
    main_character_films = main_character_get['films']
    print(f"Фильмы, в которых играл персонаж: {main_character_films}")

    """Получаем всех персонажей"""
    all_characters = []
    all_character_url = f"{swapi_url}people/"

    while all_character_url:
        page_data = requests.get(all_character_url).json()
        all_characters.extend(page_data['results'])
        all_character_url = page_data['next']

    """Ищем персонажей, у которых совпадают films с main персонажем"""
    characters_with_common_films = []
    main_films_set = set(main_character_films)

    for character in all_characters:
        if character['name'] == main_character_get['name']:
            continue

        character_films_set = set(character['films'])
        common_films = main_films_set & character_films_set

        if common_films:
            characters_with_common_films.append({
                'name': character["name"],
                'common_films_count': len(common_films)
            })               
            print(f"Персонаж: {character["name"]}, общие фильмы: {common_films}")

    return characters_with_common_films, main_character_get['name']
  
def save_results_to_files(characters_list, main_character_name):
    """Сохранение результатов в файл TXT"""
    
    with open('colleagues_list.txt', 'w', encoding='utf-8') as file:
        file.write(f"Персонажи, снимавшиеся с {main_character_name}:\n\n")
        for i, character in enumerate(characters_list, 1):
            file.write(f"{character["name"]}\n")

    print("Результат сохранен в colleagues_list.txt")     

colleagues_stars, main_character_name = swapi_get_people()
save_results_to_files(colleagues_stars, main_character_name)