__author__ = 'dhana013'



def sizeof_fmt(num, suffix='B'):

    num = num * 1024 * 1024

    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

x = sizeof_fmt(16384)
print x