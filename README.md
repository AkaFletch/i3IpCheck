An i3 block which will send a single ping to listed devices and list the related name as home

Real quick script which just pings each listed ip address and prints out which ip's respond with their given names.
It's neccessary to set the IP's as static to ensure the script will continue to work over longer periods. I recommend using a users phone as they're usually always carried

Font awesome is recommended for the nice house icon

To install:
Download the .py and simply move it where your i3Block scripts are stored and add the block to the i3Block.conf

To edit the names and Ip's used to edit the script and ensure that the IP and Name of the device user are in the same index.

Example config:<p>
#People Indicator<br>
[ipblock]<br>
label=<br>
interval=2<br>
separator=true<br>
