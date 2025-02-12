from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.validators import UniqueValidator

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "emailid", "password", "password2", "address", "phone"]

    def validate(self, attrs):
        """Ensure both passwords match."""
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        """Manually create a user with a hashed password."""
        validated_data.pop("password2")  # Remove confirmation password
        validated_data["password"] = make_password(validated_data["password"])  # Hash password
        user = User.objects.create(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        """Manually authenticate user (since no built-in auth is used)."""
        try:
            user = User.objects.get(username=data["username"])
        except User.DoesNotExist:
            raise serializers.ValidationError({"message": "Invalid credentials"})

        if not check_password(data["password"], user.password):
            raise serializers.ValidationError({"message": "Invalid credentials"})

        return {"user_id": user.id, "username": user.username}
