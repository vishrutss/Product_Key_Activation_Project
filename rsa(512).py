import binascii
 
n = 10856794111655472080085892127922388594107493469326643544653694747956504491185680623705457442282422518531269442760246982336168229529060164239779487511701433    # p*q = modulus
e = 65537
d = 725420776278122468814503587716437121833417976138385523933633356749645744646553542842287733551026055447811437731265090240047157077905633026914411783852749
 
#message="703084636222302833"
#print('message                 ', message)
 
#hex_data   = binascii.hexlify(message.encode())
#print('hex data                ', hex_data)
 
plain_text =9281472211341752261340201051684212121147221134175226134020105161546237035106531608040201051672211341752261340201051605161928147221134175226134020105160
#int(hex_data, 16)
print('plain text integer      ', plain_text)
 
if plain_text > n:
  raise Exception('plain text too large for key')
 
encrypted_text = pow(plain_text, e, n)
print('\nencrypted text integer  ', encrypted_text)
 
decrypted_text = pow(encrypted_text, d, n)
print('\ndecrypted text integer  ', decrypted_text)
 
#print('message                 ', binascii.unhexlify(hex(decrypted_text)[2:]).decode())     # [2:] slicing, to strip the 0x part 
