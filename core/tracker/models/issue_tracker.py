from django.db import models
from django.utils import timezone


class IssueTracker(models.Model):
    summary = models.CharField(verbose_name='Заголовок', max_length=200, null=False, blank=False)
    description = models.TextField(verbose_name='Подробное описание', max_length=500, null=True, blank=True)
    status = models.ForeignKey('tracker.Status', related_name='statuses', blank=True, on_delete=models.RESTRICT,
                               verbose_name='Статус', default='1')
    project = models.ForeignKey('tracker.Project', related_name='projects', blank=True, verbose_name='Проект',
                                on_delete=models.CASCADE, default='1')
    type = models.ManyToManyField('tracker.Type', related_name='types', blank=True, verbose_name='Тип', default='1')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    changed_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_deleted = models.BooleanField(verbose_name='Удалено', default=False, null=False)

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()

    def __str__(self):
        return f'{self.summary}'
