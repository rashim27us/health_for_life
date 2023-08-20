from django.db import models

class AadharWalletMapping(models.Model):
    aadhar_id = models.CharField(max_length= 16, unique= True)
    wallet_address = models.CharField(max_length= 42)
    encrypted_private_key = models.TextField(blank= True, null= True)

def __str__(self):
    return self.aadhar_id