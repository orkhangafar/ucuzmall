from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from random import randint


#Category
class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True,editable=False)

    def __str__(self):
        return self.title
    def postCount(self):
        return self.posts.all().count()
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Category,self).save(*args,**kwargs)


#Post Model
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1,related_name="userposts")
    price = models.FloatField()
    phone = models.CharField(max_length=12, blank=True)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='uploads', blank=True)
    content = models.TextField()
    slug = models.SlugField(editable=False)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts", default=True)
    #tag = models.ManyToManyField(Tag,related_name='posts')

    def __str__(self):
        return self.title+ " => " +str(self.created)

    def save(self, *args, **kwargs):
        if Post.objects.filter(title=self.title).exists():
            extra = str(randint(1, 10000))
            self.slug = slugify(self.title) + "-" + extra
        else:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)