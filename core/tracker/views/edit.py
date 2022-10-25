from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from tracker.forms import AddEditForm
from tracker.models.issue_tracker import IssueTracker


class EditView(LoginRequiredMixin, UpdateView):
    template_name = "edit_task.html"
    form_class = AddEditForm
    model = IssueTracker
    success_url = reverse_lazy('main')
    context_object_name = 'article'
