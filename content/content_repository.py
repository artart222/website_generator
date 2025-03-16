import json
from content.blogpost import BlogPost


class ContentRepository:
    def __init__(self):
        """
        Initializes an empty ContentRepository.
        """
        self.items = {}

    def add(self, item):
        """
        Adds a ContentItem to the repository.
        """
        self.items[item.slug] = item

    def get(self, slug):
        """
        Retrieves a ContentItem by its slug.
        """
        return self.items.get(slug)

    def list_all(self):
        """
        Returns a list of all ContentItems in the repository.
        """
        return list(self.items.values())

    def load(self, file_path="content.json"):
        """
        Loads content from a JSON file into the repository.
        """
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                for item_data in data:
                    post = BlogPost(
                        title=item_data["title"],
                        content=item_data["content"],
                        author=item_data["author"],
                        categories=item_data.get("categories", []),
                        tags=item_data.get("tags", []),
                    )
                    self.add(post)
        except FileNotFoundError:
            print(
                f"Warning: Content file '{file_path}' not found. Starting with an empty repository."
            )

    def __repr__(self):
        return f"<ContentRepository items={len(self.items)}>"
