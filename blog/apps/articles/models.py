from django.db import models
import datetime
from django.utils import timezone

# объяснение, что хранить в БД. Модели назывем в ед.ч.
# после добавления моделей, надо сделать миграции

class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length=255)
    article_text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.article_title

    def pub_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

class Comment(models.Model):
    # привязываем эту модель к модели статьи, во время удаления статьи, удаляются и комменты
    article = models.ForeignKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField('Имя автора', max_length=50)
    comment_text = models.CharField('Текст комментария', max_length=1000)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментрий'
        verbose_name_plural = 'Комментрии'
