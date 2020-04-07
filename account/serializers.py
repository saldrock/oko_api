from rest_framework import serializers

from account.models import Account, User_Data


# class LoginSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Account
# 		fields = ['email', 'password',]

# 		extra_kwargs = {'password': {'write_only': True}}

# 	def validate(self, data):
# 		password = data.get('password')
# 		email = data.get('email')
class User_Data_Serializer():
    class Meta:
        model = User_Data
        fields = fields = ('id', 'energyused_ytd', 'energyused_mtd','energyused_day')

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password2', 'dwelling_code',
                  'incentivisation_choice','goal','phone_number','admin_type']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        account = Account(
            email           =self.validated_data['email'],
            username        =self.validated_data['username'],
            incentivisation_choice   = self.valided_date['incentivisation_choice'],
            goal=self.valided_date['goal'],
            phone_number=self.valided_date['phone_number'],
            admin_type=self.valided_date['admin_type'],


        )
        password    = self.validated_data['password']
        password2   = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account
