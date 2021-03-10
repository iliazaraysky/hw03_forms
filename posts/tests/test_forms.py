from django.test import TestCase
from posts.models import Group, Post


class TestVerboseHelpText(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.group = Group.objects.create(
            title='Лев Толстой',
            slug='tolstoy',
            description='Группа Льва Толстого',
        )

        cls.post = Post.objects.create(
            group=TestVerboseHelpText.group,
            text="Какой то там текст",
        )

    def test_title_label_post(self):
        task = TestVerboseHelpText.post
        verbose = task._meta.get_field('group').verbose_name
        self.assertEqual(verbose, 'Группа')

    def test_title_help_text_post(self):
        task = TestVerboseHelpText.post
        help_texts = task._meta.get_field('group').help_text
        self.assertEqual(help_texts, 'Выберите название группы')

    def test_title_label_group(self):
        task = TestVerboseHelpText.group
        verbose = task._meta.get_field('title').verbose_name
        self.assertEqual(verbose, 'Заголовок группы')

    def test_title_help_text_group(self):
        task = TestVerboseHelpText.group
        help_texts = task._meta.get_field('title').help_text
        self.assertEqual(help_texts, 'Укажите заголовок группы')

    def test_obj_name_title_field_group(self):
        task = TestVerboseHelpText.group
        expected_object_name = task.title
        self.assertEquals(expected_object_name, str(task))
