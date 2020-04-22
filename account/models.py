from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token



class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email adress")
        if not username:
            raise ValueError("Users must have an email adress")

        user = self.model(
                email=self.normalize_email(email),
                username=username,
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
                email=self.normalize_email(email),
                password=password,
                username=username,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# secure version of the accounts system
class Account(AbstractBaseUser):
    GOAL_CHOICES = [
        ('SM','Save Money'),
        ('HE', 'Help Environment')

    ]
    ACCOUNT_CHOICES =  [
        ('SA','super_admin'),
        ('AD','admin'),
        ('NA','non_admin')
    ]
    #required fields
    email               = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username            = models.CharField(max_length=30, unique=True, primary_key=True)
    is_admin            = models.BooleanField(default=False) #system admin
    is_staff            = models.BooleanField(default=False) #memeber of staff
    date_joined         = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login          = models.DateTimeField(verbose_name="last_login", auto_now=True)
    is_active           = models.BooleanField(default=True)
    is_superuser        = models.BooleanField(default=False)

    #custom fields
    dwelling_code           = models.CharField(max_length=50, blank=False, default='Null')
    first_name              = models.CharField(max_length=50, blank=False, default='Null')
    surname                 = models.CharField(max_length=60, blank=False, default='Null')
    incentivisation_choice  = models.CharField(max_length=16, choices=GOAL_CHOICES,default='SM')
    goal                    = models.IntegerField(null=True)
    phone_number            = models.CharField(max_length=13, default='')
    admin_type              = models.CharField(max_length=2,default='NA', choices=ACCOUNT_CHOICES)
    logged_in               = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'  # whatever you want to be able to login with
    REQUIRED_FIELDS = ['username',]
    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class User_Data(models.Model):
    # user is is automaticly asigned on POST
    username            = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='username')
    energyused_ytd      = models.IntegerField(null=False, default=0) #users' usage year to date
    energyused_mtd      = models.IntegerField(null=False, default=0) #users' usage month to date
    energyused_day      = models.IntegerField(null=False, default=0) #users usage for today


# This is unsecure version of the accounts system as with the secure verison the front end has issues.
class Account_unsecure(models.Model):
    GOAL_CHOICES = [
        ('SM','Save Money'),
        ('HE', 'Help Environment')

    ]
    ACCOUNT_CHOICES =  [
        ('SA','super_admin'),
        ('AD','admin'),
        ('NA','non_admin')
    ]
    #required fields
    email                   = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username                = models.CharField(max_length=30, unique=True, primary_key=True, default='null')
    password                = models.CharField(max_length=50, blank=False, default='null')
    password2               = models.CharField(max_length=50, blank=False, default='null')
    dwelling_code           = models.CharField(max_length=50, blank=False, default='null')
    first_name              = models.CharField(max_length=50, blank=False, default='null')
    surname                 = models.CharField(max_length=60, blank=False, default='null')
    incentivisation_choice  = models.CharField(max_length=16, choices=GOAL_CHOICES,default='SM')
    goal                    = models.IntegerField(null=True)
    phone_number            = models.CharField(max_length=13, default='null')
    admin_type              = models.CharField(max_length=2,default='NA', choices=ACCOUNT_CHOICES)
    logged_in               = models.BooleanField(default=True)
    def __str__(self):
        return self.first_name+" "+self.surname
