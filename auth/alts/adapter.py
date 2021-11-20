from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse

class AccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        url = reverse("profile")
        return url

    def get_signup_redirect_url(self, request):
        url = reverse("choose-user")
        return url

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class SocialAccountAdapter(DefaultSocialAccountAdapter):

    def get_connect_redirect_url(self, request, socialaccount):
        assert request.user.is_authenticated
        url = reverse("profile")
        return url

