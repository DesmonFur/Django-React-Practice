from django.db import migrations
from rest_framework import serializers
from .models import Student

# class StudentSerializer(serializers.ModelSerializer):

# class Meta:
# model = Student
# fields = [‘name’, ’email’, ‘document’, ‘phone’, ‘registrationDate’]

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields =['name', 'email', 'document', 'phone', 'registrationDate']
# class Migration(migrations.Migration):

#     dependencies = [
#         ('xenoproshowcased', '0001_initial'),
#     ]

#     operations = [
#         migrations.RunPython(create_data),
#     ]