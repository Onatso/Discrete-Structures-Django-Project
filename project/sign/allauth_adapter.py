from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model

User = get_user_model()

class MySocialAccountAdapter(DefaultSocialAccountAdapter):

    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user

        if not user.email:
            return

        try:
            existing_user = User.objects.get(email=user.email)
            sociallogin.connect(request, existing_user)
        except User.DoesNotExist:
            pass

    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form)

        if not user.username:
            extra_data = sociallogin.account.extra_data
            user.username = extra_data.get("name", user.email.split("@")[0])
            user.save()

        email_address, created = EmailAddress.objects.get_or_create(
            user=user, email=user.email
        )
        email_address.verified = True
        email_address.save()

        return user