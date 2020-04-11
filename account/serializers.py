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
        fields = ['email', 'username', 'password', 'password2','first_name', 'surname','dwelling_code',
                  'incentivisation_choice','goal','phone_number','admin_type',]
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
        )
        password    = self.validated_data['password']
        password2   = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        account.set_password(password)
        account.save()
        return account
