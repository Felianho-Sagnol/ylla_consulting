# Generated by Django 3.1.8 on 2021-05-03 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0060_fix_workflow_unique_constraint'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(blank=True, help_text='Lien de la page Facebook', null=True)),
                ('instagram', models.URLField(blank=True, help_text='Lien de page Instagram', null=True)),
                ('twitter', models.URLField(blank=True, help_text='Lien de la page Twitter', null=True)),
                ('youtube', models.URLField(blank=True, help_text='Lien de la page YuTube', null=True)),
                ('pinterest', models.URLField(blank=True, help_text='Lien de la page Pinterest', null=True)),
                ('linkedin', models.URLField(blank=True, help_text='Lien de la page LinkedIn', null=True)),
                ('tiktok', models.URLField(blank=True, help_text='Lien de la page TikTok', null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Résaux sociaux',
            },
        ),
        migrations.CreateModel(
            name='AddressSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(blank=True, help_text='Votre numéro de téléphone', max_length=20, null=True, verbose_name='N° Tel')),
                ('fax', models.CharField(blank=True, help_text='Nº FAX', max_length=20, null=True, verbose_name='FAX')),
                ('email', models.EmailField(blank=True, help_text='Votre adresse email', max_length=254, null=True, verbose_name='Email')),
                ('address', models.CharField(blank=True, help_text='Votre adresse', max_length=100, null=True, verbose_name='Adresse')),
                ('open_hours', models.CharField(blank=True, help_text="Heures d'ouverture", max_length=100, null=True, verbose_name="Heures d'ouverture")),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'verbose_name': 'Adresses',
            },
        ),
    ]