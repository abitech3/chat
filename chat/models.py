from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms
from django.core.validators import RegexValidator



class User(AbstractUser) :
	class Role(models.TextChoices):
		ADMIN = "ADMIN", "Admin"
		USER = "USER", "User"

	base_role = Role.ADMIN

	role =models.CharField(max_length=100 , choices = Role.choices)

	user_image = models.ImageField(upload_to='images/' , default="chat/assets/images/first-chat.png")




	def save(self, *args, **kwargs):
		if not self.pk:
			self.role = self.base_role
			return super().save(*args , **kwargs)
		


class AddUserManager(BaseUserManager):
	def get_queryset(self, *agrs, **kwagrs):
		results =super().get_queryset(*agrs , **kwagrs)
		return results.filter(role=User.Role.USER)
	
class AddUser(User):
    base_role = User.Role.USER
	
    user = AddUserManager()

    user_id = models.IntegerField(default=1)

	 
    class meta:
	    proxy = True
		
    # def welcome(self):
	#     return "welcome"
	
class AddUserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	student_id = models.IntegerField(null=True, blank=True , default=1)



@receiver(post_save, sender=AddUser)
def create_user_profile(sender, instance, created, **kwargs):
	if created and instance == "USER":
		AddUserProfile.objects.create(user=instance)	
 

class ColorField(models.CharField):
    default_validators = [
        RegexValidator(
            regex=r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
            message='Enter a valid color code.',
            code='invalid_color'
        ),
    ]

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 7)
        super().__init__(*args, **kwargs)


class BotSetting(models.Model):
	user_id = models.IntegerField(default=1)
	api_key = models.CharField(max_length = 200)
	system_role = models.CharField(max_length =100)
	bot_model = models.CharField(max_length= 400)
	bot_name = models.CharField(max_length= 100)
	bot_image = models.ImageField(upload_to='images/')



class AddCompany(models.Model):
    com_name = models.CharField(max_length=100)
    com_addresses = models.CharField(max_length=100)
    com_phone = models.IntegerField()
    com_product = models.CharField(max_length=100)
    com_goods = models.CharField(max_length=100)
    com_service = models.CharField(max_length=100)
    com_email = models.EmailField()
    user_id  = models.IntegerField(default=1)



class AppSetting(models.Model):
	user_id = models.IntegerField(default=1)
	app_footer = models.CharField(max_length=100)
	app_signup_logo = models.ImageField(upload_to='images/')
	app_favicon = models.ImageField(upload_to='images/')
	app_color = ColorField()
	app_title = models.CharField(max_length=100)
	app_adminlogo = models.ImageField(upload_to='images/')
	app_loginimage = models.ImageField(upload_to='images/')
	app_admintext = models.CharField(max_length=100)


class FbIntegrate(models.Model ):
	user_id = models.IntegerField(default=1)
	fb_pagename = models.CharField(max_length=100)
	fb_pageid = models.CharField(max_length=100)
	fb_appname = models.CharField(max_length=100)
	fb_appid = models.CharField(max_length=100)
	fb_secretkey = models.CharField(max_length=100)
	fb_verifytoken = models.CharField(max_length=100)
	fb_accesstoken = models.CharField(max_length=100)
	fb_logo = models.ImageField(upload_to='images/')

	
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.message}'






	



	


	

