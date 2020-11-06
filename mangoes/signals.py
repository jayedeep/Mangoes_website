from django.db.models.signals import post_save
from .models import Mangoes_For_Buy
from django.dispatch import receiver
from .models import Deliver,Mango_For_Sell
from django.utils import timezone


@receiver(post_save,sender=Mangoes_For_Buy)
def create_deliver(sender,instance,created,**kwargs):
    if created:
        Deliver.objects.create(owner_of_product=instance.mangoes_of,product=instance,diliverd='no',delivery_at=timezone.now())
        mangoes=Mango_For_Sell.objects.get(id=instance.mangoes_of.id)
        mangoes.total_boxes=mangoes.total_boxes-instance.Qty
        mangoes.save()



@receiver(post_save,sender=Mangoes_For_Buy)
def save_deliver(sender,instance,created,**kwargs):
    # instance.deliver.save()
    print("this is saved")

