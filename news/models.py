from django.db import models
from django.utils import timezone #setting ko last maa timezone change garna milchha
from django.contrib.auth.admin import User
from ckeditor.fields import RichTextField

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    cat_name=models.CharField(max_length=100,unique=True)
    status=models.BooleanField(default=0)


    def __str__(self):
        return self.cat_name
    class Meta:
        verbose_name_plural='Category'
class Gallery(models.Model):
    title=models.CharField(max_length=200,unique=True)
    image=models.ImageField()

    def __str__(self):
        return self.title


class Product(models.Model):
    posted_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    image = models.ImageField(blank=True,upload_to='product')
    status=models.BooleanField(default=0) # o ko satta 1 rakhda active hunchha
    description = RichTextField()    # description = models.TextField()
    class Meta:
        verbose_name_plural='Product'

class Slider(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(blank=True, upload_to='slider')
    status = models.BooleanField(default=0)  # o ko satta 1 rakhda active hunchha
    description = RichTextField()  # description = models.TextField()

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='Slider'


class Photographpf(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(blank=True, upload_to='Photographpf')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural='Photographpf'


class Cosmo(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Cosmology(models.Model):
    posted_date = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    image = models.ImageField(blank=True,upload_to='product')
    status=models.BooleanField(default=0) # o ko satta 1 rakhda active hunchha
    description = RichTextField()    # description = models.TextField()
    class Meta:
        verbose_name_plural='Cosmology'


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Category, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateTimeField(max_length=200, unique=True)
    mod_date = models.DateTimeField(max_length=200, unique=True)
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline




class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )





# class Blog(models.Model):
#     name = models.CharField(max_length=100)
#     tagline = models.TextField()
#
#     def __str__(self):
#         return self.name
#
#
#
# class Author(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()
#
#     def __str__(self):
#         return self.name
#
# class Entry(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     headline = models.CharField(max_length=255)
#     body_text = models.TextField()
#     pub_date = models.DateTimeField(max_length=200, unique=True)
#     mod_date = models.DateTimeField(max_length=200, unique=True)
#     authors = models.ManyToManyField(Author)
#     number_of_comments = models.IntegerField()
#     number_of_pingbacks = models.IntegerField()
#     rating = models.IntegerField()
#
#     def __str__(self):
#         return self.headline



