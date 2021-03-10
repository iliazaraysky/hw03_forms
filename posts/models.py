from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок группы',
                             help_text='Укажите заголовок группы')
    slug = models.SlugField(max_length=160, unique=True,
                            verbose_name="Slug (идентификатор)",
                            help_text="Slug это уникальная строка,\
                             понятная человеку")
    description = models.TextField(verbose_name='Описание',
                                   help_text='У группы должно быть описание')

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name='Текст сообщения',
                            help_text='Обязательное поле,\
                             не должно быть пустым')
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,
                               null=True, related_name="posts",
                               verbose_name="Автор",
                               help_text="Выберите имя автора")
    group = models.ForeignKey(Group, on_delete=models.DO_NOTHING, blank=True,
                              null=True, related_name="posts",
                              verbose_name="Группа",
                              help_text="Выберите название группы")

    class Meta:
        ordering = ("-pub_date",)

    def __str__(self):
        return self.text[:15]
