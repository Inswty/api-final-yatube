from django.db import models
from django.contrib.auth import get_user_model

MAX_STR_LENGTH = 20

User = get_user_model()


class Group(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    slug = models.SlugField('Идентификатор', unique=True)
    description = models.TextField('Описание')

    class Meta():
        verbose_name = 'сообщество'
        verbose_name_plural = 'сообщества'

    def __str__(self):
        return self.title[:MAX_STR_LENGTH]


class Post(models.Model):
    text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts',
        verbose_name='Автор публикации')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True, verbose_name='Изображение')
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True, verbose_name='сообщество'
    )

    class Meta():
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'
        ordering = ['-pub_date']

    def __str__(self):
        return self.text[:MAX_STR_LENGTH]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments',
        verbose_name='Автор комментария')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments',
        verbose_name='Публикация')
    text = models.TextField('Текст комментария')
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta():
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    def __str__(self):
        return self.text[:MAX_STR_LENGTH]


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follows',
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='followers',
        verbose_name='Подписка'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('user', 'following',),
                                    name='unique_follow'),
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_prevent_self_follow",
                check=~models.Q(user=models.F('following')),
            ),
        ]
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'

    def __str__(self):
        return self.following[:MAX_STR_LENGTH]
