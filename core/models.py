from django.db import models

# Create your models here.
class Activenumber(models.Model):

    msisdn = models.CharField(max_length=150)
    region = models.CharField(max_length=150,null=True)
    product_code = models.CharField(max_length=150,null=True)
    distributor_code = models.CharField(max_length=150,null=True)
    dsr_code = models.CharField(max_length=150,null=True)
    retailer_code = models.CharField(max_length=150,null=True)
    activation_date = models.DateField(null=True)
    lifting_date = models.DateField(null=True)
    qcpass_date = models.DateField(null=True)
    usage_date = models.DateField(null=True)
    usage_value = models.DecimalField(max_digits=10,decimal_places=3,null=True)
    net_3g_usage_value = models.DecimalField(max_digits=10,decimal_places=3,null=True)
    net_4g_usage_value = models.DecimalField(max_digits=10,decimal_places=3,null=True)

    def __str__(self):
        return self.msisdn


class Result(models.Model):

    msisdn = models.CharField(max_length=150)
    region = models.CharField(max_length=150,null=True)
    product_code = models.CharField(max_length=150,null=True)
    distributor_code = models.CharField(max_length=150,null=True)
    dsr_code = models.CharField(max_length=150,null=True)
    retailer_code = models.CharField(max_length=150,null=True)
    activation_date = models.DateField(null=True)
    lifting_date = models.DateField(null=True)
    qcpass_date = models.DateField(null=True)
    usage_date = models.DateField(null=True)
    usage_value = models.DecimalField(max_digits=10,decimal_places=3,null=True)
    net_3g_usage_value = models.DecimalField(max_digits=10,decimal_places=3,null=True)
    net_4g_usage_value = models.DecimalField(max_digits=10,decimal_places=3,null=True)

    remarks = models.TextField(max_length=1000,null=True)

    def __str__(self):
        return self.msisdn

    