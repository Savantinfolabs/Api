from django.db import models
from user.models import CustomUser
# Create your models here.
class Amount(models.Model):  
    user = models.ForeignKey(CustomUser, related_name='user', blank=True, on_delete=models.CASCADE)
    # user_Amount_list = models.ForeignKey('Amount_list', blank=True, on_delete=models.DO_NOTHING)
    Total_fees=models.IntegerField(blank=True,null=True)
    Remaining_fees=models.IntegerField(blank=True,null=True)
    Paid_fees=models.IntegerField(blank=True,null=True,)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    # def save(self, *args, **kwargs):
    #         self.Remaining_fees = self.Total_fees - self.Paid_fees
    #         super(Amount, self).save(*args, **kwargs)    

    def __str__(self):
        return self.user.username.upper()

class Amount_list(models.Model):
    user_Amount_list = models.ForeignKey(Amount, blank=True, on_delete=models.CASCADE)
    Paid_To = models.CharField(max_length = 50, blank = True, null = True, unique = True)
    Paid_fees=models.IntegerField(blank=True,null=True,)
    # def save(self, *args, **kwargs):
    #         sum=0
    #         for Paid_fees in Paid_fees:
    #           self.Paid_fees += self.Paid_fees
    #         super(Amount_list, self).save(*args, **kwargs)   

    def __str__(self):
        return "{}".format(self.user_Amount_list.user.username.upper())


