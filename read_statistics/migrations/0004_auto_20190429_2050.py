# Generated by Django 2.1.7 on 2019-04-29 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('read_statistics', '0003_auto_20190330_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readdetail',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='readnum',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType'),
        ),
    ]
