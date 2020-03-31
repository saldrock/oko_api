from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token


@api_view(['POST', ])
def registration_view(request):

	if request.method == 'POST':
		serializer = RegistrationSerializer(data=request.data)
		data = {}
		if serializer.is_valid():
			account = serializer.save()
			data['response'] 		= 'successfully registered new user.'
			data['email'] 			= account.email
			data['username'] 		= account.username
			token 					= Token.objects.get(user=account).key
			data['token'] 			= token
			# data['goal'] 			= account.goal
			# data['is_house_admin'] 	= account.is_house_admin
			# data['is_house_super'] 	= account.is_house_super
			# data['phone_number'] 	= account.phone_number
			# data['house_code']		= account.house_code

		else:
			data = serializer.errors
		return Response(data)