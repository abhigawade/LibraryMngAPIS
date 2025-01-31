# Generated by Django 5.0.2 on 2024-11-11 11:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Books', '0001_initial'),
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('return_date', models.DateField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Books.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.user')),
            ],
        ),
    ]
