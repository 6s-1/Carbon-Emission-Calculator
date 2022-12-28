from rest_framework import serializers
from . models import RecentUsage, BatteryUsage, TimeStamp


class RecentUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentUsage
        fields = [
            "source",
            "capacity_percent",
            "capacity",
        ]

class BatteryUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatteryUsage
        fields = [
            "duration",
            "energy_percent",
            "energy",
        ]

class TimeStampSerializer(serializers.ModelSerializer):
    ru = RecentUsageSerializer(read_only=True)
    bu = BatteryUsageSerializer(read_only=True)
    class Meta:
        model = TimeStamp
        fields = [
            "uid",
            "date",
            "time",
            "state",
            "ru",
            "bu"
        ]