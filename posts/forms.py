from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import Post


class NewPost(ModelForm):
    class Meta:
        model = Post
        fields = ('group', 'text')
        labels = {
            'group': _('Группа'),
            'text': _('Сообщение'),
        }
        help_texts = {
            'text': _('Обязательное поле, не должно быть пустым')
        }
