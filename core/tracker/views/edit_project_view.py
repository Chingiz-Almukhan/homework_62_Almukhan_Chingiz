from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from tracker.forms import AddProjectForm
from tracker.models import Project
from tracker.views import CustomUserPassesMixin


class EditProjectView(CustomUserPassesMixin, LoginRequiredMixin, UpdateView):
    template_name = "edit_project.html"
    form_class = AddProjectForm
    model = Project
    success_url = reverse_lazy('projects')
    groups = ['manager', 'root']
