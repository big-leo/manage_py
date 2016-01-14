def is_ip_addr(host):
    list = host.split('.')
    if (len(list) != 4):
        return False
    count = 0
    for element in list:
        count = count + 1
        if (not element.isdigit()):
            return False
        if (count != 2 and count != 3 and int(element) < 1):
            return False
        if (int(element) > 254):
            return False
    return True
