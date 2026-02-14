from pathlib import Path
from zipfile import ZipFile

DEFAULT_ENCONDING = 'utf-8'

class FileReader():
    def __init__(self,file_path, encoding = DEFAULT_ENCONDING):
        self.path = file_path
        self.__encoding = encoding

    def read(self):
        return self.path.read_text(self.__encoding)


class FileWriter():
    def __init__(self, file_path: str, encoding: str = DEFAULT_ENCONDING):
        self._path = Path(file_path)
        self._encoding = encoding
 
    def write(self, content: str):
        self._path.write_text(content, self._encoding)


class FileCompressor():
    def __init__(self, file_path):
        self.path = file_path

    def compress(self):
        with ZipFile(self.path.with_suffix('.zip'), mode='w') as file:
            file.write(self.path)


def add_greeting( content: str) -> str:
    return content + '\nHello world!'



if __name__ == '__main__':
    file_path = Path('data.txt')
    content = FileReader(file_path).read()
    FileWriter(file_path).write(add_greeting(content))
    FileCompressor(file_path).compress()
