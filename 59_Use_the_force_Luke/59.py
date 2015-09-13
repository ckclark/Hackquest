from base64 import decodestring
import re
force = open('force.txt').read()
mat = re.search(r'password!(.+)', decodestring(force))
print decodestring(mat.group(1))
