from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class BlogApp(CMSApp):
    app_name = 'blog_app'
    name = 'Blog'

    def get_urls(self, page=None, language=None, **kwargs):
        return ['blogapp.urls']

apphook_pool.register(BlogApp)
