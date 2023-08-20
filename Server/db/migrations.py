from django.db import models, migrations

class Migrations(migrations.Migration):
    dependencies = [

    ]

    operations = [
        migrations.CreateModel(
            name='AadharWalletMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name = 'ID')),
                ('aadhar_id', models.CharField(max_length=16, unique=True)),
                ('wallet_address', models.CharField(max_length=42)),
                ('encrypted_private_key', models.TextField(blank= True, null=True))
            ],
        ),
    ]