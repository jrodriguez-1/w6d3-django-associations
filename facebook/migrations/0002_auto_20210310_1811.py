# Generated by Django 3.1.7 on 2021-03-10 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('facebook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expression', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='PostExpression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expression', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_expressions', to='facebook.expression')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_expressions', to='facebook.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_expressions', to='facebook.user')),
            ],
        ),
        migrations.CreateModel(
            name='GenericExpression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('expression', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='g_expressions', to='facebook.expression')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='g_expressions', to='facebook.user')),
            ],
        ),
        migrations.AddConstraint(
            model_name='postexpression',
            constraint=models.UniqueConstraint(fields=('post', 'user'), name='post_user_expression'),
        ),
    ]