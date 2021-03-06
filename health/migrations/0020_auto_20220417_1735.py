# Generated by Django 3.1.6 on 2022-04-17 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0019_prescription_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital_appointment',
            name='bed_no',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Help_Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed_number', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, default='Pending', max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('helper_doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health.doctor')),
                ('hospital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health.hospital')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='health.patient')),
            ],
        ),
    ]
