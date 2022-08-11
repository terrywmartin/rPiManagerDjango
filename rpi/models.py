from django.db import models

# Create your models here.
class RaspberryPiModel(models.Model):
    name = models.CharField(max_length=50,null=False,blank=False)

    def __str__(self):
        return self.name

class Location(models.Model):
    OPTIONS = (
        ('AL','Alabama'),
        ('AK','Alaska'),
        ('AZ','Arizona'),
        ('AR','Arkansas'),
        ('CA','California'),
        ('CO','Colorado'),
        ('CT','Connecticut'),
        ('DE','Delaware'),
        ('DC','District of Columbia'),
        ('FL','Florida'),
        ('GA','Georgia'),
        ('HI','Hawaii'),
        ('ID','Idaho'),
        ('IL','Illinois'),
        ('IN','Indiana'),
        ('IA','Iowa'),
        ('KS','Kansas'),
        ('KY','Kentucky'),
        ('LA','Louisiana'),
        ('ME','Maine'),
        ('MD','Maryland'),
        ('MA','Massachusetts'),
        ('MI','Michigan'),
        ('MN','Minnesota'),
        ('MS','Mississippi'),
        ('MO','Missouri'),
        ('MT','Montana'),
        ('NE','Nebraska'),
        ('NV','Nevada'),
        ('NH','New Hampshire'),
        ('NJ','New Jersey'),
        ('NM','New Mexico'),
        ('NY','New York'),
        ('NC','North Carolina'),
        ('ND','North Dakota'),
        ('OH','Ohio'),
        ('OK','Oklahoma'),
        ('OR','Oregon'),
        ('PA','Pennsylvania'),
        ('PR','Puerto Rico'),
        ('RI','Rhode Island'),
        ('SC','South Carolina'),
        ('SD','South Dakota'),
        ('TN','Tennessee'),
        ('TX','Texas'),
        ('UT','Utah'),
        ('VT','Vermont'),
        ('VA','Virginia'),
        ('VI','Virgin Islands'),
        ('WA','Washington'),
        ('WV','West Virginia'),
        ('WI','Wisconsin'),
        ('WY','Wyoming'),
    )

    name = models.CharField(max_length=150,blank=False,null=False)
    address1 = models.CharField(max_length=500,blank=True,null=True)
    address2 = models.CharField(max_length=500,blank=True,null=True)
    city = models.CharField(max_length=50,blank=True,null=True)
    state = models.CharField(choices=OPTIONS, max_length=75)
    zip = models.CharField(max_length=10,blank=True,null=True)

    def __str__(self):
        return self.name

class RaspberryPi(models.Model):
    name = models.CharField(max_length=50,blank =False,null=False)
    serial_number = models.CharField(max_length=250,blank=True,null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True,blank=True)
    checked_in = models.DateTimeField(null=True, blank = True)
    connect = models.BooleanField(default = False)
    date_deployed = models.DateTimeField(null=True, blank = True)
    deployed = models.BooleanField(default = False)
    model = models.ForeignKey(RaspberryPiModel,on_delete=models.SET_NULL,null=True,blank=True)
    ip_address = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class RaspberryPiSettings(models.Model):
    tab_switch_delay = models.SmallIntegerField(default=10)
    raspberry_pi = models.ForeignKey(RaspberryPi,on_delete=models.CASCADE)

class RaspberryPiURLs(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False)
    url = models.CharField(max_length=250,blank = True, null=True)
    raspberry_pi_setting = models.ForeignKey(RaspberryPiSettings,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

""" class RaspberryPiLocation(models.Model):
    rpi = models.ForeignKey(RaspberryPi,on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    deployed = models.DateTimeField()
    checked_in = models.DateTimeField()

    def __str__(self):
        return self.rpi.name
 """


