# Generated by Django 3.2.4 on 2021-06-25 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('highlighter', '0002_auto_20210625_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.DeleteModel(
            name='photo',
        ),
    ]