from rest_framework import serializers,viewsets

from hotels.models import Hotel



class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id','likes')


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
