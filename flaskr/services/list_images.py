import os
from typing import List
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

    def _get_images(self, characters_index:List) -> List:
        final_images = []
        if path_images := Config.get('PATH_IMAGES'):
            for _, _, files in os.walk(os.path.abspath(path_images)):
                for index, file_name in enumerate(files):
                    image_read = 's' if index in characters_index else 'n'
                    final_images.append({
                        'file_name':file_name,
                        'read':image_read
                    })
        return final_images

    def execute(self) -> List:
        characters_index = self._get_characters_read_index()
        return self._get_images(characters_index)
