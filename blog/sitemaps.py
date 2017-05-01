from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    """Sitemap for blog posts"""
    changefreq = 'weekly' # frequency of post pages
    priority = 0.9 # relevance of post pages to website

    def items(self):
        return Post.published.all() # objects to include in sitemap

    def lastmod(self, obj):
        return obj.publish # returns the last time object was modified
