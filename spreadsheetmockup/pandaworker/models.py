from django.db import models

# Create your models here.


class FileTemplate(models.Model):
    DAILY = 'DY'
    WEEKLY = 'WY'
    MONTHLY = 'MY'
    INTERVAL_CHOICES = [
        (DAILY, 'Daily'),
        (WEEKLY, 'Weekly'),
        (MONTHLY, 'Monthly'),
    ]
    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, blank=True)
    fileImport = models.FileField()
    column_labels = models.TextField(blank=True)
    intervals = models.CharField(
        max_length=2,
        choices=INTERVAL_CHOICES,
        default=DAILY,
    )
    live_instances = models.IntegerField(default=1)
    save_history = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class LiveReport(models.Model):
    template = models.ForeignKey(FileTemplate, on_delete=models.CASCADE)
    report_id = models.CharField(blank=True, max_length=200)
    live_file = models.FileField(blank=True)
    live_data = models.TextField(blank=True)

    def __str__(self):
        return self.report_id


class ReportFlows(models.Model):
    downstream = models.ForeignKey(FileTemplate, models.SET_NULL, blank=True, null=True, related_name='downstream')
    feed_complete = models.BooleanField(default=False)
    upstream = models.ForeignKey(FileTemplate, models.SET_NULL, blank=True, null=True, related_name='upstream')

    def __str__(self):
        return self.downstream.name + "," + self.upstream.name

