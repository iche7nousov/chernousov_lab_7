#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    first_dic = {1: "Один", 2: "Два", 3: "Три"}
    last_dic = {}

    for key, value in first_dic.items():
        print(key, value)
        last_dic[value] = key

    print(last_dic)
