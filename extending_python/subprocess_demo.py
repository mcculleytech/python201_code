import subprocess

# out = subprocess.check_call(["cmd", "/c", "calc"])
# subprocess.check_call(["calc"], shell=True)

out = subprocess.check_output(["cmd", "/c", "whoami"])
print("the output was {}".format(out.decode()))