from django import forms
from .models import *
from django.forms import ClearableFileInput
from django.forms import modelformset_factory
from multiselectfield import MultiSelectFormField

class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, user):
        return "%s" % User.username

a = Employee.objects.all()
co_author_choices = [(i.user.username,i.user.username) for i in a]

class AddprojectModelForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['Author','co_author','title','abstract','project_keywords','mentor','start_date','completion_date','status','work_progress']
        co_author = forms.MultipleChoiceField(choices=co_author_choices, widget=forms.CheckboxSelectMultiple(attrs={'class':'form-control','multiple':"multiple"}))

        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter project title here'}),
            'abstract': forms.Textarea(attrs={'class': 'form-control summernote', 'rows':'4','placeholder':'Enter your text here'}),
            'project_keywords': forms.Textarea(attrs={'class': 'form-control', 'rows':'2','placeholder':'Enter your text here'}),
            'mentor': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your mentor here'}),
            'Author': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control datetimepicker' }),
            'completion_date': forms.DateInput(attrs={'class': 'form-control datetimepicker'}),
            # 'images' : forms.ClearableFileInput(attrs={'class': 'form-control','type':'file', 'name':'upload_documents'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'work_progress': forms.Select(attrs={'class': 'form-control'}),

        }

class ProjectImageForm(forms.ModelForm):
    class Meta:
        model = Project_Images
        fields = ['project_images']

        widgets = {
        'project_images' : forms.ClearableFileInput(attrs={'multiple': True,'class': 'form-control','id':'img','type':'file', 'name':'upload_documents'}),
        }


class ProjectFilesForm(forms.ModelForm):
    class Meta:
        model = Project_Files
        fields = ['upload_documents']

        widgets = {
        # 'cover' : forms.ClearableFileInput(attrs={'multiple': True,'class': 'form-control','id':'img','type':'file', 'name':'upload_documents'}),
        'upload_documents' : forms.ClearableFileInput(attrs={'multiple': True,'class': 'form-control','id':'files','type':'file', 'name':'upload_documents'}),
        }

class assigneform(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['co_author']
        co_author = forms.MultipleChoiceField(choices=co_author_choices,
                                              widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}))

