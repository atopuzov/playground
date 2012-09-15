import re


def is_valid_ipv4(a):
    pattern = re.compile(r"(25[0-5]|2[0-4]\d|[01]?\d?\d)\.(25[0-5]|2[0-4]\d|[01]?\d?\d)\.(25[0-5]|2[0-4]\d|[01]?\d?\d)\.(25[0-5]|2[0-4]\d|[01]?\d?\d)", re.VERBOSE)
    return pattern.match(a) is not None

ar = { '161.53.200.3' : True, '255.255.255.255' : True, '45.32.342.1' : False, '8.8.8.8' : True }

for a in ar.keys():
    print "Testing:", a
    ok = ar[a] == is_valid_ipv4(a)
    if not ok:
        print "Test failed:"

