#let's create a time counter
'''first import time module so that we can use function like sleep function'''
import time
#let's go to ask second from users and keep it in second
second = int(input("How many seconds do you wanna wait?"))
#use loop to count time downward
for i in range(second):
    print(str(second - i) + ' ' 'seconds remaining')
    #use time.sleep()
    time.sleep(1)

print("\n\tTime is up!\t")
