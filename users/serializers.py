from rest_framework import serializers
from users.models import User


class UserPasswordSetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

