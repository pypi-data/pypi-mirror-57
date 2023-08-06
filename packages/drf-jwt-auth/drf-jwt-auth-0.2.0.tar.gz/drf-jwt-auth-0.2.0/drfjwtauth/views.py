from jwt import PyJWTError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from drfjwtauth.auth import JWTAuth


class VerifyJWTView(APIView):

    def post(self, request):
        token = request.data.get('token')
        try:
            JWTAuth.decode_token(token)
        except PyJWTError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'ok'})
