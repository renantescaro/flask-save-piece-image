import os
import string
from typing import List
from flaskr.utils.config import Config


class CheckPiece:
    def _get_characters_read_index(self) -> List[str]:
        path_characters = Config.get('PATH_CHARACTERS')
        if not path_characters:
            return []

        files_names = []
        for _, _, files in os.walk(os.path.abspath(path_characters)):
            for file_name in files:
                if '_' in file_name and '.png' in file_name:
                    name_file, _ = file_name.replace('.png', '').split('_')
                    files_names.append(name_file)
        return files_names

    def amount_characters(self):
        alphabet = list(string.ascii_lowercase)
        numbers = list(range(10))
        alphabet_and_numbers = alphabet + list(map(str, numbers))

        list_of_quantity = {}
        for character in alphabet_and_numbers:
            list_of_quantity[character] = 0

        characters = self._get_characters_read_index()
        for character in characters:
            list_of_quantity[character] += 1

        return list_of_quantity

    def five_characters_less(self):
        list_of_quantity = self.amount_characters()
        ordened_list = []
        for character in list_of_quantity:
            ordened_list.append({
                'quantity' : int(list_of_quantity[character]),
                'character': character
            })

        sorted_list = sorted(ordened_list, key=lambda d: d['quantity'])
        sorted_list_five = []
        for index in range(5):
            sorted_list_five.append({
                sorted_list[index]['character'] : sorted_list[index]['quantity']
            })
        return sorted_list_five
