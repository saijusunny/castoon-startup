# Generated by Django 4.0.2 on 2023-07-11 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CastoonnApp', '0003_contest_casting_call_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
