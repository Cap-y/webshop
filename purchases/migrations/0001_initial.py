# Generated by Django 3.2.5 on 2021-07-16 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('cost', models.IntegerField(default=0)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchases.item')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hireid', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=200)),
                ('items', models.ManyToManyField(through='purchases.ItemRelationship', to='purchases.Item')),
            ],
        ),
        migrations.AddField(
            model_name='itemrelationship',
            name='persons',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='purchases.person'),
        ),
    ]
