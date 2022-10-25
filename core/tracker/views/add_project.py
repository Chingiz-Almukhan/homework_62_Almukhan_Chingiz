from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy

from tracker.forms import AddProjectForm

from tracker.views.base_project import ProjectView


class AddProjectView(LoginRequiredMixin, CreateView):
    template_name = 'add_project.html'
    success_url = reverse_lazy('projects')
    model = ProjectView
    form_class = AddProjectForm
