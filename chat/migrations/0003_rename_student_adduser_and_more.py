# Generated by Django 4.2.4 on 2023-12-05 17:20

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0002_student_studentprofile"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Student",
            new_name="AddUser",
        ),
        migrations.RenameModel(
            old_name="StudentProfile",
            new_name="AddUserProfile",
        ),
        migrations.AlterModelManagers(
            name="adduser",
            managers=[
                ("user", django.db.models.manager.Manager()),
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[("ADMIN", "Admin"), ("USER", "User")], max_length=100
            ),
        ),
    ]
