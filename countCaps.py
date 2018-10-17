#!/usr/bin/bash
with open(txtFile) as fh:
    count = 0
    for i in fh.readlines():
        if i.isupper():
            count += 1
    print(count)
