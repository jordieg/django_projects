# Generated by Django 2.1.5 on 2019-04-14 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Iso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True)),
                ('latitude', models.DecimalField(decimal_places=8, max_digits=12, null=True)),
                ('longitude', models.DecimalField(decimal_places=8, max_digits=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True)),
                ('description', models.CharField(max_length=128, null=True)),
                ('justification', models.CharField(max_length=128, null=True)),
                ('year', models.IntegerField(null=True)),
                ('area_hectares', models.DecimalField(decimal_places=5, max_digits=12, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='unesco.Category')),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, null=True)),
                ('iso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='unesco.Iso')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='unesco.Region')),
            ],
        ),
        migrations.AddField(
            model_name='site',
            name='states',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='unesco.States'),
        ),
    ]
