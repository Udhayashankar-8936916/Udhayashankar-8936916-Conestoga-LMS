# Generated by Django 5.0.4 on 2024-04-16 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_book_fine_book_issue_date_book_return_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='fine',
        ),
        migrations.RemoveField(
            model_name='book',
            name='issue_date',
        ),
        migrations.RemoveField(
            model_name='book',
            name='return_date',
        ),
    ]
