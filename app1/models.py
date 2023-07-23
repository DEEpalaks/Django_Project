from django.db import models
item=(('1','OIL'),('2','Grocerey'),('3','Cosmetics'))
class app1(models.Model):
    Name=models.CharField(max_length=20)
    Item=models.CharField(max_length=20,choices=item,default='OIL')
    Quantity=models.IntegerField()
    Rate=models.IntegerField()
    Amount=models.IntegerField()
def _str_(self):
    return self.Item
# Create your models here.
