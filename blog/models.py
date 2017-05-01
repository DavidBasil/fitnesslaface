from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse 
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    """Custom manager, can retrieves posts with status 'published'"""
    def get_queryset(self):
        return super(PublishedManager, 
                     self).get_queryset().filter(status='published')


class Tag(models.Model):
    """Tag model"""
    title = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=30, unique=True)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


class Post(models.Model):
    """Blog post model"""
    STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))
    author = models.ForeignKey(User, related_name='blog_posts')
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True)
    slug = models.SlugField(max_length=200, unique_for_date='publish')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, 
                              choices=STATUS_CHOICES,
                              default='draft')
    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    objects = models.Manager()
    published = PublishedManager() # custom manager

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.pk])

    def get_update_url(self):
        return reverse('blog:post_edit', kwargs={'year': self.publish.year,
                                                'month': self.publish.month,
                                                'slug': self.slug})


class Comment(models.Model):
    """Comment model"""
    post = models.ForeignKey(Post, related_name='comments')
    name = models.CharField(max_length=60)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}.'.format(self.name, self.post)


