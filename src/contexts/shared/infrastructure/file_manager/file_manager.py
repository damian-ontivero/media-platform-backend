import os


class FileManager:
    """
    File manager class to save and retrieve files from the file system.
    """

    def __init__(self, base_dir: str) -> None:
        self._base_dir = base_dir

    def save_file(self, dir: str, filename: str, content: bytes) -> str:
        file_path = os.path.join(self._base_dir, dir, filename)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path, "wb") as f:
            f.write(content)

        return file_path

    def retrieve_file(self, path: str) -> bytes:
        file_path = os.path.join(path)

        try:
            with open(file_path, "rb") as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {file_path}")
