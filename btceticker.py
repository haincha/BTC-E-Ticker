#!/usr/bin/python

import curses
import socket
import time
import urllib
import json
import sys
from piglow import PiGlow
from time import sleep

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

BTC_api_key = "Your Key"
BTC_api_secret = "Your Secret"

piglow = PiGlow()

piglow.all(0)

color = ["white", "blue", "green", "yellow", "orange", "red"]

class CgminerClient: 
    def command(self, host, port, command):
	# sockets are one time use. open one for each command
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
        try:
            # connect to the given host and port
            sock.connect((host, port))
 
            # json encode and send the command
            self._send(sock, json.dumps({"command": "devs"}))
 
            # receive any returned data
            received = self._receive(sock)
        finally:
            # shutdown and close the socket properly
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
        
        # the null byte makes json decoding unhappy
        decoded = json.loads(received.replace('\x00', ''))
 
        return decoded
 
    def _send(self, sock, msg):
        totalsent = 0
        while totalsent < len(msg):
            sent = sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent
 
    def _receive(self, sock, size=65500):
        msg = ''
        while True:
            chunk = sock.recv(size)
            if chunk == '':
                # end of message
                break
            msg = msg + chunk
        return msg

if __name__ == "__main__":

	try:
	
		stdscr.addstr(0,8," ____ _____ ____        _____   _____ _  ____ _  __ _____ ____")
		stdscr.addstr(1,8,"/  __Y__ __Y   _\\      /  __/  /__ __Y \\/   _Y |/ //  __//  __\\")
		stdscr.addstr(2,8,"| | // / \\ |  /  _____ |  \\      / \\ | ||  / |   / |  \\  |  \\/|")
		stdscr.addstr(3,8,"| |_\\\\ | | |  \\__\\____\\|  /_     | | | ||  \\_|   \\ |  /_ |    /")
		stdscr.addstr(4,8,"\\____/ \\_/ \\____/      \\____\\    \\_/ \\_/\\____|_|\\_\\\\____\\\\_/\\_\\")
		
		stdscr.addstr(5,7,"-----------------------------------------------------------------")
		stdscr.addstr(6,7,"|        Buy        |       Sell        |        Hashing        |")
		stdscr.addstr(7,7,"-----------------------------------------------------------------")
		stdscr.addstr(8,7,"|     $             |    $              |                       |")
		stdscr.addstr(9,7,"-----------------------------------------------------------------")
		while True:
			# Run your code here
			client = CgminerClient()
			btce = "https://www.btc-e.com/api/2/btc_usd/ticker"
			btceload = urllib.urlopen(btce)
			btcejson = json.loads(btceload.read().replace('\x00', ''))
			
			ltce = "https://btc-e.com/api/2/ltc_usd/ticker"
			ltcload = urllib.urlopen(ltce)
			ltcjson = json.loads(ltcload.read().replace('\x00', ''))


			# send command and print the response
			list = client.command("localhost", 4028, "devs")
			
			hash_pad = len(str(float(list["DEVS"][0]["MHS 5s"]) / 1000))
			
			stdscr.addstr(8,54+hash_pad,"       ")
			stdscr.addstr(8,55+hash_pad,"GHz")
			
			stdscr.addstr(8,54,str(float(list["DEVS"][0]["MHS 5s"]) / 1000))
			
			buypad = len(str(btcejson["ticker"]["buy"]))
			sellpad = len(str(btcejson["ticker"]["sell"]))
			

			ltcbuypad = len(str(ltcjson["ticker"]["buy"]))
			ltcsellpad = len(str(ltcjson["ticker"]["sell"]))

			stdscr.addstr(8,15+buypad,"     ")
			stdscr.addstr(8,34+sellpad,"     ")
			
			stdscr.addstr(8,15,str(btcejson["ticker"]["buy"]))
			stdscr.addstr(8,34,str(btcejson["ticker"]["sell"]))
			stdscr.addstr(12,15,str(ltcjson["ticker"]["buy"]))
			stdscr.addstr(12,34,str(ltcjson["ticker"]["sell"]))
			stdscr.refresh()
			
			if float(list["DEVS"][0]["MHS 5s"]) / 1000 >= 6.1 and float(list["DEVS"][0]["MHS 5s"]) / 1000 < 6.2:
				piglow.colour(color[0],10)
				piglow.colour(color[1],0)
				piglow.colour(color[2],0)
				piglow.colour(color[3],0)
				piglow.colour(color[4],0)
				piglow.colour(color[5],0)
			elif float(list["DEVS"][0]["MHS 5s"]) / 1000 >= 6.2 and float(list["DEVS"][0]["MHS 5s"]) / 1000 < 6.3:
				piglow.colour(color[0],10)
				piglow.colour(color[1],10)
				piglow.colour(color[2],0)
				piglow.colour(color[3],0)
				piglow.colour(color[4],0)
				piglow.colour(color[5],0)
			elif float(list["DEVS"][0]["MHS 5s"]) / 1000 >= 6.3 and float(list["DEVS"][0]["MHS 5s"]) / 1000 < 6.4:
				piglow.colour(color[0],10)
				piglow.colour(color[1],10)
				piglow.colour(color[2],10)
				piglow.colour(color[3],0)
				piglow.colour(color[4],0)
				piglow.colour(color[5],0)
			elif float(list["DEVS"][0]["MHS 5s"]) / 1000 >= 6.4 and float(list["DEVS"][0]["MHS 5s"]) / 1000 < 6.5:
				piglow.colour(color[0],10)
				piglow.colour(color[1],10)
				piglow.colour(color[2],10)
				piglow.colour(color[3],10)
				piglow.colour(color[4],0)
				piglow.colour(color[5],0)
			elif float(list["DEVS"][0]["MHS 5s"]) / 1000 >= 6.5 and float(list["DEVS"][0]["MHS 5s"]) / 1000 < 6.6:
				piglow.colour(color[0],10)
				piglow.colour(color[1],10)
				piglow.colour(color[2],10)
				piglow.colour(color[3],10)
				piglow.colour(color[4],10)
				piglow.colour(color[5],0)
			else:
				piglow.colour(color[0],10)
				piglow.colour(color[1],10)
				piglow.colour(color[2],10)
				piglow.colour(color[3],10)
				piglow.colour(color[4],10)
				piglow.colour(color[5],10)
			
			time.sleep(1)
			
			
	except KeyboardInterrupt:
		curses.nocbreak()
		stdscr.keypad(0)
		curses.echo()
		curses.endwin()
		piglow.all(0)
		pass
	    
	    
	finally:
	    curses.nocbreak()
	    stdscr.keypad(0)
	    curses.echo()
	    curses.endwin()
	    piglow.all(0)
