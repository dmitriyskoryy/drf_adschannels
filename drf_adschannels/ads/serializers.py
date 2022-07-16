from rest_framework import serializers

from .models import Adt

class AdsListSerializer(serializers.ModelSerializer):
    """Списоа статей"""

    class Meta:
        model = Adt
        fields = ("title", "text",)