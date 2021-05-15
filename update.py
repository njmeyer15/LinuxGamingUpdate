import subprocess


def regUpdate():
    #maybe ask user if they want an update or a total update
    subprocess.call("sudo apt update",shell=True)

def freshUpdate():
    cmd="sudo apt update && sudo apt upgrage && sudo apt dist-upgrade && sudo autoremove && sudo autoclean"
    subprocess.call(cmd,shell=True)

def freshGaming():
    print("This will install wine, steam, gamemode and lutirs")
    freshUpdate()
    cmd="sudo dpkg --add-architecture i386"
    cmd2="wget -O - https://dl.winehq.org/wine-builds/winehq.key | sudo apt-key add -"
    cmd3="sudo add-apt-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ focal main' && sudo apt update && sudo apt install --install-recommends winehq-staging"
    cmd4="sudo apt install gamemode && sudo apt install steam"
    cmd5="sudo add-apt-repository ppa:lutris-team/lutris && sudo apt-get update && sudo apt-get install lutris"
    lst=[cmd,cmd2,cmd3,cmd4,cmd5]
    for i in lst:
        subprocess.call(i,shell=True)

def main():

    lst=["Update","Fresh install update","Fresh install for gaming"]

    for i in lst:
        print(lst.index(i),i)

    cmd=input("Which option would you like?")

    if cmd == "0":
        regUpdate()

    elif cmd == "1":
        freshUpdate()

    elif cmd == "2":
        freshGaming()
        


    print("Your PC has now been updated.")

main()
