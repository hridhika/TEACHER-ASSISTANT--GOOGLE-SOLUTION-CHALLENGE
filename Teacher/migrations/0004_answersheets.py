# Generated by Django 5.2 on 2025-04-06 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teacher', '0003_markingscheme'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerSheets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answersheetpic', models.ImageField(upload_to='')),
                ('studentname', models.CharField(max_length=50)),
                ('studentroll', models.CharField(max_length=10)),
                ('ownerexam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answersheet', to='Teacher.exam')),
                ('ownermarkingscheme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answersheet', to='Teacher.markingscheme')),
            ],
        ),
    ]
