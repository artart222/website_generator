from jinja2 import Environment, FileSystemLoader, TemplateNotFound


class TemplateEngine:
    def __init__(self, template_dir="templates"):
        """
        Initializes the TemplateEngine with a template directory.
        """
        self.template_dir = template_dir
        self.env = Environment(loader=FileSystemLoader(template_dir))

    def render(self, template_name, context=None):
        """
        Renders a template with the given context.

        Args:
            template_name (str): The name of the template file (e.g., "post.html").
            context (dict): A dictionary of context variables to pass to the template.

        Returns:
            str: The rendered HTML content.

        Raises:
            TemplateNotFound: If the template file does not exist.
        """
        if context is None:
            context = {}

        try:
            template = self.env.get_template(template_name)
            return template.render(context)
        except TemplateNotFound:
            raise TemplateNotFound(
                f"Template '{template_name}' not found in '{self.template_dir}'."
            )

    def render_index(self, posts):
        """
        Renders the index page with a list of blog posts.

        Args:
            posts (list): A list of blog posts to display on the index page.

        Returns:
            str: The rendered HTML content for the index page.
        """
        return self.render("index.html", {"posts": posts})
