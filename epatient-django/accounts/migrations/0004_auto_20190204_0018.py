# Generated by Django 2.1.5 on 2019-02-04 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190204_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='practice',
            field=models.CharField(default='', max_length=254, null=True),
        ),
    ]