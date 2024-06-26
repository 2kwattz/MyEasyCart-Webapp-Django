from rest_framework import serializers
from .models import Contact
from django.contrib.auth import authenticate

# serializers.py
from .models import User


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class LoginDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type' : 'password'}, write_only=True)

    class Meta:
        model= User
        fields=['email','name','password','password2','tc']
        extra_kwargs={
            'password':{'write_only': True}
        }

    def validate(self,attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError("Password and Confirm Passwords are not the same")
        return attrs
        # return super().validate(attrs)
    
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)
    
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise serializers.ValidationError("Incorrect email or password")
        else:
            raise serializers.ValidationError("Both email and password are required")

        attrs['user'] = user
        return attrs
    

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id','email','name']