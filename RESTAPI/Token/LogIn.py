
import jwt
import json
from django.conf import settings

settings.configure(DEBUG=True)
from rest_framework import views
from django.http import HttpResponse
from rest_framework.response import Response

from django.contrib.auth import get_user_model







class Login(views.APIView):

    def post(self, request):

        if not request.data:
            return Response({'Error': "Please provide username/password"}, status="400")

        username = request.data['username']
        password = request.data['password']
        User = get_user_model()
        try:
            user = User.objects.get(username=username, password=password)
        except User.DoesNotExist:
            return Response({'Error': "Invalid username/password"}, status="400")
        if user:

            payload = {
                'id': user.id,
                'email': user.email,
            }
            jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}

            return HttpResponse(
              json.dumps(jwt_token),
              status=200,
              content_type="application/json"
            )

        else:
            return Response(
              json.dumps({'Error': "Invalid credentials"}),
              status=400,
              content_type="application/json"
            )