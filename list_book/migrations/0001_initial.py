# Generated by Django 3.0 on 2019-12-20 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('date_published', models.DateField(blank=True)),
                ('number_of_pages', models.IntegerField()),
                ('type_of_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list_book.TypeBooks')),
            ],
        ),
    ]
