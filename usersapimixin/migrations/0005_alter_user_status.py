# Generated by Django 5.0.3 on 2024-03-08 16:58

import django_enumfield.db.fields
import usersapimixin.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usersapimixin', '0004_alter_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=django_enumfield.db.fields.EnumField(default=1, enum=usersapimixin.models.Status),
        ),
    ]
