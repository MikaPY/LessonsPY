import threading 
import time 


# Create function.
def gender(file_name,start,end): # add start,end
	with open(file_name) as f:
		for line in f.readlines()[start:end]:
			info = line[:-1].split(",")


# Create a file for male.
			if info[3] == 'male':
				with open("males.txt","a") as malef:
					malef.write(line)


# Create a file for female:
			elif info[3] == 'female':
				with open("females.txt", "a") as femalef:
					femalef.write(line)

			time.sleep(0.1)


# Call function.

start_time = time.time(*args)

t1 = threading.Thread(target =gender, args=("users.txt",1,25))
t2 = threading.Thread(target =gender, args=("users.txt",26,55))
t3 = threading.Thread(target =gender, args=("users.txt",51,75))
t4 = threading.Thread(target =gender, args=("users.txt",76,100))


t1.start()
t2.start()
t3.start()
t4.start()


# Wait for end
t1.join()
t2.join()
t3.join()
t4.join()



print('Time:', time.time() - start_time)