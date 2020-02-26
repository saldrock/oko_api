from django.contrib.auth.models import Userfrom django.db import modelsfrom django.core.validators import MaxValueValidator, MinValueValidatorclass Room(models.Model):    name = models.CharField(max_length=36)  # name of the room    #description = models.TextField(max_length=360) #descirption of the roomclass DataType(models.Model):    room = models.ForeignKey(Room, on_delete=models.CASCADE)    TYPES_OF_DATA = (        ('Hum', 'Humidity'),        ('Tem', 'Tempurature'),        ('Co2',  'Co2 Level'),    )    type = models.CharField(max_length=3, choices=TYPES_OF_DATA)    class Meta:        unique_together = (('room','type'),) # room and type mustent already exist        index_together = (('room', 'type'),)class TimePeriod(models.Model):    room = models.ForeignKey(Room, on_delete=models.CASCADE)    data = models.ForeignKey(DataType, on_delete=models.CASCADE)    TIME_CHOICE = (        ('1hr', 'The Last Hour'),        ('1d', '1 day Ago'),        ('3d', '3 days Ago '),        ('1w', '1 week ago'),    )    time = models.CharField(max_length=3, choices=TIME_CHOICE)    class Meta:        unique_together = (('room','data'),) # room and data mustent already exist        index_together = (('room', 'data'),)