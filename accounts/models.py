from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):

    def create_user(self, email, password, first_name, last_name):
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name
        )
        user.set_password(password) 
        user.save(using=self._db) 
        return user 

    def create_superuser(self, email, password, first_name, last_name):
        user = self.create_user(email, password, first_name, last_name)
        user.is_staff = True 
        user.is_superuser = True 
        user.save(using=self._db)
        return user 

    



class User(PermissionsMixin, AbstractBaseUser):
    GENDER_CHOICES = (
        (None, "Select gender"),
        ("M", "Male"),
        ("F", "Female"), 
    )   
    
    email = models.EmailField(unique=True) 
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, null=True) 
    gender = models.CharField(max_length=1, null=True, choices=GENDER_CHOICES)
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(
        upload_to="profile_images",
        null=True, blank=True
    ) 

    is_staff = models.BooleanField("Staff Status", default=False) 
    is_active = models.BooleanField("Active Status", default=True) 
    is_validated = models.BooleanField("Validation Status", default=False) 
    is_traveller = models.BooleanField("Traveller Status", default=False)  
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email" 
    REQUIRED_FIELDS = ["first_name", "last_name"] 

    class Meta:
        db_table = "user_accounts" 
        verbose_name = "User Account"
        verbose_name_plural = "User Accounts"
        ordering = ("-created_at",)

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.email 

    def __str__(self):
        return self.get_full_name() 


