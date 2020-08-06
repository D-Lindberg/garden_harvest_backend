from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    email = serializers.EmailField(required=True)
    zip_code = serializers.CharField(min_length=5, max_length=5)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'zip_code',
                  'state', 'first', 'lon', 'formatted_address')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.save()
            return instance
