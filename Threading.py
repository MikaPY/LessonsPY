import threading 
import time 

def nums():
	for i in range(1,10001):
		if i % 2 == 0:
			print(i)

		time.sleep(0.25)

start_time = time.time()

t1 = threading.Thread(target =nums, args=(1,2000))
t2 = threading.Thread(target =nums, args=(2001,4000))
t3 = threading.Thread(target =nums, args=(4001,6000))
t4 = threading.Thread(target =nums, args=(8001,10000))


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