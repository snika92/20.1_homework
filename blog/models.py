from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Содержимое', **NULLABLE)
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    preview = models.ImageField(upload_to='blog/', verbose_name='Изображение', **NULLABLE)
    date_of_creation = models.DateField(auto_now_add=True, verbose_name='Дата создания', **NULLABLE)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
