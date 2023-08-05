# Generated by Django 2.2.7 on 2019-11-21 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptoken', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='apptoken',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='apptoken',
            constraint=models.UniqueConstraint(
                fields=('user', 'app'),
                name='unique_app_token_and_user',
            ),
        ),
    ]
