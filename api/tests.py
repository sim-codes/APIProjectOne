import datetime
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from .views import IndexApiView
from .serializer import DataSerializer

class IndexApiViewTestCase(TestCase):
    """
    Test case for the IndexApiView class.
    """

    def test_get(self):
        """
        Test the GET request to the API with parameters.
        """
        factory = APIRequestFactory()
        request = factory.get('http://127.0.0.1:8000/api/?name=michael&language=python')
        response = IndexApiView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_no_params(self):
        """
        Test the GET request to the API without parameters.
        """
        factory = APIRequestFactory()
        request = factory.get('http://127.0.0.1:8000/api/')
        response = IndexApiView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

                              
class DataSerializerTest(TestCase):
    """
    Test case for the DataSerializer class.
    """

    def test_data_serializer(self):
        serializer = DataSerializer(data={
            'name': 'Test Name',
            'current_day': datetime.date.today(),
            'utc_time': datetime.datetime.now(),
            'language': 'Python',
            'github_file_url': 'https://github.com/example/file.py',
            'github_repo_url': 'https://github.com/example/repo',
            'status_code': 200
        })
        self.assertTrue(serializer.is_valid())
