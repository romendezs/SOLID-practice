from pathlib import Path
from zipfile import ZipFile


class FileManager:
    def __init__(self, file_path: str):
        self.path = Path(file_path)

    def read(self) -> str:
        return self.path.read_text('utf-8')

    def write(self, content: str):
        self.path.write_text(content, 'utf-8')

    def compress(self):
        with ZipFile(self.path.with_suffix('.zip'), mode='w') as file:
            file.write(self.path)

    def add_greeting(self, content: str) -> str:
        return content + '\nHello world!'


if __name__ == '__main__':
    file_path = 'data.txt'
    file_manager = FileManager(file_path)
    content = file_manager.add_greeting(file_manager.read())
    file_manager.write(content)
    file_manager.compress()