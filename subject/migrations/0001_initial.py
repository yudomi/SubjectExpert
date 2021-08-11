# Generated by Django 3.2.5 on 2021-08-11 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kmooc',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('link', models.URLField(verbose_name='link')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('image', models.ImageField(upload_to='moocs', verbose_name='image')),
                ('midclassify', models.CharField(max_length=255, verbose_name='midclassify')),
                ('level', models.CharField(max_length=255, verbose_name='level')),
            ],
        ),
        migrations.CreateModel(
            name='RecommendSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('series_num', models.CharField(max_length=255, verbose_name='series_num')),
                ('num', models.IntegerField(verbose_name='num')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('professor', models.CharField(blank=True, max_length=255, verbose_name='professor')),
                ('department', models.CharField(blank=True, max_length=255, verbose_name='department')),
                ('category', models.CharField(blank=True, max_length=255, verbose_name='category')),
                ('grade', models.IntegerField(blank=True, verbose_name='grade')),
                ('words_5', models.CharField(blank=True, max_length=255, verbose_name='words')),
                ('keywords_3', models.CharField(blank=True, max_length=255, verbose_name='keywords')),
                ('year', models.IntegerField(choices=[(2020, '2020년'), (2021, '2021년')], verbose_name='year')),
                ('semester', models.CharField(choices=[('1R', '1학기'), ('2R', '2학기')], max_length=20, verbose_name='semester')),
                ('tags', models.CharField(blank=True, max_length=255, verbose_name='tags')),
                ('words', models.TextField(blank=True, verbose_name='words')),
                ('recommend_subjects', models.ManyToManyField(through='subject.RecommendSubject', to='subject.Subject')),
            ],
            options={
                'ordering': ('num',),
            },
        ),
        migrations.CreateModel(
            name='SubjectKmooc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kmooc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_kmoocs', to='subject.kmooc')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_kmoocs', to='subject.subject')),
            ],
        ),
        migrations.AddField(
            model_name='recommendsubject',
            name='recommend_subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='subject.subject'),
        ),
        migrations.AddField(
            model_name='recommendsubject',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recommend_subjects_rel', to='subject.subject'),
        ),
        migrations.AddField(
            model_name='kmooc',
            name='subject_ids',
            field=models.ManyToManyField(blank=True, related_name='sub_moocs', through='subject.SubjectKmooc', to='subject.Subject'),
        ),
    ]
