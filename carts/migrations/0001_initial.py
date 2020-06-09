# Generated by Django 3.0.6 on 2020-05-29 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('Fruits', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kg', models.IntegerField()),
                ('price', models.IntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='customers.Customer')),
                ('fruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='Fruits.Fruit')),
            ],
        ),
    ]