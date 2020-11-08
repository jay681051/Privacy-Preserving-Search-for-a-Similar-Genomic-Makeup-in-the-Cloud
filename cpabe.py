from charm.schemes.abenc.abenc_bsw07 import CPabe_BSW07
group = PairingGroup('SS512')
cpabe = CPabe_BSW07(group)
def coabe_setup():
    (master_pk, master_sk) = cpabe.setup()
    pp= (master_pk, master_sk)
    return pp 

def cpabe_keygen(pp, attributes):
    mykey=cpabe.keygen(pp[0], pp[1], attributes)
    return mykey


def cpabe_encrypt(attributes, access_policy, msg):
    ciphertext = cpabe.encrypt(pp[0], msg, access_policy)
    return ciphertext

def cpabe_decrypt(master_pk, mykey, ciphertext)
    dec_msg = cpabe.decrypt(master_pk, mykey, ciphertext)
    print dec_msg