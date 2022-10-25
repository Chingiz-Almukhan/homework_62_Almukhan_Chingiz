from urllib.parse import urlencode

from django.views.generic import ListView

from tracker.models import Project


class ProjectView(ListView):
    template_name = 'project_page.html'
    model = Project
    context_object_name = 'projects'
