import re,uuid
import math

print("The MAC address :",end="")
print(':'.join(re.findall('..','%012x' %uuid.getnode())))
mac=(':'.join(re.findall('..','%012x' %uuid.getnode())))
#mac='b8:ca:3a:d5:eb:53'

#8002281480558766684

def mac_to_int(mac):
    res = re.match('^((?:(?:[0-9a-f]{2}):){5}[0-9a-f]{2})$', mac.lower())
    if res is None:
        raise ValueError('invalid mac address')
    return int(res.group(0).replace(':', ''), 16)

a=mac_to_int(mac)
#print(a)


def serial():
    ser=""
    for x in mac:
        if x.isdigit():
            q=collatz(x)
            ser+=q
        elif x=="a":
            q=collatz(10)
            ser+=q
        elif x=="b":
            q=collatz(11)
            ser+=q
        elif x=="c":
            q=collatz(12)
            ser+=q
        elif x=="d":
            q=collatz(13)
            ser+=q
        elif x=="e":
            q=collatz(14)
            ser+=q
        elif x=="f":
            q=collatz(15)
            ser+=q
        
    return ser


def collatz(n):
    ser=""
    ser+=str(n)
    while int(n)>1:
        if n==16:
                break
        else:
            if (int(n) % 2):
                # n is odd
                n = 3*int(n) + 1
                ser+=str(n)
            else:
                # n is even
                n = int(int(n)/2)
                ser+=str(n)
    return ser

def GenerateKey(key):
    n1=83838793906163188026
    #alist=[]
    #blist=[]
    #k=''
    #j=0
    #for i in str(key):
        #alist.append(i)
    #while j<(len(alist)-1):
        #blist.append(abs(int(alist[j])-int(alist[j+1])))
        #j+=2
    #for i in blist:
        #k=k+str(i)
    #q=int(math.sqrt(int(k)))
    pk = pow(int(key), e, n1)
    return pk


n = 16322248854717185868693137444495017222610798110677101243225786420994899969921561034075424089437502357991087257430903364024757168516523496869928155396275643260667735473894075577715049469423705610827028161701230735567521786117490700888799431608420644084015132882892157658260795560746254790116228753500399156147637929103209122490458064178105461436152306552566578484867003564330185757888538224787046808839419211762739480786934501781049898983855824827967500746030384039265771639028825554303122452586469835716887796068188272905701857421380928928102812738387458260411424089417611886165533436506093271526271970992037067020231    # p*q = modulus
e = 65537
d = 11813625160972503997674447740088448463269917719484529660667591636685720816840247891882961781259112972045550345132939716025303744929013771617989412439796433502090626126748120618175010399204175533575983853733557817887755442005234507315856878387991895135285011721120994344598357822732774611507594102469413210441342223196871676425376538611680207192950699886611553226441703865411492948411156193241887898345831243727377320387769109486590452092242500774568706908757554223437599595996209830838691672911264337361322310053978799074403963842126541233649541873288603307609417065755459530137423053184869732967810517188449422981121 
#message="703084636222302833"
#print('message                 ', message)
 
#hex_data   = binascii.hexlify(message.encode())
#print('hex data                ', hex_data)

z=int(serial())
print("\n\nserial key: ",z)
plain_text =z
#int(hex_data, 16)
#print('plain text integer      ', plain_text)
 
if plain_text > n:
  raise Exception('plain text too large for key')
 
encrypted_text = pow(plain_text, e, n)
print('\nencrypted text integer  ', encrypted_text)
######################################################################################################





 
decrypted_text = pow(encrypted_text, d, n)
print('\ndecrypted text integer  ', decrypted_text)
 
#print('message                 ', binascii.unhexlify(hex(decrypted_text)[2:]).decode())     # [2:] slicing, to strip the 0x part 



print("\nServer side")
#f=int(input("Serial key: "))
k=GenerateKey(int(decrypted_text))
print("Product key: ",k)


encrypted_pk=pow(k, e, n)
print('\nencrypted product key  ', encrypted_pk)

decrypted_pk = pow(encrypted_pk, d, n)
print('\ndecrypted text integer  ', decrypted_pk)

print("\nClient side ")
i=int(input("Please enter the product key: "))
k2=GenerateKey(z);
if k2==i:
        print("Product activated")
else:
        print("Invalid product key")

