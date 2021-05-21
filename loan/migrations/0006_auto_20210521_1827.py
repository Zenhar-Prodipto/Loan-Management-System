# Generated by Django 3.2.3 on 2021-05-21 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loan', '0005_rename_approved_by_loan_loan_approved_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loancollentionsheet',
            name='loan_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_collection_loan_id', to='loan.loan'),
        ),
        migrations.AlterField(
            model_name='loancollentionsheet',
            name='member',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='loan_collection_member_id', to='loan.loan'),
        ),
    ]