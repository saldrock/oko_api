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
class User_Data_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Data
        fields = ('id', 'energyused_ytd', 'energyused_mtd','energyused_day')

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'username', 'password', 'password2','first_name', 'surname','dwelling_code',
                  'incentivisation_choice','goal','phone_number','admin_type','logged_in']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        account = Account(
            email                   =self.validated_data['email'],
            username                =self.validated_data['username'],
            dwelling_code           =self.validated_data['dwelling_code'],
            first_name              =self.validated_data['first_name'],
            surname                 =self.validated_data['surname'],
            incentivisation_choice  =self.validated_data['incentivisation_choice'],
            goal                    =self.validated_data['goal'],
            phone_number            =self.validated_data['phone_number'],
            admin_type              =self.validated_data['admin_type'],
            logged_in               =self.validated_data['logged_in'],
        )
        password    = self.validated_data['password']
        password2   = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account


class Account_Serializer(serializers.BaseSerializer):
    class Meta:
        model = Account
        fields = '__all__'
    def save(self):
        account = Account(
            email                   =Account.email,
            username                =Account.username,
            #dwelling_code           ='dwelling_code',
            #first_name              ='first_name',
            #surname                 ='surname',
            #incentivisation_choice  ='incentivisation_choice',
            # goal                    ='goal',
            #phone_number            ='phone_number',
            #admin_type              ='admin_type',
          # logged_in               ='logged_in',
        )
        account.save()
        return account