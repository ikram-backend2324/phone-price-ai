from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Phone Brand',
                'verbose_name_plural': 'Phone Brands',
            },
        ),
        migrations.CreateModel(
            name='PhoneInspection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='phones/')),
                ('condition', models.CharField(
                    choices=[('new', 'New / Like New'), ('good', 'Good'), ('fair', 'Fair'), ('poor', 'Poor')],
                    default='good', max_length=10
                )),
                ('result', models.TextField(blank=True)),
                ('price_min', models.IntegerField(default=0)),
                ('price_max', models.IntegerField(default=0)),
                ('confidence', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Phone Inspection',
                'verbose_name_plural': 'Phone Inspections',
                'ordering': ['-created_at'],
            },
        ),
    ]
