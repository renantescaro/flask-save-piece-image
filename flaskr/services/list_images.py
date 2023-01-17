import os
from typing import List, Tuple
from flaskr.utils.config import Config


class ListImages:
    def __init__(self) -> None:
        self._path_images = Config.get('PATH_IMAGES')
        self._path_character = Config.get('PATH_CHARACTERS')

    def _get_files(self, path_files:str|None) -> List[str]:
        final_files = []
        if path_files:
            for _, _, files in os.walk(os.path.abspath(path_files)):
                final_files.extend(iter(files))
        return final_files

    def _is_improper_images(self, image_name:str) -> bool:
        return '(' in image_name

    def _delete_image(self, image_path:str) -> None:
        os.remove(f'{self._path_character}{image_path}')

    def _get_characters_read_index(self) -> List:
        characters_index = []
        files = self._get_files(self._path_character)

        for file_name in files:
            if '_' in file_name and '.png' in file_name:
                if self._is_improper_images(file_name):
                    self._delete_image(file_name)
                else:
                    _, image_index = file_name.replace('.png', '').split('_')
                    if image_index not in characters_index:
                        characters_index.append(int(image_index))
        return characters_index

    def _get_list_images(self) -> Tuple[List, int]:
        final_images = []
        number_read = 0
        characters_index = self._get_characters_read_index()
        images = self._get_files(self._path_images)

        for image_name in images:
            index, name = image_name.split('_')

            image_read = 's' if int(index) in characters_index else 'n'
            number_read += 1 if image_read == 's' else 0
            final_images.append({
                'index':index,
                'name':name,
                'read':image_read
            })
        return final_images, number_read

    def execute(self) -> Tuple[List, int]:
        return self._get_list_images()
