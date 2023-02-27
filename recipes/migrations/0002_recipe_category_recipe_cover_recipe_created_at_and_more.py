# Generated by Django 4.1.5 on 2023-02-27 13:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recipes.category'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cover',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='recipes/covers/%Y/%m/%d/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.CharField(default='-', max_length=165),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recipe',
            name='preparation_steps',
            field=models.TextField(default='-'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='preparation_steps_is_html',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recipe',
            name='preparation_time',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='preparation_time_unit',
            field=models.CharField(default=' ', max_length=65),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='servings',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='servings_unit',
            field=models.CharField(default=' ', max_length=65),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recipe',
            name='title',
            field=models.CharField(default='', max_length=65),
            preserve_default=False,
        ),
    ]
