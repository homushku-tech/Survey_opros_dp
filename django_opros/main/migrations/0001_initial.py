# Generated by Django 5.1.2 on 2024-12-12 17:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Answer_Options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_text', models.CharField(max_length=255)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.questions')),
            ],
        ),
        migrations.CreateModel(
            name='Survey_Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.questions')),
                ('survey_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.survey')),
            ],
        ),
        migrations.CreateModel(
            name='Responses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('survey_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.survey')),
                ('survey_question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.survey_questions')),
            ],
        ),
    ]