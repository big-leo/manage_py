def full_ip(host):
    print(host, '<- address not correct')

def is_ip_addr(host):
    list = host.split('.')
    if (len(list) != 4):
        return False
    count = 0
    for element in list:
        count = count + 1
        if (not element.isdigit()):
            full_ip(host)
            return False
        if (count != 2 and count != 3 and int(element) < 1):
            full_ip(host)
            return False
        if (int(element) > 254):
            full_ip(host)
            return False
    return True
