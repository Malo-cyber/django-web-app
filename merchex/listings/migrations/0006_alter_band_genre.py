# Generated by Django 4.0.4 on 2022-05-30 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_listing_band'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='genre',
            field=models.CharField(choices=[('HH', 'Hip Hop'), ('SP', 'Synth Pop'), ('AR', 'Alternative Rock'), ('TK', 'Techno'), ('FT', 'Future'), ('VR', 'Variete'), ('RP', 'Rap'), ('DB', 'Dub')], max_length=5),
        ),
    ]