from content.content_item import ContentItem


class BlogPost(ContentItem):
    def __init__(self, title, content, author, categories=None, tags=None, **kwargs):
        """
        Initializes a BlogPost with additional blog-specific attributes.
        """
        super().__init__(title, content, **kwargs)
        self.author = author
        self.categories = categories or []
        self.tags = tags or []

    def __repr__(self):
        return f"<BlogPost title='{self.title}' author='{self.author}'>"
