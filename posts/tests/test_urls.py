from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from posts.models import Group, Post

User = get_user_model()


class StaticURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.group = Group.objects.create(
            title='Лев Толстой',
            slug='tolstoy',
            description='Группа Льва Толстого',
        )

        cls.post = Post.objects.create(
            group=StaticURLTests.group,
            text="Какой то там текст",
        )

    def setUp(self):
        self.guest_client = Client()
        self.user = User.objects.create_user(username='TestForTest')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_urls_list(self):
        """
        Тестирование по списку, для анонимного пользователя,
        список URL, где ответ должен быть равен 200
        """

        url_list = ['/', '/group/tolstoy']
        for test_url in url_list:
            response = self.guest_client.get(test_url)
            self.assertEqual(response.status_code, 200)

    def test_new_page_not_login_user(self):
        """Страница доступна авторизированному пользователю"""

        response = self.guest_client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_group_slug_response_not_login_user(self):
        """Проверка доступности созданной группы для всех пользователей"""

        response = self.guest_client.get('/group/tolstoy')
        self.assertEqual(response.status_code, 200)

    def test_new_page_not_login_user(self):
        """
        Страница создания нового поста,
        перенаправляет анонимного пользователя
        """

        response = self.guest_client.get('/new')
        self.assertEqual(response.status_code, 302)

    def test_new_page_login_user(self):
        """Главная страница доступна авторизированному пользователю"""

        response = self.authorized_client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_group_slug_response_login_user(self):
        """
        Проверка доступности созданной группы
        для авторизированных пользователей
        """

        response = self.authorized_client.get('/group/tolstoy')
        self.assertEqual(response.status_code, 200)

    def test_new_page_login_user(self):
        """Страница доступна авторизированному пользователю"""

        response = self.authorized_client.get('/new')
        self.assertEqual(response.status_code, 200)

    def test_new_page_not_login_user_redirect(self):
        """Страница перенаправляет анонимного пользователя"""

        response = self.guest_client.get('/new', follow=True)
        self.assertRedirects(response, '/auth/login/?next=/new')

    def test_urls_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон"""

        template_url_names = {
            'index.html': '/',
            'group.html': '/group/tolstoy',
            'newpost.html': '/new',
        }
        for template, reverse_name in template_url_names.items():
            with self.subTest():
                response = self.authorized_client.get(reverse_name)
                self.assertTemplateUsed(response, template)
