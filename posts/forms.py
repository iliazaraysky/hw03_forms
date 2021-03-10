from django.forms import ModelForm
from .models import Post


class NewPost(ModelForm):
    """
     Если необходимо сделать переопределение verbose_name и help_texts
     непосредственно из формы. После fields указываем
            labels = {
                'group': _('Группа'),
                'text': _('Сообщение'),
            }
            help_texts = {
                'text': _('Обязательное поле, не должно быть пустым')
            }
     """
    class Meta:
        model = Post
        fields = ('group', 'text')
