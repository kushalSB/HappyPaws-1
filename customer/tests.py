<<<<<<< HEAD
from django.test import TestCase

# Create your tests here.
=======

from django.test import SimpleTestCase, TestCase

from django.urls import reverse,resolve

# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_case_index_url(self):
        url=reverse('imdex')
        self.assertEquals(resolve(url).func.index)

>>>>>>> frontend
