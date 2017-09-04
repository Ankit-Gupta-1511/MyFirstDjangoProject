from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import authenticate, login
from django.template import loader
from django.http import HttpResponse
from products.models import Product, Stock, Categories, SubCategories
from .forms import SignUpForm
# Create your views here.
all_categories = Categories.objects.all()
sub_categories_menu = SubCategories.objects.all()
def index(request):
     html="<h1>Hey I am in user_portal</h1>"
     return HttpResponse(html)

def signup(request):
     template = loader.get_template('user/signup.html')
     context={
        'all_categories': all_categories,
        'sub_categories_menu': sub_categories_menu,
     }
     return HttpResponse(template.render(context, request))

def signup_submit(request):
     template = loader.get_template('user/signup.html')
     context={
        'all_categories': all_categories,
        'sub_categories_menu': sub_categories_menu,
     }
     return HttpResponse(template.render(context, request))

class SignUp(generic.View):
    form_class = SignUpForm
    template_name = 'user/signup.html'

    #display blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form': form})

    #display data filled form
    def post(self,request):
        print('heya its post')
        form =self.form_class(request.POST)
        print('hey i am gonna check for validation')
        #validity check
        print(form.is_valid())
        if form.is_valid():
            print('heya its valid')
            user = form.save(commit= False)

            #cleaned data
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user.set_password(password)
            print(user)
            user.save()
            print('Hey i am authenticating')
            #authentication
            user = authenticate(username=username,password=password)
            print(user)
            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('products:index')
        return render(request, self.template_name, {'form': form})
