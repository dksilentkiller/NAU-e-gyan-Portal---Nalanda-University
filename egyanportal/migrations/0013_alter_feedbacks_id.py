# Generated by Django 5.1 on 2024-09-01 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('egyanportal', '0012_alter_noti_notdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbacks',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]