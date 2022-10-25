from django.views.generic import DetailView

from tracker.models.issue_tracker import IssueTracker


class TaskView(DetailView):
    template_name = 'task_view.html'
    model = IssueTracker
    context_object_name = 'task'
