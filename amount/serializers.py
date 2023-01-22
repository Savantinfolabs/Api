from rest_framework import serializers
from .models import Amount

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Amount
        extra_kwargs={'password': {'read_only':True}}
        fields=('username','email','password','phone','gender')
