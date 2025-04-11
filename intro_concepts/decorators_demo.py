from datetime import datetime
import time

def logger(funct):
	def wrapper():
		print("-"*50)
		print("> Execution started {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
		funct()
		print("> Execution completed {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
		print("-"*50)
	return wrapper

@logger
def demo_function():
	print("Executing Task!")
	time.sleep(3)
	print("Task completed")

# demo_function()

# logger(demo_function())

def logger_args(funct):
	def wrapper(*args, **kwargs):
		print("-"*50)
		print("> Execution started {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
		funct(*args, **kwargs)
		print("> Execution completed {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
		print("-"*50)
	return wrapper

@logger_args
def demo_function_args(sleep_time):
	print("Executing Task!")
	time.sleep(sleep_time)
	print("Task completed")

demo_function_args(1)
demo_function_args(2)
