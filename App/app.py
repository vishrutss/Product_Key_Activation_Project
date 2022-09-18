import time, socket, sys
import re,uuid
import math
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

mac=(':'.join(re.findall('..','%012x' %uuid.getnode())))


    
def invalidForm():
    pop=Popup(title='Invalid Form',content=Label(text='Please fill in all inputs with valid information.'),size_hint=(None,None),size=(400,400))
    pop.open()

def invalidPkey():
    pop=Popup(title='Invalid Product key',content=Label(text='The product key you have entered is invalid.'),size_hint=(None,None),size=(400,400))
    pop.open()

def valid():
    pop=Popup(title='Product activated',content=Label(text='Thank you for purchasing the product. Your product has been activated'),size_hint=(None,None),size=(800,400))
    pop.open()
    
def mac_to_int(mac):
    res = re.match('^((?:(?:[0-9a-f]{2}):){5}[0-9a-f]{2})$', mac.lower())
    if res is None:
        raise ValueError('invalid mac address')
    return int(res.group(0).replace(':', ''), 16)

a=mac_to_int(mac)

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
    pk = pow(int(key), e, n1)
    return pk

n = 16322248854717185868693137444495017222610798110677101243225786420994899969921561034075424089437502357991087257430903364024757168516523496869928155396275643260667735473894075577715049469423705610827028161701230735567521786117490700888799431608420644084015132882892157658260795560746254790116228753500399156147637929103209122490458064178105461436152306552566578484867003564330185757888538224787046808839419211762739480786934501781049898983855824827967500746030384039265771639028825554303122452586469835716887796068188272905701857421380928928102812738387458260411424089417611886165533436506093271526271970992037067020231    # p*q = modulus
e = 65537
d = 11813625160972503997674447740088448463269917719484529660667591636685720816840247891882961781259112972045550345132939716025303744929013771617989412439796433502090626126748120618175010399204175533575983853733557817887755442005234507315856878387991895135285011721120994344598357822732774611507594102469413210441342223196871676425376538611680207192950699886611553226441703865411492948411156193241887898345831243727377320387769109486590452092242500774568706908757554223437599595996209830838691672911264337361322310053978799074403963842126541233649541873288603307609417065755459530137423053184869732967810517188449422981121 

z=int(serial())
plain_text =z
if plain_text > n:
    raise Exception('plain text too large for key')

encrypted_text = pow(plain_text, e, n)

class MainWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    
    def btn(self):
        e=self.email.text
        n=self.namee.text
        if e=="" or n=="":
            invalidForm()
        else:
            print('Client Server...')
            time.sleep(1)
            #Get the hostname, IP Address from socket and set Port
            soc = socket.socket()
            shost = socket.gethostname()
            ip = socket.gethostbyname(shost)
            #get information to connect with the server
            print(shost, '({})'.format(ip))
            server_host = ip
            print("server\'s IP address:",ip)
            name = "Client"
            port = 1234
            print('Trying to connect to the server: {}, ({})'.format(server_host, port))
            time.sleep(1)
            soc.connect((server_host, port))
            print("Connected...\n")
            soc.send(n.encode())
            server_name = soc.recv(1024)
            server_name = server_name.decode()
            print('{} has joined...'.format(server_name))

            soc.send(e.encode())

            message = str(encrypted_text)
               #if message == "[bye]":
                  #message = "Leaving the Chat room"
            soc.send(message.encode())
            print("\n")
                  #break
            #soc.send(message.encode())
            print('\nThe product key has been sent to your email')
            print("Name:", self.namee.text, "email:", self.email.text)


class SecondWindow(Screen):
    pkey = ObjectProperty(None)
    def btn(self):
        if self.pkey.text=="":
            invalidForm()
        else:
            i=int(self.pkey.text)
            z=int(serial())
            k2=GenerateKey(z);
            if k2==i:
                    valid()
            else:
                    invalidPkey()


class WindowManager(ScreenManager):
    pass
    
kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
