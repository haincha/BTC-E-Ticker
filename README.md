BTC-E-Ticker
============

Just a basic Ticker / ASIC Hashing reader / PiGlow feedback.

Assuming you have API turned on in cgminer.

Pretty basic. Free to take whatever you want, leave the rest.

The piglow.py library has been borrowed from https://github.com/Boeeerb/PiGlow and remains fully intact. If you need any help setting it up, suggest you check that link.

You will need ncurses installed to use the interface, however, if you have cgminer installed you already have ncurses.

API Key and Secret can be obtained from https://btc-e.com They are only needed if you intend to add the ability to buy and sell coin from this ticker. Which is obviously not implemented yet. So, pretty safe to leave out.

Make sure your conf file located at "/root/.cgminer/cgminer.conf" matches up with mine. This can be accomplished by issuing a "sudo nano /root/.cgminer/cgminer.conf" from your pi and making sure everything underneath the BTC address match up.
