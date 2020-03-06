from django.views.generic import View
from django.shortcuts import render, redirect 




class CreateUserView(View):
    template_name = "accounts/registration/register.html"
    form_class = None 

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            "form": self.form_class 
        })

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        