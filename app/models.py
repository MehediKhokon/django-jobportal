from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User

# Create your models here.
class JobPost(models.Model):
    job_name = models.CharField(max_length=80)
    company_name = models.CharField(max_length=80)
    category = models.CharField(max_length=50, default='IT', choices=(
        ('accounting', 'Accounting'),
        ('it', 'IT'),
        ('marketing', 'Marketing'),
        ('customer support', 'Customer Support')
    ))
    vacency = models.IntegerField()
    job_responsibilities = models.TextField()
    emp_status = models.CharField(max_length=80)
    education_req = models.TextField()
    experiance_req = models.TextField()
    add_req = models.TextField()
    job_location = models.TextField()
    salay = models.CharField(max_length=80, default='N/A')
    other_benefit = models.TextField(blank=True, default='N/A')
    publish_date = models.DateTimeField(default=datetime.now)
    application_deadline = models.CharField(max_length=80)


    def __str__(self):
        return self.job_name

    class Meta:
        ordering = ['-id']
        
            
class Cv(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    present_address = models.CharField(max_length=80)
    career_objective = models.TextField(blank= True)
    ssc_result = models.CharField(max_length=20)
    hsc_result = models.CharField(max_length=20)
    bsc_result = models.CharField(max_length=20)
    msc_result = models.CharField(max_length=20)
    phd = models.CharField(max_length=20, default= 0)
    no_of_work_experiance = models.CharField(max_length=20)
    language_skill = models.CharField(max_length=50, default='Bangla', choices=(
        ('bangla', 'Bangla'),
        ('english', 'English'),
        ('both', 'Both'),
    ))
    interest = models.CharField(max_length=50)
    total =  models.CharField(max_length=50, default=20)

    jobpost = models.ManyToManyField(
        JobPost, blank=True
    )

    def __str__(self):
        return 'Name: {}| Email: {}|Total: {}'.format(self.name, self.email, self.total)

    class Meta:
        ordering = ['-total']