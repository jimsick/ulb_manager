from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    (True, '正常'),
    (False, '报警'),
    )


class Company(models.Model):
    company_id = models.PositiveSmallIntegerField(verbose_name='公交公司ID', unique=True)
    company_name = models.CharField('公司名称', max_length=50)
    company_server = models.CharField('公司服务器地址', max_length=25, blank=True, null=True)
    company_report_list = models.SmallIntegerField('服务器列表', default=0, blank=True, null=True)
    create_user = models.CharField('创建人', max_length=20, blank=True, null=True)
    create_user_id = models.CharField('创建人ID', max_length=20, blank=True, null=True)
    # owner = models.ForeignKey(User, related_name='company_create_user', on_delete=models.CASCADE)

    def __str__(self):
        return "%s:%s" % (self.company_id, self.company_name)

    # class Meta:
    #     # db_table = 'BusCompanyInfoTable'
    #     verbose_name = u'公交公司信息表'


class Bus(models.Model):
    bus_id = models.CharField(max_length=25, verbose_name='公交车ID', unique=True)
    company = models.ForeignKey(Company, related_name='company', on_delete=models.CASCADE, verbose_name='公交公司ID')
    bus_license_plate = models.CharField('公交车牌号', max_length=25)
    bus_line = models.CharField('公交线路号', max_length=25, blank=True, null=True)
    bus_state = models.BooleanField('公交车状态', choices=STATUS_CHOICES, default=False)
    bus_locate = models.CharField('公交车位置', max_length=20, blank=True, null=True)
    create_user_id = models.CharField('创建人ID', max_length=20, blank=True, null=True)
    create_user = models.CharField('创建人', max_length=20, blank=True, null=True)
    # owner = models.ForeignKey(User, related_name='bus_create_user', on_delete=models.CASCADE)

    def __str__(self):
        return "%s:%s" % (self.bus_id, self.bus_license_plate)

    # class Meta:
    #     # db_table = 'BusInfoTable'
    #     verbose_name = u'车辆信息表'


class Alarm(models.Model):
    bus = models.ForeignKey(Bus, related_name='alarm_bus',on_delete=models.CASCADE, verbose_name='公交车ID')
    alarm_time = models.DateTimeField('报警时间')
    alarm_locate = models.CharField('报警位置信息', max_length=20)
    # owner = models.ForeignKey(User, related_name='alarms_create_user', on_delete=models.CASCADE)
    create_user_id = models.CharField('创建人ID', max_length=20, blank=True, null=True)
    create_user = models.CharField('创建人', max_length=20, blank=True, null=True)

    def __str__(self):
        return "公交车牌号:%s" % self.Bus.bus_license_plate

    # class Meta:
        # db_table = 'AlarMinFoTable'
        # verbose_name = u'报警信息表'

