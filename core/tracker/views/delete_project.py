from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import DeleteView

from tracker.models import Project
from tracker.views import CustomUserPassesMixin


class DeleteProjectView(CustomUserPassesMixin, LoginRequiredMixin, DeleteView):
    model = Project
    groups = ['manager', 'root']

    def get_success_url(self):
        return reverse_lazy('projects')
