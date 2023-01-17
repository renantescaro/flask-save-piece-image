import os
from typing import List, Tuple
from flaskr.utils.config import Config


class ListImages:
    def _get_characters_read_index(self) -> List:
        path_characters = Config.get('PATH_CHARACTERS')
        if not path_characters:
            return []

        characters_index = []
        for _, _, files in os.walk(os.path.abspath(path_characters)):
            for file_name in files:
                if '_' in file_name and '.png' in file_name:
                    _, image_index = file_name.replace('.png', '').split('_')
                    if image_index not in characters_index:
                        characters_index.append(int(image_index))
        return characters_index

    def _get_images(self, characters_index:List[int]) -> Tuple[List, int]:
        final_images = []
        number_read = 0
        if path_images := Config.get('PATH_IMAGES'):
            for _, _, files in os.walk(os.path.abspath(path_images)):
                for file_name in files:
                    index, name = file_name.split('_')

                    image_read = 's' if int(index) in characters_index else 'n'
                    number_read += 1 if image_read == 's' else 0
                    final_images.append({
                        'index':index,
                        'name':name,
                        'read':image_read
                    })
        return final_images, number_read

    def execute(self) -> Tuple[List, int]:
        characters_index = self._get_characters_read_index()
        return self._get_images(characters_index)
