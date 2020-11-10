# Generated by Django 2.2 on 2019-04-20 19:22

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(max_length=80)),
                ('company_name', models.CharField(max_length=80)),
                ('category', models.CharField(choices=[('accounting', 'Accounting'), ('it', 'IT'), ('marketing', 'Marketing'), ('customer support', 'Customer Support')], default='IT', max_length=50)),
                ('vacency', models.IntegerField()),
                ('job_responsibilities', models.TextField()),
                ('emp_status', models.CharField(max_length=80)),
                ('education_req', models.TextField()),
                ('experiance_req', models.TextField()),
                ('add_req', models.TextField()),
                ('job_location', models.TextField()),
                ('salay', models.CharField(default='N/A', max_length=80)),
                ('other_benefit', models.TextField(blank=True, default='N/A')),
                ('publish_date', models.DateTimeField(default=datetime.datetime.now)),
                ('application_deadline', models.CharField(max_length=80)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Cv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=80)),
                ('present_address', models.CharField(max_length=80)),
                ('career_objective', models.TextField(blank=True)),
                ('ssc_result', models.CharField(max_length=20)),
                ('hsc_result', models.CharField(max_length=20)),
                ('bsc_result', models.CharField(max_length=20)),
                ('msc_result', models.CharField(max_length=20)),
                ('phd', models.CharField(default=0, max_length=20)),
                ('no_of_work_experiance', models.CharField(max_length=20)),
                ('language_skill', models.CharField(choices=[('bangla', 'Bangla'), ('english', 'English'), ('both', 'Both')], default='Bangla', max_length=50)),
                ('interest', models.CharField(max_length=50)),
                ('total', models.CharField(default=0, max_length=50)),
                ('jobpost', models.ManyToManyField(blank=True, default=None, to='app.JobPost')),
                ('manager', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-total'],
            },
        ),
    ]
