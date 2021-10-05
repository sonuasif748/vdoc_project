from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from projects.filters import *
from .forms import *
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password, check_password, pbkdf2


# Create your views here.

# Employee REGISTRATION
@login_required(login_url='login_page')
def Employee_Registration(request):
    employeeuserform = Employee_user_form()
    employeeform = Employee_form()
    mydict = {'form': employeeuserform, 'form2': employeeform}
    if request.method == "POST":
        euf = Employee_user_form(request.POST)
        ef = Employee_form(request.POST, request.FILES)
        if euf.is_valid() and ef.is_valid():
            user = euf.save()
            user.set_password(user.password)
            user.save()
            employee = ef.save(commit=False)
            employee.user = user
            employee.save()

            emailid = request.POST.get('email')
            password = request.POST.get('password')
            subject = 'V-Docs Activation'
            message = f'''Hello Sir/Mam,
            
                Your account has been created successfully.
                
                User_id = {emailid}
                Password = {password}
                
Best Regards,
V-Doc's'''
            send_mail(
                subject,
                message,
                'from@mail.com',
                [emailid],
                fail_silently=False,
            )

            user.groups.add(Group.objects.get(name='Employee'))
            return redirect('Employee_list_page')
    return render(request, 'users/Employee/employee_reg.html', context=mydict)


# USER PROFILE VIEWS
@login_required(login_url='login_page')
def User_profile(request):
    data = Employee.objects.all()
    return render(request, 'users/profile.html',{'data':data})


# USERS BY CONDITION
def is_Employee(user):
    a = user.groups.filter(name='Employee')
    return a


# AUTHENTICATION
def Login_User(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # user = auth.authenticate(username=User.objects.get(email=username), password=password)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if User.is_superuser:
                return redirect('/')
            if User.is_active:
                return redirect('/')
            else:
                return redirect('login_page')

    return render(request, 'users/login.html')

def Logout_User(request):
    logout(request)
    return redirect("login_page")

class Employees_list_view(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'users/Employee/employee_list.html'
    context_object_name = 'employee'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter = Userlist(self.request.GET, queryset)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        filter = ListFilter(self.request.GET, queryset)
        context["filter"] = filter
        return context

def update_status(request,status,id):
    a = User.objects.filter(id=id)
    a.update(is_active=status)

    emailid = a[0].email
    subject = 'V-Docs Activation'
    message = f'''Hello Sir/Mam,

                    Your account has been created successfully.

                    User_id = {emailid}
                    Now Activated, You can Login now

    Best Regards,
    V-Doc's'''
    send_mail(
        subject,
        message,
        'from@mail.com',
        [emailid],
        fail_silently=False,
    )

    return redirect('Employee_list_page')


# bb - YhaWLEWS9Q