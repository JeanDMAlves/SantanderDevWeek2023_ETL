import requests
import json

class Potter_API:
    def __init__(self):
        self.base_url = "https://api.potterdb.com/v1"

    def get_books(self):
        response = requests.get(f"{self.base_url}/books")
        books = response.json()
        books = books["data"]
        books_preprocessed = {}
        for book in books:
            infos = {}
            infos["resumo"] = book["attributes"]["title"]
            infos["author"] = book["attributes"]["author"]
            infos["release_date"] = book["attributes"]["release_date"]
            infos["pages"] = book["attributes"]["pages"]
            books_preprocessed[book["attributes"]["title"]] = infos
        with open('books.json', 'w') as f:
            json.dump(books_preprocessed, f)
        return books_preprocessed
    
    def get_characters(self):
        response = requests.get(f"{self.base_url}/characters")
        characters = response.json()
        characters = characters["data"]
        characters_preprocessed = {}
        for character in characters:
            infos = {}
            infos["nasceu"] = character["attributes"]["born"]
            infos["morreu"] = character["attributes"]["died"]
            infos["genero"] = character["attributes"]["gender"]
            infos["wiki_url"] = character["attributes"]["wiki"]
            characters_preprocessed[character["attributes"]["name"]] = infos
        with open('characters.json', 'w') as f:
            json.dump(characters_preprocessed, f)
        return characters_preprocessed
    
if __name__== "__main__":
    api = Potter_API()
    print(api.get_books())
    print(api.get_characters())