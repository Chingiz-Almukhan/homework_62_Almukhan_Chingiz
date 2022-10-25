from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy

from tracker.forms import AddProjectForm
from tracker.models import Project
from tracker.views import CustomUserPassesMixin


class AddProjectView(CustomUserPassesMixin, LoginRequiredMixin, CreateView):
    template_name = 'add_project.html'
    success_url = reverse_lazy('projects')
    model = Project
    form_class = AddProjectForm
    groups = ['manager', 'root']


