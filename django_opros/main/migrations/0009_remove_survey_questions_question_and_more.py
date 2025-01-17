# Generated by Django 5.1.2 on 2024-12-15 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_responses_interiew_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey_questions',
            name='question',
        ),
        migrations.RemoveField(
            model_name='survey_questions',
            name='survey',
        ),
        migrations.RemoveField(
            model_name='responses',
            name='survey_question',
        ),
        migrations.RemoveField(
            model_name='responses',
            name='answer',
        ),
        migrations.AddField(
            model_name='questions',
            name='survey',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='main.survey'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='description',
            field=models.TextField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='responses',
            name='survey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='main.survey'),
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Ответ (для открытых вопросов)')),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='main.questions')),
                ('responses', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='main.responses')),
            ],
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=255)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='main.questions')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerSelections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selections', to='main.answers', verbose_name='Ответ')),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selections', to='main.options', verbose_name='Выбранный вариант')),
            ],
        ),
        migrations.AddField(
            model_name='answers',
            name='option',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='main.options', verbose_name='Выбранный вариант'),
        ),
        migrations.DeleteModel(
            name='Answer_Options',
        ),
        migrations.DeleteModel(
            name='Survey_Questions',
        ),
    ]
