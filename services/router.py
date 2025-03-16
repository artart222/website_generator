class Router:
    def __init__(self, base_url=""):
        """
        Initializes the Router with a base URL.
        """
        self.base_url = base_url

    def resolve(self, slug):
        """
        Resolves a file path for a given slug.
        """
        return f"{slug}.html"  # Only use the slug for file paths

    def generate_url(self, slug):
        """
        Generates a full URL for a given slug.
        """
        return f"{self.base_url}/{slug}"  # Use base_url for URLs
