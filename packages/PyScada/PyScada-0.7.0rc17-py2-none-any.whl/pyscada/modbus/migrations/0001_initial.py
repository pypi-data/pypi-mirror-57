# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyscada', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModbusClient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('protocol', models.PositiveSmallIntegerField(default=0, choices=[(0, 'TCP'), (1, 'UDP'), (2, 'serial ASCII'), (3, 'serial RTU')])),
                ('ip_address', models.GenericIPAddressField(default='127.0.0.1')),
                ('port', models.CharField(default='502', help_text='for TCP and UDP enter network port as number (def. 502, for serial ASCII and RTU enter serial port (/dev/pts/13))', max_length=400)),
                ('unit_id', models.PositiveSmallIntegerField(default=0)),
                ('modbus_client', models.OneToOneField(to='pyscada.Client', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ModbusVariable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.PositiveIntegerField()),
                ('function_code_read', models.PositiveSmallIntegerField(default=0, help_text=b'', choices=[(0, 'not selected'), (1, 'coils (FC1)'), (2, 'discrete inputs (FC2)'), (3, 'holding registers (FC3)'), (4, 'input registers (FC4)')])),
                ('modbus_variable', models.OneToOneField(to='pyscada.Variable', on_delete=models.CASCADE)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
