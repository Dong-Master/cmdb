# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='接口名称', max_length=32)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='接口描述')),
                ('doc', models.CharField(verbose_name='接口文档', max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='CMDBUser',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('username', models.CharField(verbose_name='用户账号', max_length=32)),
                ('password', models.CharField(verbose_name='用户密码', max_length=32)),
                ('nickname', models.CharField(verbose_name='用户姓名', max_length=32)),
                ('phone', models.CharField(verbose_name='用户手机号', max_length=32)),
                ('email', models.EmailField(verbose_name='用户邮箱', max_length=254)),
                ('photo', models.ImageField(verbose_name='用户头像', upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Cpu',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('processor', models.CharField(null=True, max_length=32, blank=True)),
                ('vendor_id', models.CharField(null=True, max_length=32, blank=True)),
                ('cpu_family', models.CharField(null=True, max_length=32, blank=True)),
                ('model', models.CharField(null=True, max_length=32, blank=True)),
                ('model_name', models.CharField(null=True, max_length=32, blank=True)),
                ('stepping', models.CharField(null=True, max_length=32, blank=True)),
                ('microcode', models.CharField(null=True, max_length=32, blank=True)),
                ('cpu_MHz', models.CharField(null=True, max_length=32, blank=True)),
                ('cache_size', models.CharField(null=True, max_length=32, blank=True)),
                ('physical_id', models.CharField(null=True, max_length=32, blank=True)),
                ('siblings', models.CharField(null=True, max_length=32, blank=True)),
                ('core_id', models.CharField(null=True, max_length=32, blank=True)),
                ('cpu_cores', models.CharField(null=True, max_length=32, blank=True)),
                ('apicid', models.CharField(null=True, max_length=32, blank=True)),
                ('initial_apicid', models.CharField(null=True, max_length=32, blank=True)),
                ('fpu', models.CharField(null=True, max_length=32, blank=True)),
                ('fpu_exception', models.CharField(null=True, max_length=32, blank=True)),
                ('cpuid_level', models.CharField(null=True, max_length=32, blank=True)),
                ('wp', models.CharField(null=True, max_length=32, blank=True)),
                ('flags', models.TextField(null=True, max_length=32, blank=True)),
                ('bogomips', models.CharField(null=True, max_length=32, blank=True)),
                ('clflush_size', models.CharField(null=True, max_length=32, blank=True)),
                ('cache_alignment', models.CharField(null=True, max_length=32, blank=True)),
                ('address_sizes', models.CharField(null=True, max_length=32, blank=True)),
                ('power_management', models.CharField(null=True, max_length=32, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('MemTota', models.CharField(null=True, max_length=32, blank=True)),
                ('MemFree', models.CharField(null=True, max_length=32, blank=True)),
                ('MemAvailable', models.CharField(null=True, max_length=32, blank=True)),
                ('Buffers', models.CharField(null=True, max_length=32, blank=True)),
                ('Cached', models.CharField(null=True, max_length=32, blank=True)),
                ('SwapCached', models.CharField(null=True, max_length=32, blank=True)),
                ('Active', models.CharField(null=True, max_length=32, blank=True)),
                ('Inactive', models.CharField(null=True, max_length=32, blank=True)),
                ('Active_anon', models.CharField(null=True, max_length=32, blank=True)),
                ('Inactive_anon', models.CharField(null=True, max_length=32, blank=True)),
                ('Active_file', models.CharField(null=True, max_length=32, blank=True)),
                ('Inactive_file', models.CharField(null=True, max_length=32, blank=True)),
                ('Unevictable', models.CharField(null=True, max_length=32, blank=True)),
                ('Mlocked', models.CharField(null=True, max_length=32, blank=True)),
                ('SwapTotal', models.CharField(null=True, max_length=32, blank=True)),
                ('SwapFree', models.CharField(null=True, max_length=32, blank=True)),
                ('Dirty', models.CharField(null=True, max_length=32, blank=True)),
                ('Writeback', models.CharField(null=True, max_length=32, blank=True)),
                ('AnonPages', models.CharField(null=True, max_length=32, blank=True)),
                ('Mapped', models.CharField(null=True, max_length=32, blank=True)),
                ('Shmem', models.CharField(null=True, max_length=32, blank=True)),
                ('Slab', models.CharField(null=True, max_length=32, blank=True)),
                ('SReclaimable', models.CharField(null=True, max_length=32, blank=True)),
                ('SUnreclaim', models.CharField(null=True, max_length=32, blank=True)),
                ('KernelStack', models.CharField(null=True, max_length=32, blank=True)),
                ('PageTables', models.CharField(null=True, max_length=32, blank=True)),
                ('NFS_Unstable', models.CharField(null=True, max_length=32, blank=True)),
                ('Bounce', models.CharField(null=True, max_length=32, blank=True)),
                ('WritebackTmp', models.CharField(null=True, max_length=32, blank=True)),
                ('CommitLimit', models.CharField(null=True, max_length=32, blank=True)),
                ('Committed_AS', models.CharField(null=True, max_length=32, blank=True)),
                ('VmallocTotal', models.CharField(null=True, max_length=32, blank=True)),
                ('VmallocUsed', models.CharField(null=True, max_length=32, blank=True)),
                ('VmallocChunk', models.CharField(null=True, max_length=32, blank=True)),
                ('HardwareCorrupted', models.CharField(null=True, max_length=32, blank=True)),
                ('AnonHugePages', models.CharField(null=True, max_length=32, blank=True)),
                ('HugePages_Total', models.CharField(null=True, max_length=32, blank=True)),
                ('HugePages_Free', models.CharField(null=True, max_length=32, blank=True)),
                ('HugePages_Rsvd', models.CharField(null=True, max_length=32, blank=True)),
                ('HugePages_Surp', models.CharField(null=True, max_length=32, blank=True)),
                ('Hugepagesize', models.CharField(null=True, max_length=32, blank=True)),
                ('DirectMap4k', models.CharField(null=True, max_length=32, blank=True)),
                ('DirectMap2M', models.CharField(null=True, max_length=32, blank=True)),
                ('DirectMap1G', models.CharField(null=True, max_length=32, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('ip', models.CharField(verbose_name='服务器ip', max_length=32)),
                ('mac', models.CharField(verbose_name='服务器物理地址', max_length=32)),
                ('cpu', models.CharField(verbose_name='服务器CPU', max_length=32)),
                ('memory', models.CharField(verbose_name='服务器内存', max_length=32)),
                ('isalive', models.CharField(verbose_name='服务器状态', max_length=32)),
                ('hostname', models.CharField(verbose_name='服务器名称', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Service_Cpu',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('service_id', models.IntegerField()),
                ('cpu_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Service_Memory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('service_id', models.IntegerField()),
                ('Memory_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='cmdbuser',
            name='service',
            field=models.ManyToManyField(to='Service.Service'),
        ),
    ]
