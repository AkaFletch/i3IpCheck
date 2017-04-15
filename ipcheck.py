import os

ips = ["192.168.1.187", "192.168.1.133", "192.168.1.110"]
names = ["Ryan", "Mum", "Dad"]

home = ""
count = 0

for i in range(len(ips)):
    response = os.system("ping -c 1 " + ips[i]+" 2>&1 >/dev/null")
    if response == 0:
        if count > 0:
            home += ", "
        home += names[i]
        count = count + 1

if home == "":
    print("No one is home")
    print("No one is home")
elif count == 1:
    print(home + " is home")
    print(home + " is home")
elif count > 1:
    print(home + " are home")
    print(home + " are home")
