# Generated by Django 4.2.2 on 2023-06-14 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "app_funcionarios",
            "0003_funcionarios_estadocivil_funcionarios_setor_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="funcionarios",
            name="email",
            field=models.CharField(
                default="teste@gmail.com", max_length=100, verbose_name="Email"
            ),
            preserve_default=False,
        ),
    ]