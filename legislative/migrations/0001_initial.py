# Generated by Django 5.0.3 on 2024-03-17 11:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('primary_sponsor', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Legislator',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legislative.bill')),
            ],
        ),
        migrations.CreateModel(
            name='VoteResult',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('vote_type', models.IntegerField()),
                ('legislator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legislative.legislator')),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legislative.vote')),
            ],
        ),
    ]
