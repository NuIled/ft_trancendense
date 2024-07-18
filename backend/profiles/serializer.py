from rest_framework import serializers 
from .models import User_profile
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

class User_Register(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68,min_length=6,write_only=True)
    password1 = serializers.CharField(max_length=68,min_length=6,write_only=True)

    class Meta:
        model = User_profile
        fields = ['email','first_name','last_name' ,'password','password1']

    def valideate(self,attrs):
        password = attrs.get('password','')
        password1 = attrs.get('password1','')
        if password != password1:
            raise serializers.ValidationError('password dose not match')
        return attrs

    def create(self,validated_data):
        try:
            validated_data.pop('password1')
            print(validated_data)
            user = User_profile.objects.create_user(**validated_data)
            print(user)
        except Exception as e:
            print(e , ' ssss')

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_profile
        fields = ['id','email','password','first_name','last_name','avatar','bio']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class LoginUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=255,write_only=True)
    access = serializers.CharField(max_length=255,read_only=True)
    refresh = serializers.CharField(max_length=255,read_only=True)
    class Meta:
        model = User_profile
        fields = ['email','password','first_name','access','refresh']

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        try:
            user = User_profile.objects.get(email=email) #check password
        except:
            raise AuthenticationFailed("invalid credentials try again")
        if not user.is_active:
            raise AuthenticationFailed('User not Found or password incorrect')
        if not user.check_password(raw_password=password):
            raise AuthenticationFailed('User not Found or password incorrect')
        token = user.token()
        return {
            'email': user.email,
            'first_name':user.first_name,
            'access': str(token.access_token),
            'refresh': str(token),
        }



class ResetPassword(serializers.ModelSerializer):
    pass
             