from django.db import models
from django.contrib.auth.models import User


class Users_task(models.Model):
    '''
    This class discribes users task.
    '''
    STATUS = (
        ('finished', 'task are finished'),
        ('compliting', 'compliting my task')
    )

    NOTIFICATE_AT = (
        ('don`t notificate', 'don`t notificate'),
        ('one hour', 'notificate me at one hour'),
        ('two hours', 'notificate me at two hours'),
        ('four hours', 'notificate me at four hours'),
        ('eight hours', 'notificate me at eight hour'),
    )

    title = models.CharField(
        verbose_name='title', max_length=255
    )
    discription = models.CharField(
        verbose_name='discription', max_length=1024
    )
    status = models.CharField(
        max_length=255,
        choices=STATUS,
        default='compliting...'
    )
    created_at = models.DateField(auto_now_add=True)
    notification = models.CharField(
        max_length=255, 
        choices=NOTIFICATE_AT,
        default='don`t notificate'
    )

class Users_tasks_broker(models.Model):
    '''
    This model works like classic broker in the m2m 
    model
    '''
    user_id = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name='user_id',
    )
    task_id = models.ForeignKey(
        Users_task,
        on_delete=models.PROTECT,
        verbose_name='task_id',
    )