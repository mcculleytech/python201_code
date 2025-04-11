from ctypes import *
from ctypes import wintypes

kernel32 = windll.kernel32
SIZE_T = c_size_t # make it easier using ctypes and wintypes interchangably

VirtualAlloc = kernel32.VirtualAlloc
VirtualAlloc.argtypes = (wintypes.LPVOID, SIZE_T, wintypes.DWORD, wintypes.DWORD)
VirtualAlloc.restype = wintypes.LPVOID

MEM_COMMIT = 0x00001000
MEM_RESERVE = 0x00002000
PAGE_EXECUTE_READ_WRITE = 0x40

ptr = VirtualAlloc(None, 1024 *4, MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READ_WRITE)

error = GetLastError()

if error:
	print(error)
	print(WinError(error))

print("VirtualAlloc: ", hex(ptr))

nt = windll.ntdll
NTSTATUS = wintypes.DWORD

NTAllocateVirtualMemory = nt.NtAllocateVirtualMemory
NTAllocateVirtualMemory.argtypes = (wintypes.HANDLE, POINTER(wintypes.LPVOID), wintypes.ULONG, POINTER(wintypes.ULONG), wintypes.ULONG, wintypes.ULONG)
NTAllocateVirtualMemory.restype = NTSTATUS

handle = 0xffffffffffffffff # psuedo handle to use
base_address = wintypes.LPVOID(0x0) # NULL to allow OS to determine location in memory
zero_bits = wintypes.ULONG(0)
size = wintypes.ULONG(1024 * 12)
# MEM_COMMIT, MEM_RESERVE and PAGE_EXECUTE_READ_WRITE will work for the rest
ptr2 = NTAllocateVirtualMemory(handle, byref(base_address), zero_bits, byref(size), MEM_COMMIT | MEM_RESERVE, PAGE_EXECUTE_READ_WRITE)

if ptr2 != 0:
	print("error!")
	print(ptr2)

print("NTAllocateVirtualMemory: ", hex(base_address.value))


input()
