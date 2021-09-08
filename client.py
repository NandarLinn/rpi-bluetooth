import bluetooth
import time

port = 1
predefined_address = ["DC:A6:32:B3:6C:D3", "B8:27:EB:37:B1:1D"]

while True:
	print("Waiting for Connection .....")
	sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

	nearby_devices = bluetooth.discover_devices(lookup_names = True)
	print("found %d devices" % len(nearby_devices))

	for addr, name in nearby_devices:
		print("  %s - %s" % (addr, name))
		str_addr = addr.decode('"utf-8"')
		if str_addr in predefined_address:
			sock.connect((str_addr,port))

			try:
				sock.send(bytes("Hello", encoding='utf-8'))
			except:
				print("Send fail")

			#Get reply data
			try:
				reply = sock.recv(4096)
				if reply:
					print("Reply Data", reply)
					print("### Do Something Here ###")
					## Do Something ##
				else:
					time.sleep(40)
					print("Recieved time out")
			except:
				pass

		else: print("Sorry device not found")
		sock.close()
		time.sleep(120)
