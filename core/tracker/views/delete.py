from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from django.views.generic import DeleteView

from tracker.models.issue_tracker import IssueTracker


class Delete(LoginRequiredMixin, DeleteView):
    model = IssueTracker

    def get_success_url(self):
        return reverse_lazy('main')
