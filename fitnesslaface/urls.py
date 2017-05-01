from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from blog.sitemaps import PostSitemap
# dictionary of sitemaps
sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    # homepage, redirects to post list
    url(r'^$', RedirectView.as_view(
                                    pattern_name='blog:post_list',
                                    permanent=False)),
    # admin panel
    url(r'^admin/', admin.site.urls),
    # blog
    url(r'^blog/', include('blog.urls', namespace='blog')),
    # user account
    url(r'^account/', include('account.urls')),
    # sitemap
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
]

# static media folder
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)
