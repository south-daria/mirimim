# Generated by Django 3.0.8 on 2020-07-20 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_assignment_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='attend',
            name='teacher',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
