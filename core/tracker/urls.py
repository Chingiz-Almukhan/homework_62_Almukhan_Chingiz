from django.urls import path

from tracker.views.add import AddView
from tracker.views.add_project import AddProjectView
from tracker.views.base import IndexView
from tracker.views.base_project import ProjectView
from tracker.views.delete import Delete
from tracker.views.delete_project import DeleteProjectView
from tracker.views.edit import EditView
from tracker.views.edit_project_view import EditProjectView
from tracker.views.edit_user_view import EditUserView
from tracker.views.project_view import ProjectDetailView
from tracker.views.task_view import TaskView

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('task/<int:pk>', TaskView.as_view(), name='task'),
    path('add/<int:pk>', AddView.as_view(), name='add'),
    path('edit/<int:pk>', EditView.as_view(), name='edit'),
    path('delete/confirm/<int:pk>', Delete.as_view(), name='delete'),
    path('projects/', ProjectView.as_view(), name='projects'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project'),
    path('add/project', AddProjectView.as_view(), name='add_project'),
    path('edit/user/<int:pk>', EditUserView.as_view(), name='edit_user'),
    path('delete/project/<int:pk>', DeleteProjectView.as_view(), name='delete_project'),
    path('edit/project/<int:pk>', EditProjectView.as_view(), name='edit_project')
]
