import threading, time
from datetime import datetime

def sleeper(i):
	print("hello from %d!" % i)
	time.sleep(i)
	print("goodbye from %d!" % i)

print(datetime.now().strftime("%H:%M:%S"))
# sleeper(0)
# sleeper(1)
# sleeper(2)
# sleeper(3)
# threading.Thread(target=sleeper, args=(0,)).start()
# threading.Thread(target=sleeper, args=(1,)).start()
# threading.Thread(target=sleeper, args=(2,)).start()
# threading.Thread(target=sleeper, args=(3,)).start()
# threading.Timer(0, sleeper, [0]).start()
# threading.Timer(1, sleeper, [1]).start()
# threading.Timer(2, sleeper, [2]).start()
# threading.Timer(3, sleeper, [3]).start()
print(datetime.now().strftime("%H:%M:%S"))

# print to screen and ask user for input
stop = False

# def input_thread():
# 	global stop
# 	while True:
# 		user_input = input("Should we stop?: ")
# 		print(">> User says: {}".format(user_input))
# 		if user_input == "yes":
# 			stop = True
# 			break

# def output_thread():
# 	global stop
# 	count = 0
# 	while not stop:
# 		print(count)
# 		count += 1
# 		time.sleep(1)


# t1 = threading.Thread(target=input_thread).start()
# t2 = threading.Thread(target=output_thread).start()

# syncronize threads with lock

data_lock = threading.Lock()
data = [x for x in range(1000)]

def sync_consume_thread():
	global data_lock, data
	while True:
		data_lock.acquire()
		if len(data) > 0:
			print(threading.current_thread().name, data.pop())
		data_lock.release()


threading.Thread(target=sync_consume_thread).start()
threading.Thread(target=sync_consume_thread).start()
threading.Thread(target=sync_consume_thread).start()

# Thread will persist unless considered a daemon.