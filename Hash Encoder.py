# Jaden Russell
# 11/11/2022
# SDEV 300

import hashlib

print('Enter a message to encode:')
message = input()
message = message.encode()

print(hashlib.md5(message).hexdigest())

print(hashlib.sha256(message).hexdigest())
print(hashlib.sha512(message).hexdigest())
