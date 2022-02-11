# Generated by Django 3.0.8 on 2020-07-18 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('assignment_id', models.AutoField(primary_key=True, serialize=False)),
                ('classroom_id', models.IntegerField(default=-1)),
                ('notice_id', models.IntegerField(default=-1)),
                ('s_id', models.CharField(max_length=10, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('title', models.CharField(max_length=50, null=True)),
                ('content', models.TextField(max_length=500, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('classroom_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50, null=True)),
                ('teacher', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('file_id', models.AutoField(primary_key=True, serialize=False)),
                ('obj_code', models.BooleanField(default=False)),
                ('obj_id', models.IntegerField()),
                ('file_url', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('notice_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50, null=True)),
                ('s_id', models.CharField(max_length=10, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('title', models.CharField(max_length=50, null=True)),
                ('content', models.TextField(max_length=500, null=True)),
                ('scope', models.IntegerField(blank=True, default=-1)),
                ('submit_at', models.DateTimeField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj_code', models.IntegerField()),
                ('obj_name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('s_id', models.CharField(max_length=10, null=True)),
                ('password', models.CharField(max_length=255, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]