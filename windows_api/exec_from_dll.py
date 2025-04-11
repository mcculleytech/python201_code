from ctypes import *

print(windll.msvcrt.time(None))

windll.msvcrt.puts(b"print this")

mut_str = create_string_buffer(10)
print(mut_str.raw)

mut_str.value = b"AAAA"
print(mut_str.raw)

windll.msvcrt.memset(mut_str, c_char(b"X"), 5)
windll.msvcrt.puts(mut_str)
print(mut_str.raw)

lib = WinDLL("C:\\Users\\alex\\source\\repos\\dll\\x64\\Debug\\dll.dll")
lib.hello()

lib.length.argtypes = (c_char_p, )
lib.length.restype = c_int

str1 = c_char_p(b"test")
print(lib.length(str1))

str2 = c_char_p(b"test1234")
print(lib.length(str2))


# note the dll function returns 3 for length, due to null terminator.
str3 = b"abc\x00123"
print(len(str3))
print(lib.length(c_char_p(str3)))

lib.add.argtypes = (c_int, c_int)
lib.add.restype = c_int

print("2 + 2 = ", lib.add(2,2))

lib.add_p.argtypes = (POINTER(c_int), POINTER(c_int), POINTER(c_int))

x = c_int(2)
y = c_int(4)
result = c_int(0)

print(result)
print(result.value)

lib.add_p(byref(x), byref(y), byref(result))
print("2 + 4 = ", result.value)
