breakpoint()

test = "test"
print(test)

print(test)

print("here")

for i in range(10):
	print(i)

# can also load pdb with:
# python -m pdb debugging.py
# can modify or print vars, introduce new vars, etc. 
# run -> reruns program.
# p test -> will result in value of varaible.
# c -> continues program
# step -> run until it steps into a fuction
# help -> prints help menu
# b func, line#, etc. -> creates breakpoint
# l 1,4 -> view first 4 lines.
# jump -> jump to line
# <Return> -> run previous command
# can't jump into function before args are defined, or the middle of try - except
# disable -> disbale breakpoint 