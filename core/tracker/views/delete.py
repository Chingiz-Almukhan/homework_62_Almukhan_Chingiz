from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import DeleteView

from tracker.models.issue_tracker import IssueTracker
from tracker.views import CustomUserPassesMixin


class Delete(CustomUserPassesMixin, LoginRequiredMixin, DeleteView):
    model = IssueTracker
    groups = ['lead', 'manager', 'root']

    def get_success_url(self):
        return reverse_lazy('main')
