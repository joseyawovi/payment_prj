# Generated by Django 5.1.7 on 2025-03-17 05:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0003_alter_account_account_status_alter_kyc_gender_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="kyc",
            name="account",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="account.account",
            ),
        ),
        migrations.AlterField(
            model_name="account",
            name="account_status",
            field=models.CharField(
                choices=[("in-active", "In-ctive"), ("active", "Active")],
                default="in-active",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="kyc",
            name="gender",
            field=models.CharField(
                choices=[("male", "Male"), ("female", "Female")], max_length=40
            ),
        ),
        migrations.AlterField(
            model_name="kyc",
            name="identity_type",
            field=models.CharField(
                choices=[
                    ("international_passport", "International Passport"),
                    ("national_id_card", "National ID Card"),
                    ("driver_licence", "Driver Licence"),
                ],
                max_length=40,
            ),
        ),
        migrations.AlterField(
            model_name="kyc",
            name="marital_status",
            field=models.CharField(
                choices=[
                    ("married", "Married"),
                    ("other", "Other"),
                    ("single", "Single"),
                ],
                max_length=40,
            ),
        ),
    ]
