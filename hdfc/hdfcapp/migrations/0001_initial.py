# Generated by Django 4.1.4 on 2023-02-23 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee_Details",
            fields=[
                ("EMP_ID", models.IntegerField(primary_key=True, serialize=False)),
                ("Name", models.CharField(max_length=20)),
                ("Age", models.IntegerField(null=True)),
                ("Designation", models.CharField(max_length=20)),
                ("Qualification", models.CharField(max_length=20)),
            ],
            options={"db_table": "Employee",},
        ),
    ]