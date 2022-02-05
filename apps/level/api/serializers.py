from rest_framework import serializers

from apps.level.models import UserGlucoseLevel


class UserGlucoseLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGlucoseLevel
        fields = '__all__'
