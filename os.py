import os
import sys
import random
import threading
import socket

def editfile(filename):
	print(f"\033[47m\033[91m\033[1mFileEditor v1.0 ~ Name: {filename} ~ Enter 'okeyexit' to exit\033[0m")
	content = ""
	for num in range(1, 1000000000):
		line = input(f"\033[0m{num}| \033[93m")
		if line == "okeyexit":
			break
		else:
			content += line+"\n"
	return content
def title(text):
	print(f"\033[93m\033[1mSSVPYO\033[0m/ \033[93m{text}\033[0m")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class ssvpyo:
	def __init__(self):
		self.files = {}
	def load(self):
		savefile = open(".ssvpyo.save-os", "r")
		exec(f"self.files = {savefile.read()}")
		savefile.close()
	def save(self):
		savefile = open(".ssvpyo.save-os", "w")
		savefile.write(str(self.files))
		savefile.close()
	def cmd(self, c):
		try:
			c = c.split()
			if c[0] == "cf":
				title(f"Filename: {c[1]}")
				content = editfile(c[1])
				self.files[c[1]] = content
				title(f"File Created")
			elif c[0] == "rf":
				title(f"Filename: {c[1]}")
				if c[1] in self.files:
					del self.files[c[1]]
				else:
					title("File not found")
			elif c[0] == "ef":
				title(f"Filename: {c[1]}")
				if c[1] in self.files:
					content = editfile(c[1])
					self.files[c[1]] = content
				else:
					title("File not found")
			elif c[0] == "sf":
				title(f"Filename: {c[1]}")
				if c[1] in self.files:
					print(self.files(c[1]))
				else:
					title("File not found")
			elif c[0] == "pf":
				title(f"Filename: {c[1]}")
				if c[1] in self.files:
					try:
						exec(self.files[c[1]])
					except Exception as e:
						print(f"{c[1]}: Error: {e}")
				else:
					title("File not found")
			elif c[0] == "ls":
				lslist = []
				for name, a in self.files.items():
					lslist.append(name)
				print(" ".join(lslist))
			elif c[0] == "bf":
				title(f"Filename: {c[1]}")
				if c[1] in self.files:
					print(len(self.files[c[1]]))
				else:
					title("File not found")
			elif c[0] == "ht":
				title(f"Target: {c[1]}")
				title(f"Port: {c[2]}")
				title(f"Method: {c[3]}")
				title(f"Path: {c[4]}")
				title(f"Buffer Size: {c[5]}")
				mes = f"{c[3]} {c[4]} HTTP/1.1\r\nHost: {c[1]}\r\n"
				yesno = input(f"Use Token? (Y/n): ")
				yesno = yesno.lower()[0]
				if yesno == "y":
					token = input("Enter Token: ")
					mes += f"Authorization: Beaser {token}\r\n"
				yesno = input(f"Use VPN Proxy? (Y/n): ")
				yesno = yesno.lower()[0]
				ips = ["102.38.17.193", "103.78.170.13", "125.141.151.83", "94.198.40.18", "41.33.145.219", "52.191.208.232", "217.52.247.77", "213.6.170.17", "203.57.51.53", "156.67.172.185", "155.248.213.236"]
				uas = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3", "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.54", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"]
				if yesno == "y":
					ua = random.choice(uas)
					print(f"User Agent: {ua}")
					ip = random.choice(ips)
					print(f"IP Address: {ip}")
					mes += f"User-Agent: {ua}\r\nX-Forwarded-For: {ip}\r\nX-Real-IP: {ip}\r\nPragma: no-cache\r\nCache-Control: no-cache, no-store, must-revalidate\r\n"
				mes += "\r\n"
				try:
					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					s.settimeout(3)
					s.connect((c[1], int(c[2])))
					s.sendall(mes.encode())
					r = s.recv(int(c[5]))
					print(f"\n{r.decode()}")
				except Exception as e:
					title(f"Error: {e}")
				s.close()
			elif c[0] == "ci":
				title(f"Checking: {c[1]}")
				try:
					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);s.settimeout(1);s.connect((c[1], 80));s.close()
					print(f"IP Address is Real")
				except:
					try:
						socket.inet_aton(c[1])
						print(f"IP Address is True but closed")
					except:
						print(f"IP Address is Fake")
			elif c[0] == "gi":
				try:
					ip = socket.gethostbyname(c[1])
					print(f"Found: {ip}")
				except:
					title("Website not found")
			elif c[0] == "ss":
				lslist = []
				for name, a in self.files.items():
					lslist.append(name)
				title(f"Os size: {len(str(self.files))} B")
				title(f"Os creator: https://github.com/aertsimon90/")
				title(f"Os save file: .ssvpyo.save-os")
				title(f"Os files: {' '.join(lslist)}")
				title(f"Os file count: {len(lslist)}")
			elif c[0] == "cr":
				clear()
			elif c[0] == "ex":
				print(f"Goodbye!")
				sys.exit()
			elif c[0] == "help":
				print("cf <file-name> = Create a file")
				print("rf <file-name> = Remove a file")
				print("ef <file-name> = Edit a file content")
				print("sf <file-name> = Show a file content")
				print("pf <file-name> = Start file with python")
				print("ls = List files")
				print("bf <file-name> = Display a file byte size")
				print("ht <target> <port> <method> <path> <buffersize> = Send a http request and display recv")
				print("ci <ip-address> = Check ip address is real or fake")
				print("gi <website-url> = Find a website ip address")
				print("ss = Show os info")
				print("cr = Clear screen")
				print("ex = Exit the os")
				print("help = Open this page")
			else:
				if c == "":
					pass
				elif c == None:
					pass
				else:
					title(f"Command not found: {c[1]} | Please enter 'help' to display avaible commands")
		except Exception as e:
			if c == "":
				pass
			elif c == None:
				pass
			elif c == []:
				pass
			elif c == " ":
				pass
			else:
				title(f"Error: {e}")
def startos():
	clear()
	print("\033[91m\033[47m\033[1mSimonScap's Virtual \033[94mPython OS (SSVPYO)\033[0m")
	myos = ssvpyo()
	try:
		myos.load()
	except:
		title("Save file not found | Creating...")
		file = open(".ssvpyo.save-os", "w")
		file.write("{}")
		file.close()
		myos.load()
	while True:
		myos.save()
		c = input(f"\033[93m~$ \033[0m")
		myos.cmd(c)

os.system(f"chmod +x *")

myoss = threading.Thread(target=startos)
myoss.start()
myoss.join()
