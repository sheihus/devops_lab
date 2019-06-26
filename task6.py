#!/usr/bin/env python


def int_ip(ip):
    """  Convert IP-address to int """
    a = ip.split(".")
    s = 0
    for i in range(4):
        s += int(a[i]) << (3 - i) * 8
    return s


def subnet(ip, mask):
    """ Calculate subnet """
    return int_ip(ip) & int_ip(mask)


def check_ip(ip1, ip2, mask):
    """ Check ip IP in one subnet """
    return subnet(ip1, mask) == subnet(ip2, mask)


if __name__ == "__main__":
    ip1 = input("ip1: ")
    ip2 = input("ip2: ")
    mask = input("mask: ")
    print(check_ip(ip1, ip2, mask))
