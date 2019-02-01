__author__ = 'Alison Mukoma <mukomalison@gmail.com, sonlinux>'
__license__ = "MIT"
__email__ = "mukomalison@gmail.com"
__revision__ = '$Format:%H$'

from django.test import TestCase
from ..views.api_client import CataasClient
from rest_framework.test import APIClient

from ..forms.tag_form import TagForm


class TestCataasCient(TestCase):

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()

    def test_tag_form(self):
        form = TagForm(data={'tag': "brown"})
        self.assertTrue(form.is_valid())
