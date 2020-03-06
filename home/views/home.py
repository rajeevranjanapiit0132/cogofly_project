from django.shortcuts import render
from django.views.generic import View 


class IndexView(View):
    """
    Index page of cogofly.com
    """
    template_name = "home/index.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name) 

