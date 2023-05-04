from django.db import models

# Create your models here.
class Posts(models.Model):
    blog_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author_name = models.ForeignKey('Author', on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now=True)
    featured_image = models.ImageField(upload_to='Images/', height_field=None, width_field=None)
    medium_url = models.URLField()


    def __str__(self):
        return self.title


class Author(models.Model):
    user_id = models.AutoField(primary_key=True ,unique=True)
    name = models.CharField(max_length=200)
    bio = models.TextField()
    author_image = models.ImageField(upload_to='Images/author/',height_field=None, width_field=None, null=True, default="default_author.jpg")
    email = models.EmailField(max_length=60, unique=True)
    isdCode = models.CharField(max_length=5)
    mobile = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name
    


class SocialMediaHandles(models.Model):
    instagram = models.CharField(max_length=100, null=True)
    twitter = models.CharField(max_length=100, null=True)
    linkedin = models.CharField(max_length=100, null=True)
    github = models.CharField(max_length=100, null=True)
    medium = models.CharField(max_length=100, null=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)


    def __str__(self):
        return "Social Media Handles for author: " + str(author) 

