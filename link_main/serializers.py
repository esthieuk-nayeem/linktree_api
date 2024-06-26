from rest_framework import serializers
from authentication.models import User
from  .models import *


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkModel
        fields = '__all__'