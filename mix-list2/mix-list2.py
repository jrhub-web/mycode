#!/usr/bin/env python3
proto = ['ssh', 'http', 'https']
protoa =['ssh', 'http', 'https']
print(proto)
print(proto[1])

proto.append('dns') # this line will add
                    # 'd', 'n', and 's' to
                    # the end of our list
protoa.append('dns') # This line will append 'dns' to the end of our list

print(proto)

proto2 = [22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method -- then print result
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method -- the print result
print(protoa)
