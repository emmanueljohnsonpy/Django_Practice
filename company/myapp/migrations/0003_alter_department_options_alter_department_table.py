# Generated by Django 5.0.6 on 2024-07-06 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_department_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['name'], 'verbose_name_plural': 'my models'},
        ),
        migrations.AlterModelTable(
            name='department',
            table='Department',
        ),
    ]
