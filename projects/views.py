from bootstrap_modal_forms.generic import (BSModalCreateView, BSModalUpdateView, BSModalDeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView,CreateView
from django.shortcuts import render, redirect, HttpResponseRedirect,HttpResponse
from django.urls import reverse_lazy, reverse
from .filters import *
from .models import *
from .forms import *
from user.models import *
from user.forms import *
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail


# Create your views here.
def register_request(request):
    if request.method == 'POST':
        form = Employee_user_form(request.POST, request.FILES)
        form2 = Employee_form(request.POST, request.FILES)
        if form.is_valid() and form2.is_valid():
            user = form.save()
            password = User.objects.make_random_password()
            user.set_password(password)
            user.is_active = False
            print(password)
            user.save()
            employee = form2.save(commit=False)
            employee.user = user
            employee.save()

            emailid = request.POST.get('email')
            fname = request.POST.get('first_name')
            lname = request.POST.get('last_name')
            mobile = request.POST.get('phone_no')
            # passwordd = request.POST.get('password')
            subject = 'Register Request'
            message = f'''Hello Sir/Mam,

                            Your account has been created successfully.

                            First Name= {fname}
                            Last Name = {lname}
                            Mobile Number = {mobile}
                            User_id = {emailid}

            Best Regards,
            {fname} {lname}'''
            send_mail(
                subject,
                message,
                'from@mail.com',
                ['asif.md@finnovo.io'],
                fail_silently=False,
            )

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
            messages.success(request, "Your request has been send successfully")

    else:
        form = Employee_user_form()
        form2 = Employee_form()
    return render(request, 'register request.html', {'form': form, 'form2': form2})


# Projects list View
class Projects_list_view(LoginRequiredMixin, ListView):
    model = Projects
    form_class = AddprojectModelForm
    second_form_class = ProjectImageForm
    third_form_class = ProjectFilesForm
    template_name = 'Projects/Projects_list_view.html'
    context_object_name = 'projects'
    success_url = reverse_lazy('projects_list')

    def get_queryset(self):
        queryset = super().get_queryset()
        filter = Filterss(self.request.GET, queryset)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()
        if 'form3' not in context:
            context['form3'] = self.third_form_class()
        queryset = self.get_queryset()
        filter = Filterss(self.request.GET, queryset)
        model2 = Employee.objects.all()
        context["myfilter"] = filter
        context["empdata"] = model2
        return context


# Projects CARDS VIEW
class Projects_Card_View(LoginRequiredMixin, ListView):
    model = Projects
    template_name = 'Projects/Projects_cards_view.html'
    context_object_name = 'projects'
    success_url = reverse_lazy('projects_cards')

    def get_queryset(self):
        queryset = super().get_queryset()
        filter = Filterss(self.request.GET, queryset)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = self.get_queryset()
        filter = Filterss(self.request.GET, queryset)
        model2 = Employee.objects.all()
        context["myfilter"] = filter
        context["empdata"] = model2
        return context

# ------------------------#
# PROJECT CURD OPERATIONS
# -------------------------#

# RETRIEVE PROJECT
@login_required(login_url='login_page')
def ProjectDetailView(request, id):
    data1 = Projects.objects.get(pk=id)
    data2 = Project_Images.objects.filter(project_img=data1)
    data3 = Project_Files.objects.filter(project=data1)
    data4 = assigneform(instance=data1)
    if request.method == "POST":
        data = assigneform(request.POST, instance=data1)
        data.save()
        return HttpResponseRedirect(reverse('project_details', args=[id]))
    return render(request, 'Projects/Project_detail_view.html',
                  {'projects': data1, 'form2': data2, 'form3': data3, 'form4': data4})


# POST NEW PROJECT
@login_required(login_url='login_page')
def Add_Project_View(request):
    project_form = AddprojectModelForm()
    image_form = ProjectImageForm()
    file_form = ProjectFilesForm()
    if request.method == 'POST':
        project_form = AddprojectModelForm(request.POST, request.FILES)
        image_form = ProjectImageForm(request.POST, request.FILES)
        file_form = ProjectFilesForm(request.POST, request.FILES)
        images = request.FILES.getlist('project_images')
        files = request.FILES.getlist('upload_documents')
        if (project_form.is_valid(), image_form.is_valid(), file_form.is_valid()):
            project_instance = project_form.save(commit=False)
            project_instance.save()
            for i in images:
                image_instance = Project_Images(project_images=i, project_img=project_instance)
                image_instance.project_img = project_instance
                image_instance.save()
            for f in files:
                file_instance = Project_Files(upload_documents=f, project=project_instance)
                file_instance.project = project_instance
                file_instance.save()
                return redirect('projects_list')

        return HttpResponseRedirect(reverse_lazy('projects_list'))

    return render(request, 'Projects/addproject.html', {'form': project_form, 'form2': image_form, 'form3': file_form})


# Update PROJECT
@login_required(login_url='login_page')
def ProjectUpdateView(request, id):
    update_project = Projects.objects.get(pk=id)
    projectview = AddprojectModelForm(instance=update_project)
    Images_Project = Project_Images.objects.filter(project_img=update_project)
    Files_Project = Project_Files.objects.filter(project=update_project)
    imagesview = [ProjectImageForm(prefix=str(images.id), instance=images) for images in Images_Project]
    filesview = [ProjectFilesForm(prefix=str(files.id), instance=files) for files in Files_Project]
    addimages = ProjectImageForm()
    addfiles = ProjectFilesForm()
    if request.method == "POST":
        projectviews = AddprojectModelForm(request.POST, request.FILES, instance=update_project)
        imagesview = [ProjectImageForm(request.POST, request.FILES,
                                       prefix=str(images.id), instance=images) for images in Images_Project]
        filesview = [ProjectFilesForm(request.POST, request.FILES,
                                      prefix=str(filess.id), instance=filess) for filess in Files_Project]
        if (
        projectviews.is_valid(), all([fv.is_valid() for fv in filesview]), all([iv.is_valid() for iv in imagesview])):
            project_instance = projectviews.save(commit=False)
            project_instance.save()
            for iv in imagesview:
                images_instance = iv.save(commit=False)
                images_instance.update_project = project_instance
                images_instance.save()
            for fv in filesview:
                files_instance = fv.save(commit=False)
                files_instance.update_project = project_instance
                files_instance.save()
            addimages = ProjectImageForm(request.POST, request.FILES)
            addfiles = ProjectImageForm(request.POST, request.FILES)
            images = request.FILES.getlist('project_images')
            files = request.FILES.getlist('upload_documents')
            if addimages.is_valid() and addfiles.is_valid():
                for i in images:
                    image_instance = Project_Images(project_images=i, project_img=project_instance)
                    image_instance.project_img = project_instance
                    image_instance.save()
                for f in files:
                    file_instance = Project_Files(upload_documents=f, project=project_instance)
                    file_instance.project = project_instance
                    file_instance.save()
                return redirect('projects_list')
    return render(request, 'Projects/update_project.html',
                  {'form': projectview, 'form2': Images_Project, 'form3': Files_Project, 'addimg': addimages,
                   'addfile': addfiles})


@login_required(login_url='login_page')
def ProjectDeleteView(request, id):
    dlp = Projects.objects.get(pk=id)
    dlp.delete()
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url='login_page')
def DeleteImageView(request, id):
    dli = Project_Images.objects.get(pk=id)
    dli.delete()
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url='login_page')
def DeleteFileView(request, id):
    dlf = Project_Files.objects.get(pk=id)
    dlf.delete()
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url='login_page')
def dashboard(request):
    data = Projects.objects.all()
    data2 = Project_Images.objects.all()
    data3 = Project_Files.objects.all()
    data4 = Employee.objects.all()
    return render(request, 'dashboard.html', {'data': data, 'data2': data2, 'data3': data3, 'data4': data4})


def test1(request):
    data = AddprojectModelForm()
    return render(request, 'test.html', {'form': data})
