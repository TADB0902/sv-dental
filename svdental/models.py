from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

# Them bang lien he

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    # name of post
    title = models.CharField(max_length=200, unique=True)
    # address of post
    image = models.ImageField(upload_to='uploads/%Y/%m', default = None, null=False)
    slug = models.SlugField(max_length=200, unique=True)
    # content of post (add ckeditor)
    content = RichTextUploadingField()
    # timpstemp
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    # status
    status = models.IntegerField(choices=STATUS, default=0)
    # soft delete
    active = models.BooleanField(default=True)
    # foreign key to category table
    #
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-created_on']

    def admin_photo(self):
        if(self.image.url):
            return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))

    def link_test(self):
        return mark_safe('<a class="btn btn-primary" href="/post/draft/{}" role="button"  target="_blank">View Draft</a>'.format(self.slug))

    def __str__(self):
        return self.title


class Appointment(models.Model):
    customerName = models.CharField(max_length=200)

    email = models.EmailField(max_length = 254)

    phoneNumber = models.CharField(max_length=200)

    active = models.BooleanField(default=True)

    # timpstemp
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on', 'active']

    def __str__(self):
        return self.customerName




