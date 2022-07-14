from django.db import models

from django.db import models
from django.contrib.auth.models import User

from .utils import translate_str
from django.utils.text import slugify

class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.authorUser.username}'


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.name}'


class Adt(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Author')
    adtCategory = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категории')
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Date')
    title = models.CharField(max_length=128, verbose_name='Заголовок объявления')
    slug = models.SlugField(max_length=255, verbose_name='URL')
    text = models.TextField(verbose_name='Описание', default=None)

    #добав ссылку на текущий объект. Для того, чтобы при создании объекта или переходе
    #к его деталям не прописывать в каждом дженерике succes_url.
    def get_absolute_url(self):
        return f'/ads/{self.id}'

    def save(self, *args, **kwargs):
        s = translate_str(self.title)
        self.slug = slugify(s)
        super(Adt, self).save(*args, **kwargs)


class Respond(models.Model):
    responseAdt = models.ForeignKey(Adt, on_delete=models.CASCADE, verbose_name='Adt')
    responseUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    #получил отклик принятие или нет
    acceptResponse = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.responseUser}'


class OneTimeCode(models.Model):
    codeUser = models.OneToOneField(User, on_delete=models.CASCADE)
    oneTimeCode = models.CharField(max_length=128)