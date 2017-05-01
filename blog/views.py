from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, UpdateView
from django.core.mail import send_mail
from django.db.models import Count # performs aggregated counts
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .models import Post, Comment, Tag
from .forms import SharePostForm, CommentForm, PostForm


def post_list(request, tag_slug=None):
    """Displays the list of all published posts"""
    object_list = Post.published.all() # custom manager
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1) # displays the first page
    except EmptyPage:
        posts = paginator.page(paginator.num_pages) # displays the last page
    return render(request, 'blog/post/list.html', {'posts': posts,
                                                    'page': page,
                                                    'tag': tag})


def post_detail(request, pk):
    """Displays a detailed view of a particular post"""
    post = get_object_or_404(Post, pk=pk)
    # comments
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else: 
        comment_form = CommentForm()
    # list of tags id's of the current post
    post_tags_ids = post.tags.values_list('id', flat=True)
    # get all posts with all those tags excluding the current one
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(
                                                                id=post.id)
    # same_tags = number of tags shared with all tags queried
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by(
                                                    '-same_tags', '-publish')
    return render(request, 'blog/post/detail.html', {'post': post,
                                            'comments': comments,
                                            'comment_form': comment_form,
                                            'similar_posts': similar_posts})


@login_required
def post_create(request):
    """Creates new blog post"""
    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.status = 'published'
            post.save()
            return redirect(post.get_absolute_url())
    else:
        form = PostForm()
    return render(request, 'blog/post/create.html', {'form': form})


def post_share(request, post_id):
    """Handles post sharing"""
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        form = SharePostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(
                                                            cd['name'],
                                                            cd['email'],
                                                            post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(
                                                            post.title,
                                                            post_url,
                                                            cd['name'],
                                                            cd['comments'])
            send_mail(subject, message, 'admin@fitnesslaface.com', [cd['to']])
            sent = True
    else: 
        form = SharePostForm()
    return render(request, 'blog/post/share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})


@login_required
def post_edit(request, pk):
    """Updates an existing blog post"""
    post = get_object_or_404(Post, pk=pk, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.status = 'published'
            post.save()
            return redirect(post.get_absolute_url())
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post/edit.html', {'form': form})






