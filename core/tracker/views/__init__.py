from django.contrib.auth.mixins import UserPassesTestMixin


class CustomUserPassesMixin(UserPassesTestMixin):
    groups = []

    def test_func(self):
        return self.request.user.groups.filter(name__in=self.groups).exists()
