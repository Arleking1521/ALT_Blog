from django.db import models
from django.utils import timezone
from logReg.models import CustomUser
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(CustomUser, verbose_name='Автор', on_delete=models.CASCADE)
    title = models.CharField(verbose_name = 'Заголовок поста', max_length=50)
    content = models.TextField(verbose_name = 'Информация')
    date = models.DateTimeField(verbose_name = 'Дата публикации', default = timezone.now)

    def __str__(self) -> str:
        return f'{self.author}: {self.title}'
    
class Post_Attachments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.FileField(upload_to='post_atts/')
    type = models.CharField(max_length=6, blank=True, null=True)

    def save(self, *args, **kwargs):
        file_ex = self.image.name.split('.')[-1].lower()
        if file_ex in ['jpeg', 'jpg', 'png', 'tfif', 'gif']:
            self.type = 'img'
        else:
            self.type = 'doc'
        super().save(*args, **kwargs)