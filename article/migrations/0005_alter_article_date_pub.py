# Generated by Django 3.2.5 on 2021-07-26 01:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_alter_article_date_pub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_pub',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date publication'),
        ),
    ]
