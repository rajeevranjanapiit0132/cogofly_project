from django.shortcuts import render
from django.views.generic import View 


class DashboardIndexView(View):
    template_name = "home/dashboard/index.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name) 
        