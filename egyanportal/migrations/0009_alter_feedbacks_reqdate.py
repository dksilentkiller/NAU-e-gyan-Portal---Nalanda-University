# Generated by Django 5.1 on 2024-08-31 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egyanportal', '0008_alter_feedbacks_reqdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbacks',
            name='reqdate',
            field=models.DateTimeField(),
        ),
    ]