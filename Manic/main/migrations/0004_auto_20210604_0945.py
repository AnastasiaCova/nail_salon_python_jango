# Generated by Django 3.1.2 on 2021-06-04 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210604_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pricelist',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='orderpricelist', to='main.pricelist'),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='pricelist',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='reviewpricelist', to='main.pricelist'),
        ),
    ]
