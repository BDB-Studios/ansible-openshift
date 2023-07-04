#!/usr/bin/python3
# -*- coding: utf-8 -*-
# macgen.py script to generate a MAC address for guests on Xen

import random


def random_mac():
	mac = [ 0x52, 0x54, 0x00,
		random.randint(0x00, 0x7f),
		random.randint(0x00, 0xff),
		random.randint(0x00, 0xff) ]
	return ':'.join(map(lambda x: "%02x" % x, mac))


print(random_mac())
