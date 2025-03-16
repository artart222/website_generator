from pathlib import Path


class FileSystemStorageAdapter:
    def __init__(self, output_dir="output"):
        """
        Initializes the FileSystemStorageAdapter with an output directory.
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(
            exist_ok=True
        )  # Create the output directory if it doesn't exist

    def save(self, file_path, content):
        """
        Saves content to a file in the output directory.
        """
        full_path = self.output_dir / file_path
        full_path.parent.mkdir(
            parents=True, exist_ok=True
        )  # Create parent directories if needed
        with open(full_path, "w") as file:
            file.write(content)

    def read(self, file_path):
        """
        Reads content from a file in the output directory.
        """
        full_path = self.output_dir / file_path
        with open(full_path, "r") as file:
            return file.read()

    def __repr__(self):
        return f"<FileSystemStorageAdapter output_dir='{self.output_dir}'>"
