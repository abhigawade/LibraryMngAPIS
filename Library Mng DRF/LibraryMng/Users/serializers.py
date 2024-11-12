from Users.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'phone', 'full_name', 'is_librarian')
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            full_name=validated_data['full_name'],
            is_librarian=validated_data['is_librarian']
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user