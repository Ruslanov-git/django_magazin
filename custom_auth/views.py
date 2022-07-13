from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from custom_auth.serializers import RegisterSerializer


# class RegisterView(APIView):
#
#     def post(self, request, *args, **kwargs):
#         login = request.data.get('login')
#         # if User.objects.filter(username=login).exists():
#         #     return Response({'login': 'login already used'})
#         password = request.data.get('password')
#         validate_password(password)
#         user = User.objects.create(username=login)
#         user.set_password(password)
#         user.save()
#         token = Token.objects.create(user=user)
#         return Response({'token': str(token.key)})


class RegisterView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)
        return Response({'token': str(token.key)})

