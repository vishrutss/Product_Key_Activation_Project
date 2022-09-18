import re,uuid

print("The MAC address :",end="")
print(':'.join(re.findall('..','%012x' %uuid.getnode())))
mac=(':'.join(re.findall('..','%012x' %uuid.getnode())))

def mac_to_int(mac):
    res = re.match('^((?:(?:[0-9a-f]{2}):){5}[0-9a-f]{2})$', mac.lower())
    if res is None:
        raise ValueError('invalid mac address')
    return int(res.group(0).replace(':', ''), 16)

#a=mac_to_int(mac)
#print(a)

def GetSerial():
	sum=""
	index=1
	for x in mac:
		if x.isdigit():
			sum+=str(int(x)*(index*2))
			index+=1
		elif x=="a":
			sum+=str(10*(index*2))
			index+=1
		elif x=="b":
			sum+=str(11*(index*2))
			index+=1
		elif x=="c":
			sum+=str(12*(index*2))
			index+=1
		elif x=="d":
			sum+=str(13*(index*2))
			index+=1
		elif x=="e":
			sum+=str(14*(index*2))
			index+=1
		elif x=="f":
			sum+=str(15*(index*2))
			index+=1
	return sum


def GenerateKey(key):
	x=key;
	y=int(x*x+53/x+113*(x/4))
	return y

z=int(GetSerial())
print("Serial key: ",z)
print("\nServer side")
f=int(input("Serial key: "))
k=GenerateKey(f)
print("Product key: ",k)

print("\nClient side ")
i=int(input("Please enter the product key: "))
k2=GenerateKey(z);
if k==k2:
        print("Product activated")
else:
        print("Invalid product key")
