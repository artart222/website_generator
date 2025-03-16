from config.config_manager import ConfigManager
from engine.dynamic_site_engine import DynamicSiteEngine
from content.blogpost import BlogPost
from content.content_repository import ContentRepository
from services.template_engine import TemplateEngine
from services.router import Router
from services.storage_manager import FileSystemStorageAdapter


def main():
    config = ConfigManager()

    content_repo = ContentRepository()
    template_engine = TemplateEngine(template_dir=config.get("template_dir"))
    router = Router(base_url=config.get("base_url"))
    storage = FileSystemStorageAdapter(output_dir=config.get("output_dir"))

    post1 = BlogPost(
        title="My First Blog Post",
        content="This is the content of my first blog post.",
        author="John Doe",
        categories=["Python", "Web Development"],
        tags=["blog", "tutorial"],
    )
    post2 = BlogPost(
        title="Another Blog Post",
        content="This is another blog post.",
        author="Jane Smith",
        categories=["JavaScript", "Web Development"],
        tags=["blog", "coding"],
    )

    content_repo.add(post1)
    content_repo.add(post2)

    site_engine = DynamicSiteEngine(
        config=config,
        content_repo=content_repo,
        template_engine=template_engine,
        router=router,
        storage_manager=storage,
    )

    site_engine.initialize()
    site_engine.generate_site()

    print("Site generation complete!")


if __name__ == "__main__":
    main()
