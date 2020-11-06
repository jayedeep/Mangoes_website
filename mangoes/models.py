from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from PIL import Image

class CustomUser(AbstractUser):
    profile_pic=models.ImageField(upload_to="images",default="user-thumb.jpg")
    email = models.EmailField(_('email address'), unique=True)
    contact=models.CharField(max_length=12)
    address=models.TextField(max_length=200)
    farm_name=models.CharField(max_length=100)

    def __str__(self):
        return self.username
    
    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)

        # img=Image.open(self.profile_pic.path)

        # if img.height >300 or img.width>300:
        #     output_size=(300,300)
        #     img.thumbnail(output_size)
        #     img.save(self.profile_pic.path)

class Mango_For_Sell(models.Model):
    m=(
        ('A','A'),
        ('B','B'),
        ('C','C'),
    )
    w=(
        ('5','5'),
        ('10','10')
    )
    yorn=(
        ('yes','yes'),
        ('no','no'),
    )
    owner=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    Type_Of_Mango=models.CharField(max_length=20,choices=m,default='A')
    weigth=models.CharField(max_length=10,choices=w,default='5')
    ripe=models.CharField(max_length=10,choices=yorn,default='no')
    pkgd_at=models.DateTimeField(default=timezone.now)
    photo1=models.ImageField(upload_to="photos")
    photo2=models.ImageField(upload_to="photos")
    photo3=models.ImageField(upload_to="photos")
    photo4=models.ImageField(upload_to="photos")
    photo5=models.ImageField(upload_to="photos")
    photo6=models.ImageField(upload_to="photos")
    price=models.IntegerField(default=300)
    total_boxes=models.IntegerField()
    limit=models.IntegerField(default=25)
    discount=models.IntegerField(default=0)

    def __str__(self):
        return self.owner.username+"'s "+self.Type_Of_Mango

class Mangoes_For_Buy(models.Model):
    owner=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    Qty=models.IntegerField()
    mangoes_of=models.ForeignKey(Mango_For_Sell,on_delete=models.CASCADE)
    total_bill=models.IntegerField()
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Buyer: "+self.owner.username+" "+"seler: "+self.mangoes_of.owner.username 

class Deliver(models.Model):
    yorn=(
        ('yes','yes'),
        ('no','no'),
    )
    owner_of_product=models.ForeignKey(Mango_For_Sell,on_delete=models.CASCADE)
    product=models.ForeignKey(Mangoes_For_Buy,on_delete=models.CASCADE)
    diliverd=models.CharField(max_length=10,choices=yorn,default='no')
    delivery_at=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return "Buyer:"+self.product.owner.username+" "+"seller"+self.product.mangoes_of.owner.username
    
