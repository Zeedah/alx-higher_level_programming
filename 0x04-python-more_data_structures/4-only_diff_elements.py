#!/usr/bin/python3
# 4-only_diff_elements.py
# zuwairah dahiru <375@holbertonschool.com>


def only_diff_elements(set_1, set_2):
    """Return a set of all elements present in only one set."""
    return (set_1 ^ set_2)
