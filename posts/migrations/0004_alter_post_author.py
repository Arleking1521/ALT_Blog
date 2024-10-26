# Generated by Django 5.1.2 on 2024-10-26 05:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logReg', '0001_initial'),
        ('posts', '0003_rename_post_id_post_attachments_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logReg.customuser', verbose_name='Автор'),
        ),
    ]
