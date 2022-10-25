from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from tracker.forms import EditForm
from tracker.models import Project
from tracker.views import CustomUserPassesMixin


class EditUserView(CustomUserPassesMixin, LoginRequiredMixin, UpdateView):
    template_name = "edit_user.html"
    form_class = EditForm
    model = Project
    success_url = reverse_lazy('projects')
    context_object_name = 'project'
    groups = ['lead', 'manager', 'root']


