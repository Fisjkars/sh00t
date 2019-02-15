# Generated by Django 2.0.8 on 2019-02-15 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_template_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screenshot', models.ImageField(upload_to='screenshots')),
                ('sh0t', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Sh0t')),
            ],
        ),
    ]
