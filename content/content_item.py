from datetime import datetime


class ContentItem:
    def __init__(self, title, content, slug=None, created_at=None, updated_at=None):
        """
        Initializes a ContentItem with basic attributes.
        """
        self.title = title
        self.content = content
        self.slug = slug or self.generate_slug(title)
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def generate_slug(self, title):
        """
        Generates a URL-friendly slug from the title.
        """
        return title.lower().replace(" ", "-")

    def __repr__(self):
        return f"<ContentItem title='{self.title}' slug='{self.slug}'>"
