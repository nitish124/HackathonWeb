from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

status_choices = (
    ('evclient', 'evclient'),
    ('evdealer', 'evdealer'),
    ('evmender', 'evmender')
)

class MyAccountManager(BaseUserManager):
    #for creating Normal User
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            return ValueError('User must have an email address')
        
        if not username:
            return ValueError('User must have an username')
        
        user = self.model(
            email = self.normalize_email(email),#normalize_email is use to lowercase all letters in the email
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    #For creating SuperUser
    def create_superuser(self, first_name, last_name, email, username, password):
        #We use the create_user function that we created above
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models. EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)
    point_accumulator = models.IntegerField(default=0)

    #required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=status_choices, default='evclient')

    #Set login Field - Login with email addresse
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    #When we return the account object in template this should return the email addresse
    def __str__(self):
        return self.email
    
    #If the user is admin,, he has all the permission to change everything
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
