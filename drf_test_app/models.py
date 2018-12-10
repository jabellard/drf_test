from django.db import models

# Create your models here.


class Test(models.Model):
    test_id = models.AutoField(
        primary_key=True,
    )

    test_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.test_name
