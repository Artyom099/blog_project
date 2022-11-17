from django.db import models

# объяснение, что хранить в БД. Модели назывем в ед.ч.

class Article(models.Model):
    article_title = models.CharField('Название статьи', max_length=255)
    article_text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('Дата публикации')

class Comment(models.Model):
    # привязываем эту модель к модели статьи, во время удаления статьи, удаляются и комменты
    article = models.ForeingKey(Article, on_delete = models.CASCADE)
    author_name = models.CharField('Имя автора', max_length=50)
    comment_text = models.CharField('Текст комментария', max_length=1000)
