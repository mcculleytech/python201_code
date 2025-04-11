from ctypes import *
from ctypes import wintypes

# I have a feeling this script won't work on win11. the move from win10 made it significantly harder to make direct syscalls in windows from heap memory.
# The first section of the code works, but when i try the second section it dies and spits an error for executable memory space.

SIZE_T = c_size_t # make it easier using ctypes and wintypes interchangably
NTSTATUS = wintypes.DWORD

MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000
PAGE_EXECUTE_READ_WRITE = 0x40

# syscalls vary on win version and release, look into win version.
# win11 23H2 -> same as in course 18h

"""
mov r10, rcx
mov eax, 18h
syscall
return
"""

def verify(x):
	if not x:
		raise WinError()

# step 1 - write asm as shellcode
# use debugger x64 debug
 
# step 2 - place shellcode into memory

buf = create_string_buffer(b"\xb8\x05\x00\x00\x00\xc3")
buf_addr = addressof(buf)
print(hex(buf_addr))

VirtualProtect = windll.kernel32.VirtualProtect
VirtualProtect.argtypes = (wintypes.LPVOID, SIZE_T, wintypes.DWORD, wintypes.LPDWORD)
VirtualProtect.restype = wintypes.INT

# step 3 - update memory for location to enable execution - otherwise error will spit for no execute privs in memory
old_protection = wintypes.DWORD(0)
protect = VirtualProtect(buf_addr, len(buf), PAGE_EXECUTE_READ_WRITE, byref(old_protection))
verify(protect)

asm_type = CFUNCTYPE(c_int)
asm_function = asm_type(buf_addr)

r = asm_function()
print(hex(r))

buf2 = create_string_buffer(b"\x49\x89\xCA\xB8\x18\x00\x00\x00\x0F\x05")
buf_addr2 = addressof(buf2)
print("Buffer address:", hex(buf_addr2))

old_protection = wintypes.DWORD(0)
protect = VirtualProtect(buf_addr2, len(buf2), PAGE_EXECUTE_READ_WRITE, byref(old_protection))
verify(protect)

syscall_type = CFUNCTYPE(NTSTATUS, wintypes.HANDLE, POINTER(wintypes.LPVOID), wintypes.ULONG, POINTER(wintypes.ULONG), wintypes.ULONG, wintypes.ULONG)
syscall_function = syscall_type(buf_addr2)

handle = 0xffffffffffffffff # psuedo handle to use
base_address = wintypes.LPVOID(0x0) # NULL to allow OS to determine location in memory
zero_bits = wintypes.ULONG(0)
size = wintypes.ULONG(1024 * 24)
# MEM_COMMIT, MEM_RESERVE and PAGE_EXECUTE_READ_WRITE will work for the rest
ptr2 = syscall_function(handle, byref(base_address), zero_bits, byref(size), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READ_WRITE)

if ptr2 != 0:
	print("error!")
	print(ptr2)

print("Syscall allocation: ", hex(base_address.value))

input()