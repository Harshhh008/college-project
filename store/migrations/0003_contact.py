# Generated by Django 4.0.3 on 2022-07-31 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_orderplaced_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
    ]
