from rest_framework import serializers
from .models import Swap

class SwapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Swap
        fields = ['id', 'requester', 'requested_skill', 'offered_skill', 'is_accepted']