# Generated by Django 5.0.4 on 2024-04-16 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_book_fine_book_issue_date_book_return_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='returened_date',
            field=models.DateField(null=True),
        ),
    ]
