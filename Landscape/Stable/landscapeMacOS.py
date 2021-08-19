# Landscape project by TheShadowG
from os import get_exec_path
import re
from sys import version
import time

version = '1.2.1'
print ("Version: " + version)
print ("Project landscape")
print ("/!\ ATTENTION /!\ ")
print ("If your client don't save the log in the minecraft folder this program won't function")
pattern = 'You earned'
matching_lines = [line for line in open('/Users/vincenzodeluca/Library/Application Support/minecraft/logs/latest.log').readlines() if pattern in line] # please edit /Users/vincenzodeluca/Library/...
 #and replace vincenzodeluca whit your user, info: https://github.com/Vincenzo160/project-landscape/wiki/Setting-the-path
if matching_lines == []:
    print ("")
    print ("No GEXP Found, if you think this is an error please report it on https://bit.ly/reportnoGEXP")
    print ("")
print ("Select from this menu")
print ("Show [G]exp earned:")
print ("Show [T]otal Gexp earned:")
input = input(":")

def list():
    print("")
    print("GEXP Earned:")
    sum = 0
    for s in matching_lines:
        m = re.search("earned (\\d+) GEXP", s)
        sum = sum + int(m.group(1))
        print(m.group(1))
    print("Total GEXP Earned = {}".format(sum))

def ssum():
    print("")
    print("Total GEXP Earned:")
    sum = 0
    for s in matching_lines:
        m = re.search("earned (\\d+) GEXP", s)
        sum = sum + int(m.group(1))
    print("GEXP Earned = {}".format(sum))


if input == "g" or input == "G" or input == "": list()
if input == "t" or input == "T": ssum()

time.sleep(10)


exit()
