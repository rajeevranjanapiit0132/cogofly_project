from django.contrib.auth.views import LoginView
from django.conf import settings

from ..forms import UserAuthForm 


class UserAuthView(LoginView):
    """
    User login page, redirect user to /home/
    after login successful
    """
    template_name = "accounts/auth/login.html"
    form_class = UserAuthForm 

    def get_success_url(self):
        url = self.get_redirect_url() 
        return url or settings.LOGIN_REDIRECT_URL 
