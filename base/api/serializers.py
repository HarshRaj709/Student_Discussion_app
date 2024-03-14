from rest_framework.serializers import ModelSerializer
from base.models import Room


class RoomSerializer(ModelSerializer):          #same same Forms.py // ModelForm
    class Meta:
        model = Room
        fields = '__all__'
