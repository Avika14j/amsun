# Generated by Django 3.1.6 on 2022-04-18 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('health', '0020_auto_20220417_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100, null=True)),
                ('days_time', models.CharField(max_length=100, null=True)),
                ('timing', models.CharField(max_length=100, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('foundation_date', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('experience', models.CharField(max_length=100, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis_Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, default='Pending', max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('test_type', models.CharField(blank=True, max_length=100, null=True)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('diagnosis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health.diagnosis')),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health.doctor')),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health.hospital')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health.patient')),
            ],
        ),
    ]