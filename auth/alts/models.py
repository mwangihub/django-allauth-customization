from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from allauth.account.signals import user_signed_up
from django.dispatch import receiver

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.non = False
        user.save(using=self._db)
        return user



class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255,unique=True,)
    first_name =  models.CharField(verbose_name='first name',max_length=255,)
    last_name =  models.CharField(verbose_name='last name',max_length=255,)
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False) 
    admin = models.BooleanField(default=False)
    buyer = models.BooleanField(default=False)
    employee = models.BooleanField(default=False) 
    non = models.BooleanField(default=True) 
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["names",]

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_buyer(self):
        return self.buyer

    @property
    def is_employee(self):
        return self.employee

    @property
    def is_non(self):
        return self.non

@receiver(user_signed_up)
def populate_profile(sociallogin, user, **kwargs):    
    user.active=True
    user.save()
    '''Very useful to set user profile account. Uncomment bootom user save methods if 
    there is user profile model you can 
    print(user.socialaccount_set.filter(provider=sociallogin.account.provider)[0].extra_data) 
    to see extra data from the provider '''
    if sociallogin.account.provider == 'facebook':
        data = user.socialaccount_set.filter(provider='facebook')[0].extra_data
        picture_url = "http://graph.facebook.com/" + sociallogin.account.uid + "/picture?type=large"            
        email = data['email']
        first_name = data['first_name']

    # user.profile.avatar_url = picture_url
    # user.profile.email_address = email
    # user.profile.first_name = first_name
    # user.profile.save()
