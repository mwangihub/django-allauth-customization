# Django-allauth customization

This project aims to reduce the number of customization needed to be implemented in django-allauth.

Django-all auth is amazing package with a lot of features.

In the event where we need a complete customized user model, we will have to overrride ```allauth.accounts```.
Thanks to ```DefaultAccountAdapter DefaultSocialAccountAdapter allauth.socialaccount.signals```
```allauth.account.signals && providers``` we will be able to determine how custom user will be saved.

 For this case we are using django-allauth to create diffrent types of user accounts with custom User models 
 i.e ```alts.models```
