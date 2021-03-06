# Generated by Django 2.1.5 on 2019-02-11 15:05
from django.conf import settings
from django.db import migrations, models


def foward_func(apps, schema_editor):
    # 현재 유저에 대해서 Profile을 만들어준다.
    auth_user_model = settings.AUTH_USER_MODEL.split('.')
    User = apps.get_model(*auth_user_model);
    Profile = apps.get_model('accounts', 'Profile')

    for user in User.objects.all():
        print('create profile for user#{}'.format(user.pk))
        Profile.objects.create(user=user)
    pass


def backward_func(apps, schema_editor):
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20190208_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True),
        ),

        migrations.RunPython(foward_func, backward_func),
    ]
