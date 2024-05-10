# Generated by Django 4.2.6 on 2024-05-10 01:42

from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('paper_review', '0003_alter_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostMonthlyPseudorec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('content', markdownx.models.MarkdownxField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
