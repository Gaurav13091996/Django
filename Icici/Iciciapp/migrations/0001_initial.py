# Generated by Django 4.1.4 on 2023-02-27 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee_Details",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20)),
                ("age", models.IntegerField()),
                ("designation", models.CharField(max_length=20)),
                ("doj", models.DateTimeField()),
            ],
            options={"db_table": "Employee",},
        ),
    ]
