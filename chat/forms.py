from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from .models import BotSetting, AddCompany, AppSetting, FbIntegrate , AddUserProfile





class BotSettingForm(ModelForm):

    class Meta:
         model = BotSetting

         fields = "__all__"

 
         widgets = {

            'api_key': forms.TextInput(attrs={'class': 'form-control','name':'fullname'}),
             'system_role': forms.Textarea(attrs={'class': 'form-control', 'name':'username', 'col': 80,'col': 20}),
             'bot_model': forms.TextInput(attrs={'class': 'form-control' ,'name':'email'}),
             'bot_name': forms.TextInput(attrs={'class': 'form-control' }),
             'bot_image': forms.FileInput(attrs={'class': 'form-control' ,  'name':'password'}),
            }


class AppSettingForm(ModelForm):

    class Meta:
         model = AppSetting

         fields = "__all__"

         widgets = {
             
             'app_footer': forms.TextInput(attrs={'class': 'form-control','name':'fullname'}),
             'app_signup_logo': forms.FileInput(attrs={'class': 'form-control', 'name':'username'}),
             'app_favicon': forms.FileInput(attrs={'class': 'form-control' ,'name':'email'}),
             'app_color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color' }),
             'app_title': forms.TextInput(attrs={'class': 'form-control' ,  'name':'password'}),
             'app_adminlogo': forms.FileInput(attrs={'class': 'form-control' ,  'name':'password'}),
             'app_loginimage': forms.FileInput(attrs={'class': 'form-control' ,  'name':'password'}),
             'app_admintext': forms.TextInput(attrs={'class': 'form-control' ,  'name':'password'}),

            
             }


class AppSettingEditForm(ModelForm):

    class Meta:
         model = AppSetting

         fields = "__all__"

         widgets = {
             
             'app_footer': forms.TextInput(attrs={'class': 'form-control','name':'fullname'}),
             'app_signup_logo': forms.FileInput(attrs={'class': 'form-control', 'name':'username'}),
             'app_favicon': forms.FileInput(attrs={'class': 'form-control' ,'name':'email'}),
             'app_color': forms.TextInput(attrs={'class': 'form-control', 'type': 'color' }),
             'app_title': forms.TextInput(attrs={'class': 'form-control' ,  'name':'password'}),
             'app_adminlogo': forms.FileInput(attrs={'class': 'form-control' ,  'name':'password'}),
             'app_loginimage': forms.FileInput(attrs={'class': 'form-control' ,  'name':'password'}),
             'app_admintext': forms.TextInput(attrs={'class': 'form-control' ,  'name':'password'}),

            
             }



class ProfileForm(ModelForm):

    class meta:
         model = AddUserProfile

         fields = "__all__"

         widgets ={
           'student_id' :  forms.NumberInput(attrs={'class' : 'form-control'})
         }


class CompanyEditForm(ModelForm):

    class Meta:
         model = AddCompany
         
         fields = "__all__"



         widgets = {
             
            'com_name': forms.TextInput(attrs={'class':'form-control','name':'fullname'}),
             'com_addresses': forms.TextInput(attrs={'class': 'form-control','id':'yourEmail', 'name':'username'}),
             'com_phone': forms.NumberInput(attrs={'class': 'form-control' ,'name':'email'}),
             'com_product': forms.TextInput(attrs={'class': 'form-control' ,}),
             'com_goods': forms.TextInput(attrs={'class': 'form-control' ,  'name':'password'}),
             'com_service': forms.TextInput(attrs={'class': 'form-control' ,  'name':'password'}),
             'com_email': forms.EmailInput(attrs={'class': 'form-control' ,  'name':'password'}),


            
             }

class IntegrateForm(ModelForm):

   class Meta:
       
    model = FbIntegrate

    fields = "__all__"

    widgets = {
                
    'fb_pagename': forms.TextInput(attrs={'class': 'form-control','name':'fullname'}),
    'fb_pageid': forms.TextInput(attrs={'class': 'form-control','name':'username'}),
    'fb_appname': forms.TextInput(attrs={'class': 'form-control' ,'name':'email'}),
    'fb_appid': forms.TextInput(attrs={'class': 'form-control' ,}),
    'fb_secretkey': forms.TextInput(attrs={'class': 'form-control' ,  'name':'password'}),
    'fb_verifytoken': forms.TextInput(attrs={'class': 'form-control' ,  'name':'password'}),
    'fb_accesstoken': forms.TextInput(attrs={'class': 'form-control' ,  'name':'password'}),
    'fb_logo': forms.FileInput(attrs={'class': 'form-control' ,  'name':'password'}),
              
            
    }

class CompanyForm(ModelForm):

    class Meta:
           
     model = AddCompany

     fields = "__all__"


     widgets = {
             'com_name': forms.TextInput(attrs={'class':'form-control','name':'fullname'}),
             'com_addresses': forms.TextInput(attrs={'class': 'form-control','id':'yourEmail', 'name':'username'}),
             'com_phone': forms.NumberInput(attrs={'class': 'form-control' ,'name':'email'}),
             'com_product': forms.TextInput(attrs={'class': 'form-control' ,}),
             'com_goods': forms.TextInput(attrs={'class': 'form-control' ,  'name':'password'}),
             'com_service': forms.TextInput(attrs={'class': 'form-control' ,  'name':'password'}),
             'com_email': forms.EmailInput(attrs={'class': 'form-control' ,  'name':'password'}),

            
         }