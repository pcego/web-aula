from django.test import TestCase
from workshop.subscriptions.forms import SubscriptionForm

class SubscriptionTest(TestCase):

    def setUp(self):
        self.response = self.client.get('/subscription/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)


    def test_template_used(self):
        self.assertTemplateUsed(self.response,
                                'subscriptions/subscription_form.html')

    def test_html_form(self):
        """
        Verifica a estrutura do formulário HTML (tags)

        """
        tags = (('form',10),
                ('<input', 6),
                ('type="text', 11),
                ('type="email',1),
                ('type="submit"',1))

        for text, count in tags:
            with self.subTest():
                self.assertContains(self.response, text, count)


    def test_csrf_token(self):
        """
        Verifica se o HTML form possui o csrf_token
        """
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """
        Verifica se existe um variável de contexto para o form

        """
        form = self.response.context['form']
        self.assertIsInstance(form, SubscriptionForm)


    def test_form_has_field(self):

        form = self.response.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))



