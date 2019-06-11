# Generated by Django 2.2.1 on 2019-06-11 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ptart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(upload_to='attachment')),
                ('hit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ptart.Hit')),
            ],
        ),
    ]
