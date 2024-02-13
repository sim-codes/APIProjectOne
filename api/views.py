from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .serializer import DataSerializer
from .data import TextData


class IndexApiView(APIView):
    """
    API view for retrieving data based on name and language.

    This view accepts GET requests with 'name' and 'language' parameters.
    It returns a JSON response containing the serialized data.

    If 'name' and 'language' parameters are not provided, it returns an error response with status code 400.
    """

    def get(self, request):
        if 'name' in request.GET and 'language' in request.GET:
            name = request.GET.get('name')
            language = request.GET.get('language')
            data = TextData(name=name, language=language)
            serializer = DataSerializer(data)

            return Response(serializer.data)
        return Response({'error': 'Please provide name and language'}, status=400)