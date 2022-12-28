from django.db import models
from django.urls import reverse

# Create your models here.
class TimeStamp(models.Model):

    uid = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    state = models.CharField(max_length=50)

    class Meta:
        verbose_name ="TimeStamp"
        verbose_name_plural ="TimeStamps"

    def __str__(self):
        return f"{self.uid} --> {self.date} --- {self.time}"

    def get_absolute_url(self):
        return reverse("TimeStamp_detail", kwargs={"pk": self.pk})



class RecentUsage(models.Model):

    timestamp = models.OneToOneField(TimeStamp, related_name="ru", on_delete=models.CASCADE)
    source = models.CharField(max_length=50)
    capacity_percent = models.IntegerField()
    capacity = models.IntegerField()

    class Meta:
        verbose_name = "recent_usage"
        verbose_name_plural = "recent_usages"

    def __str__(self):
        return f"{self.timestamp.date} --- {self.timestamp.time} <-- {self.timestamp.uid}"

    def get_absolute_url(self):
        return reverse("recent_usage_detail", kwargs={"pk": self.pk})


class BatteryUsage(models.Model):

    timestamp = models.OneToOneField(TimeStamp, related_name="bu", on_delete=models.CASCADE)
    duration = models.TimeField(auto_now=False, auto_now_add=False)
    energy_percent = models.IntegerField()
    energy = models.IntegerField()


    class Meta:
        verbose_name = "battery_usage"
        verbose_name_plural = "battery_usages"

    def __str__(self):
        return f"{self.timestamp.date} --- {self.timestamp.time} <-- {self.timestamp.uid}"

    def get_absolute_url(self):
        return reverse("battery_usage_detail", kwargs={"pk": self.pk})
