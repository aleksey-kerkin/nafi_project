from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "lastname",
            "name",
            "middlename",
            "business_area",
            "email",
            "password",
            "phone",
            "organization",
            "entity",
        )

    def validate(self, data):
        user = User(**data)
        password = data.get("password")

        try:
            validate_password(password, user)
        except exceptions.ValidationError as e:
            serializer_errors = serializers.as_serializer_error(e)
            raise exceptions.ValidationError(
                {"password": serializer_errors["non_field_errors"]}
            )

        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            lastname=validated_data["lastname"],
            name=validated_data["name"],
            middlename=validated_data["middlename"],
            business_area=validated_data["business_area"],
            email=validated_data["email"],
            password=validated_data["password"],
            phone=validated_data["phone"],
            organization=validated_data["organization"],
            entity=validated_data["entity"],
        )

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "lastname",
            "name",
            "middlename",
            "business_area",
            "email",
            "phone",
            "organization",
            "entity",
        )
