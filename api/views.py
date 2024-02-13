from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .serializer import DataSerializer
from .data import TextData


class IndexApiView(APIView):
    def get(self, request):
        name = request.GET.get('name') or None
        language = request.GET.get('language') or None
        data = TextData(name=name, language=language)
        serializer = DataSerializer(data)

        return Response(serializer.data)