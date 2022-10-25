from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy
from tracker.forms import AddEditForm
from tracker.models import IssueTracker, Project
from tracker.views import CustomUserPassesMixin


class AddView(CustomUserPassesMixin, LoginRequiredMixin, CreateView):
    template_name = 'add_task.html'
    success_url = reverse_lazy('main')
    model = IssueTracker
    form_class = AddEditForm
    groups = ['dev', 'lead', 'manager', 'root']

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        form.instance.project = project
        return super(AddView, self).form_valid(form)


