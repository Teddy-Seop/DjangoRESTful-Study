from django.db import models

class posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    writer = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class container(models.Model):
    c_id = models.IntegerField(primary_key=True)
    entry = models.CharField(max_length=100)
    output = models.CharField(max_length=100)
    arrival = models.DateTimeField(auto_now=True)
    departure = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=100)
    load = models.CharField(max_length=100)
    weight = models.IntegerField()
    temparature = models.FloatField()
    humidity = models.FloatField()

    def __str__(self):
        return self.title