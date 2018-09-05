# Generated by Django 2.1.1 on 2018-09-05 06:24

from django.db import migrations
import djongo.models.fields
import testapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('blog', djongo.models.fields.EmbeddedModelField(model_container=testapp.models.NewBlog, null=True)),
            ],
        ),
    ]
