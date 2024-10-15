from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class post(models.Model):
    author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    title = models.CharField(verbose_name = 'Заголовок поста', max_length=50)
    content = models.TextField(verbose_name = 'Информация')
    date = models.DateTimeField(verbose_name = 'Дата публикации', default = timezone.now)

    def __str__(self) -> str:
        return f'{self.author}: {self.title}'
    