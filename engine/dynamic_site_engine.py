class DynamicSiteEngine:
    def __init__(self, config, content_repo, template_engine, storage_manager, router):
        """
        Initializes the DynamicSiteEngine with essential components.
        """
        self.config = config  # Manages site-wide settings
        self.content_repo = content_repo  # Manages content items
        self.template_engine = template_engine  # Renders HTML from templates
        self.storage_manager = storage_manager  # Handles file I/O
        self.router = router  # Maps URLs to content/templates

    def initialize(self):
        """
        Initializes the engine and its components.
        """
        self.config.load()  # Load configuration
        self.content_repo.load()  # Load content
        self.template_engine.setup()  # Set up templates

    def generate_site(self):
        """
        Generates the static website.
        """
        # Render all content items
        for content_item in self.content_repo.list_all():
            html = self.template_engine.render(content_item)
            output_path = self.router.resolve(content_item.slug)
            self.storage_manager.save(output_path, html)

        # Generate index page
        index_html = self.template_engine.render_index(self.content_repo.list_all())
        self.storage_manager.save("index.html", index_html)

    def deploy(self):
        """
        Deploys the generated site to the output directory.
        """
        self.storage_manager.deploy()
