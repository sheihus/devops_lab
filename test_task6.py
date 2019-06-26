#!/usr/bin/env python

from unittest import TestCase

import task6


class TestTask6(TestCase):

    def setUp(self):
        """Init"""

    def test_int_ip(self):
        """Test for int_ip"""
        self.assertEqual(task6.int_ip("255.255.1.1"), 0b11111111111111110000000100000001)
        self.assertEqual(task6.int_ip("255.255.255.255"), 0b11111111111111111111111111111111)
        self.assertEqual(task6.int_ip("0.0.0.0"), 0)
        self.assertEqual(task6.int_ip("0.0.0.1"), 1)
        self.assertEqual(task6.int_ip("0.0.1.1"), 0b00000000000000000000000100000001)

    def test_check_ip(self):
        """Test for check_ip"""
        self.assertFalse(task6.check_ip("192.168.1.1", "192.168.37.2", "255.255.255.0"))
        self.assertFalse(task6.check_ip("192.168.1.1", "192.168.1.2", "255.255.255.255"))
        self.assertTrue(task6.check_ip("192.168.1.1", "192.168.1.2", "255.255.255.0"))

    def test_subnet(self):
        """Test for subnet"""
        self.assertEqual(task6.subnet("2.68.1.1", "255.0.0.0"), 0b00000010000000000000000000000000)
        self.assertEqual(task6.subnet("2.4.1.1", "255.255.0.0"), 0b00000010000001000000000000000000)
        self.assertEqual(task6.subnet("8.8.1.1", "255.0.0.0"), 0b00001000000000000000000000000000)
        self.assertEqual(task6.subnet("1.1.1.1", "255.255.0.0"), 0b00000001000000010000000000000000)

    def tearDown(self):
        """Finish"""
