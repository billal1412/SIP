import sys,os,readline
prompt = "\033[33;1mSIP\033[37;1m}> \033[32;1m"
def show(type,msg):
	if type=="error":
		print ("\033[33;1m{\033[31;1mERROR\033[33;1m}> \033[31;1m%s\033[0m"%(msg))
#		sys.exit()
	elif type=="sukses":
		print ("\033[33;1m{\033[32;1mSUCCESS\033[33;1m}> \033[32;1m%s\033[0m"%(msg))
	elif type=="warning":
		print ("\033[33;1m{WARNINGS}> \033[37;1m%s\033[0m"%(msg))
	elif type=="error2":
		print ("\033[33;1m{\033[31;1m%s\033[33;1m}> \033[31;1mNot found"%(msg))
try:
	import requests,socket,json
except Exception as E:
	show("error",str(E))
	sys.exit()

def banner():
	print ("""
\033[32;1m                                   _________-----_____
\033[32;1m                        _____------           __      ----_
\033[32;1m                ___----             ___------              \\
\033[32;1m                   ----________        ----                 \\
\033[32;1m                               -----__    |             _____)
\033[32;1m                                    __-                /     \\
\033[32;1m                        _______-----    ___--          \    /)\\
\033[32;1m                  ------_______      ---____            \__/  /
\033[31;1m    _____ ___________ \033[32;1m         -----__    \ --    _          /\\
\033[31;1m   /  ___|_   _| ___ \ \033[33;1mSEARCH    \033[32;1m    --__--__     \_____/   \_/\\
\033[31;1m   \ `--.  | | | |_/ / \033[33;1mIP ADDRESS      \033[32;1m       ----|   /          |
\033[31;1m    `--. \ | | |  __/                 \033[32;1m            |  |___________|
\033[31;1m   /\__/ /_| |_| |  \033[33;1mAuthor: Billal    \033[32;1m            |  | ((_(_)| )_)
\033[31;1m   \____/ \___/\_| \033[33;1m Version: 0.1      \033[32;1m            |  \_((_(_)|/(_)
\033[32;1m  Woll Cyber Team | Black Coder Crush             \             (
\033[32;1m                                                   \_____________)""")

#ConectionError = show("error","Connection ERROR, \033[32;1mPlease Check Your Connection")

def help():
	print ("""\033[32;1m
                WELCOME TO SIP (Search IP)\033[33;1m
Commands:\033[31;1m
     help         = help
     my_ip        = show your ip address
     get_ip       = show ip address with hostname
     check_status = check status code with hostname
     find         = find location ip
     exit         = Exit Program\033[0m""")
class sip:
	url1 = "https://api.svrsc.xyz/myip.php"
	def myip(self):
#		r = ""
		try:
			r = requests.get(sip().url1)
			j = json.loads(r.text)
			show("sukses","Your IP: \033[34;1m"+str(j["myip"]))
		except requests.exceptions.ConnectionError:
			show("error","Connection ERROR, \033[32;1mPlease Check Your Connection");sys.exit()
#			sys.exit()
	def get_ip(self,host):
		url = "https://api.svrsc.xyz/rIP.php?host="+host
		try:
			r = requests.get(url)
			j = json.loads(r.text)
			ip = j["ip"]
			if ip:
				show("sukses","IP ADDRESS: \033[34;1m"+str(ip))
			else:
				show("error","IP not found");sys.exit()
		except requests.exceptions.ConnectionError:
			show("error","Connection ERROR, \033[32;1mPlease Check Your Connection");sys.exit()
	def check_status(self,host):
		try:
			r = requests.get(host)
			show("sukses","STATUS CODE: \033[34;1m"+str(r.status_code))
		except requests.exceptions.ConnectionError:
			show("error","Connection ERROR, \033[32;1mPlease Check Your Connection");sys.exit()
		except requests.exceptions.MissingSchema:
			show("warning","Please use http:// or https://");sys.exit()
	def find(self,ip):
		auth = 'd9e58341-1d55-4715-a728-efef142aa3b8';
		url = 'https://ipfind.co/?auth=d9e58341-1d55-4715-a728-efef142aa3b8&ip='+ip
		j = ""
		try:
			r = requests.get(url)
			j = json.loads(r.text)
		except requests.exceptions.ConnectionError:
			show("error","Connection ERROR, \033[32;1mPlease Check Your Connection");sys.exit()
		try:
			print ("\033[33;1m{\033[32;1mCITY\033[33;1m}> \033[32;1m"+str(j["city"]))
		except KeyError:
			show("error2","CITY")
		try:
			print ("\033[33;1m{\033[32;1mCURRENCY\033[33;1m}> \033[32;1m"+str(j['currency']))
		except KeyError:
			show("error2","CURRENCY")
		try:
			print ("\033[33;1m{\033[32;1mCOUNTRY\033[33;1m}> \033[32;1m"+str(j["country"]))
		except KeyError:
			show("error2","COUNTRY")
		try:
			print ("\033[33;1m{\033[32;1mTIME ZONE\033[33;1m}> \033[32;1m"+str(j["timezone"]))
		except KeyError:
			show("error2","TIME ZONE")
class main:
	def __init__(self):
		while True:
			co = raw_input(prompt)
			if co in ["my_ip","MY_IP"]:
				s = sip()
				s.myip()
			elif co in ["get_ip","GET_IP"]:
				host = raw_input("\033[33;1m{\033[37;1mHOST\033[33;1m}> \033[32;1m")
				s = sip()
				s.get_ip(host)
			elif co in ["q","e","quit","exit"]:
				sys.exit()
			elif co in ["help","HELP"]:
				help()
			elif co in ["check_status","CHECK_STATUS"]:
				host = raw_input("\033[33;1m{\033[37;1mHOST\033[33;1m}> \033[32;1m")
				s = sip()
				s.check_status(host)
			elif co in ["find","FIND"]:
				ip = raw_input("\033[33;1m{\033[37;1mIP\033[33;1m}> \033[32;1m")
				s = sip()
				s.find(ip)
			else:
				show("error","Command '%s' not found"%(co))
version = sys.version[0]
if version == "3":
	show("warning","User python2.7")
	sys.exit()
banner()
main()
