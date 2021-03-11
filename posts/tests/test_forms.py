from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from posts.forms import NewPost
from posts.models import Group, Post

User = get_user_model()


class TestCreateForm(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.group = Group.objects.create(
            title='Лев Толстой',
            slug='tolstoy',
            description='Группа Льва Толстого',
        )

        cls.post = Post.objects.create(
            group=TestCreateForm.group,
            text="Какой-то там текст",
        )

    def setUp(self):
        self.guest_client = Client()
        self.user = User.objects.create_user(username='TestForTest')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_form_create(self):
        post_count = Post.objects.count()
        form_data = {
            # 'group': 'Лев Толстой',
            'text': 'Отправить текст',
        }
        response = self.authorized_client.post(reverse('new_post'),
                                               data=form_data,
                                               follow=True)

        self.assertRedirects(response, reverse('index'))
        self.assertEqual(Post.objects.count(), post_count + 1)
        # self.assertTrue(Post.objects.filter(
        #    text='Отправить текст',
        #    group=TestCreateForm.group.title).exists())
