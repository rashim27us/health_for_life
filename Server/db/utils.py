from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from django.core.exceptions import ObjectDoesNotExist
from .models import AadharWalletMapping

import base64

class EncryptionUtils:
    def __init__(self, key: bytes):
        self.key = key

    def encrypt(self, data:str) ->str:
        cipher = AES.new(self.key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        return f'{iv}:{ct}'
    
    def decrypt(self, encrypted_data: str) -> str:
        iv, ct = encrypted_data.split(':')
        iv = base64.b64decode(iv)
        ct = base64.b64decode(ct)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        pt_bytes = unpad(cipher.decrypt(ct), AES.block_size)
        return pt_bytes.decode('utf-8')
    
class AadharWalletMapppingUtils:
    @classmethod
    def create_mapping(cls, aadhar_id, wallet_address, encrypted_private_key = None):
        mapping = AadharWalletMapping(aadhar_id= aadhar_id, wallet_address= wallet_address, encrypted_private_key= encrypted_private_key)
        mapping .save()

    @classmethod
    def get_mapping(cls, aadhar_id):
        try:
            mapping = AadharWalletMapping.objects.get(aadhar_id= aadhar_id)
            return mapping
        except ObjectDoesNotExist:
            return None