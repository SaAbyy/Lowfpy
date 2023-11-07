import random
import sys

print('\
 __                   _____                \n\
|  |   ______  _  ___/ ____\_____ ___.__   \n\
|  |  /  _ \ \/ \/ /\   __/____  <   |  |  \n\
|  |_(  <_> )     /  |  |  |  |_> >___  |  \n\
|____/\____/ \/\_/   |__|  |   __// ____|  \n\
                           |__|   \/     ')
  
def wordlists(var):
  return 0

def generate_passwords(var):
  return 0

def generate_pseudos(var):
  return 0

dont_break = True

def help():
  return ("Lowfpy is a tool for generate passwords, wordlists and pseudos. Let's see what you can do \n \
  Test")

while True :
  command = sys.stdin.readline()
  if command == "-h" :
    output = help()
    print(output)
  
