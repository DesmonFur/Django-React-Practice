# Generated by Django 3.0.3 on 2020-02-13 05:47

from django.db import migrations

def create_data(apps, schema_editor):
    Student = apps.get_model('xenoproshowcased', 'Student')
    Student(name="Desmond Furtick", email="desfurdev@gmail.com", document="12345678", phone="1234567891").save()

class Migration(migrations.Migration):

    dependencies = [
        ('xenoproshowcased', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
