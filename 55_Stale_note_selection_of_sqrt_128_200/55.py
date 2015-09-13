import Crypto.Hash.RIPEMD as RIPEMD
code = [
    '15DC394AC902BE1BB1E52ABF2ECE13975929978D', # The
    'CD98BF0202EF07E38E87F6BD9445E5E7331E2C78', # secret
    '2C08E8F5884750A7B99F6F2F342FC638DB25FF31', # password
    'E8BD072B096A73DB1871FE1C7457B0334D1D4013', # 
    'FEE311A7CF1A6E280C3C156EDF1CA5786D93F5C9', # Teufels
    'E4B29A10FE99C0E10B28AE941148DC9F4B34A6F2', # Advokat
]

code = [x.lower() for x in code]
print code
for line in open('german.dic'):
    line = line.rstrip()
    ret = RIPEMD.new(line).hexdigest()
    if ret == code[3] or ret == code[4] or ret == code[5]:
        print line, ret
