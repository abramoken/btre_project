# Generated by Django 2.1.1 on 2022-06-22 22:55

from django.db import migrations, models
import realtors.validators


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_auto_20220622_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=models.FileField(upload_to='photos/%Y/%m/%d/', validators=[realtors.validators.validate_file_size]),
        ),
    ]
