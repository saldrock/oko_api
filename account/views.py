from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import RegistrationSerializer, User_Data_Serializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User_Data
from django.core.mail import send_mail

class User_DataViewSet(viewsets.ModelViewSet):
	queryset = User_Data.objects.all()
	serializer_class = User_Data_Serializer
	permission_classes = (AllowAny,)


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
			data['first_name'] 		= account.first_name
			data['surname'] 		= account.surname
			data['dwelling_code']	= account.dwelling_code
			data['incentivisation_choice']	= account.incentivisation_choice
			data['goal'] 					= account.goal
			data['phone_number'] 			= account.phone_number
			data['admin_type'] 				= account.admin_type
			data['logged_in'] 				= account.logged_in

		else:
			data = serializer.errors
		return Response(data)

send_mail(
	'Oko Verification Email',
	'Your verification code is XYZ',
	'okodevelopment@gmail.com',
	['nevecurnyn1999@gmail.com'],
	fail_silently=False,
).send()
