from django.db import models

class IPO(models.Model):
    company_name = models.CharField(max_length=100)
    issue_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name
