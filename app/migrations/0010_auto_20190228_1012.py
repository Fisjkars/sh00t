# Generated by Django 2.1.7 on 2019-02-28 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_screenshot'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default='')),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='MethodologyMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default='')),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ModuleMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default='')),
                ('order', models.IntegerField(default=0)),
                ('methodology', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.MethodologyMaster')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.RemoveField(
            model_name='flag',
            name='order',
        ),
        migrations.AddField(
            model_name='casemaster',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ModuleMaster'),
        ),
    ]