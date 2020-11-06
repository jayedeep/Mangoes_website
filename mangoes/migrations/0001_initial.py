# Generated by Django 3.1.2 on 2020-11-06 11:44

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('profile_pic', models.ImageField(default='user-thumb.jpg', upload_to='images')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('contact', models.CharField(max_length=12)),
                ('address', models.TextField(max_length=200)),
                ('farm_name', models.CharField(max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Mango_For_Sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type_Of_Mango', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], default='A', max_length=20)),
                ('weigth', models.CharField(choices=[('5', '5'), ('10', '10')], default='5', max_length=10)),
                ('ripe', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=10)),
                ('pkgd_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('photo1', models.ImageField(upload_to='photos')),
                ('photo2', models.ImageField(upload_to='photos')),
                ('photo3', models.ImageField(upload_to='photos')),
                ('photo4', models.ImageField(upload_to='photos')),
                ('photo5', models.ImageField(upload_to='photos')),
                ('photo6', models.ImageField(upload_to='photos')),
                ('price', models.IntegerField(default=300)),
                ('total_boxes', models.IntegerField()),
                ('limit', models.IntegerField(default=25)),
                ('discount', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mangoes_For_Buy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Qty', models.IntegerField()),
                ('total_bill', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('mangoes_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangoes.mango_for_sell')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deliver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diliverd', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=10)),
                ('delivery_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner_of_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangoes.mango_for_sell')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mangoes.mangoes_for_buy')),
            ],
        ),
    ]