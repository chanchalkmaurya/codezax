from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts, Author, SocialMediaHandles


codezax_handles = {
    'youtube': 'https://www.youtube.com/@CodeZax',
    'linkedin': 'https://www.linkedin.com/company/codezax/',
    'twitter': ''
}
# Create your views here.

def index(request):
    featured_post = Posts.objects.order_by("-id")
    all_stories = Posts.objects.all()

    # find all the blogs which is written by the author (author_id)
    author = Author.objects.all()


    param = {'featured_post':featured_post, 'all_stories':all_stories, 'codezax_handles':codezax_handles, 'authors':author}
    return render(request, 'blog/index.html', param)   


def author(request, author_id):
    # find the author details by using author_id
    author=None
    try:
        author = Author.objects.get(user_id=author_id)
    except Exception as e:
        print(e)

    # find all the blogs which is written by the author (author_id)
    author_post = None
    try:
        author_post = Posts.objects.filter(author_name=author_id)
    except Exception as e:
        print(e)

    # find all the socialMediaHandles there
    socials = None
    try:
        socials = SocialMediaHandles.objects.get(author=author_id)
    except Exception as e:
        print(e)

    param = {
        'author': author,
        'author_post':author_post,
        'socials':socials,
        'codezax_handles':codezax_handles
    }
    return render(request, 'blog/author.html', param)  


def author_list(request):
    author_list = Author.objects.all()
    social_handles= SocialMediaHandles.objects.all()
    return render(request, 'blog/author_list.html', {'authors': author_list, 'socials':social_handles, 'codezax_handles':codezax_handles})


def contact(request):
    return HttpResponse("contact.html", {'codezax_handles':codezax_handles})    



def post(request, blog_id):
    post_data = None
    try:
        post_data = Posts.objects.get(blog_id=blog_id)
    except Exception as e:
        print(e)

    # find author of this post
    author_id = post_data.author_name
    print(author_id)

    # Fetch all posts of this author excluding the current posts
    all_post_of_author = None
    try:
        all_post_of_author = Posts.objects.filter(author_name_id=author_id).exclude(blog_id=blog_id ).order_by("-blog_id")
    except Exception as e:
            print(e)

    social_media_handles = None
    try:  
        social_media_handles = SocialMediaHandles.objects.get(author_id=author_id)
    except Exception as e:
        print(e)

    author = ""
    try:
        author = Author.objects.get(user_id=author_id)
    except Exception as e:
        print(e)
    
    param = {
        'post':post_data,
        'social_handles':social_media_handles,
        'author':author,
        'codezax_handles':codezax_handles,
        'all_post_of_author':all_post_of_author
        }
    return render(request, 'blog/post.html', param)      