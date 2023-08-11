import os, sys, threading, socket

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
				if c[1] == "":
					title("Name not found")
				elif c[1] == ".":
					title("Name error")
				elif c[1] == "/":
					title("Name error")
				elif c[1] == "*":
					title("Name error")
				elif c[1] == "'":
					title("Name error")
				elif c[1] == '"':
					title("Name error")
				elif "/" in c[1]:
					title("Invalid char: /")
				else:
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
				try:
					s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
					s.settimeout(3)
					s.connect((c[1], int(c[2])))
					s.sendall(f"{c[3]} {c[4]} HTTP/1.1\r\nHost: {c[1]}\r\n\r\n".encode())
					r = s.recv(int(c[5]))
					print(f"\n{r.decode()}")
				except Exception as e:
					title(f"Error: {e}")
				s.close()
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
				print("ss = Show os info")
				print("cr = Clear screen")
				print("ex = Exit the os")
				print("help = Open this page")
			else:
				title(f"Command not found: {c[1]} | Please enter 'help' to display avaible commands")
		except Exception as e:
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
