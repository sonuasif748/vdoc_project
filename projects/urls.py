from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url
from .filters import ListFilter
from django.urls import path
from projects import views
from .views import *

urlpatterns = [
    path('register_request',register_request, name='homepage'),
    path('Homepage', login_required(Projects_list_view.as_view()), name='projects_list'),
    path('projects_cards', login_required(Projects_Card_View.as_view()), name='projects_cards'),
    path('add_project/', Add_Project_View, name='add_project'),
    path('project_update/<int:id>/', ProjectUpdateView, name='project_update'),
    path('delete_project/<int:id>/', ProjectDeleteView, name='delete_project'),
    path('project_details/<int:id>/',ProjectDetailView, name='project_details'),
    path('test/',test1, name='test'),
    path('deleteimage/<int:id>/',DeleteImageView, name='deleteimage'),
    path('deletefile/<int:id>/',DeleteFileView, name='deletefile'),
    path('',dashboard, name='dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
