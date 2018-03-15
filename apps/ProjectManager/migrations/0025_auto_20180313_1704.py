# Generated by Django 2.0.2 on 2018-03-13 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManager', '0024_auto_20180309_0918'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InceptionSqlOperateRecord',
        ),
        migrations.AlterModelOptions(
            name='inceptionhostconfig',
            options={'default_permissions': (), 'verbose_name': 'Inception数据库账号配置', 'verbose_name_plural': 'Inception数据库账号配置'},
        ),
        migrations.AlterField(
            model_name='incepmakeexectask',
            name='exec_status',
            field=models.CharField(choices=[('0', '未执行'), ('1', '已完成'), ('2', '处理中')], default='0', max_length=10, verbose_name='执行进度'),
        ),
    ]