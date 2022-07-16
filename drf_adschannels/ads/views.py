from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Adt
from .serializers import AdsListSerializer

class AdsListView(APIView):
    """Вывод списка статей"""
    def get(self, request):
        ads = Adt.objects.all()
        serializer = AdsListSerializer(ads, many=True)
        return Response(serializer.data)
