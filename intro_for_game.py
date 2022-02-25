from time import sleep
import sys
print "Welcome to:\n"

sleep(1)

title = """
      _                                _
     | |                              | |
     | | ___  ___  _ __   __ _ _ __ __| |_   _
 _   | |/ _ \/ _ \| '_ \ / _` | '__/ _` | | | |
| |__| |  __/ (_) | |_) | (_| | | | (_| | |_| |
 \____/ \___|\___/| .__/ \__,_|_|  \__,_|\__, |
                  | |                     __/ |
                  |_|                    |___/
"""
for i in title: #This goes through each line of the title
  sleep(0.01)
  sys.stdout.write(i)
  sys.stdout.flush()


words = "\n\nToday you will be versing other contestants in order to test your knowledge for money. \nYou will have 30 seconds to answer each question and input your answer. \n\nHave Fun!\n\n"

for x in words:
  sleep(0.1)
  sys.stdout.write(x) #Writes character by character without a space
  sys.stdout.flush() #Runs this function more smoothly


sleep(1) #Follows the intro
print "Loading ."
sleep(1.5)
print "Loading .."
sleep(1.5)
print "Loading ..."
sleep(1.5)



