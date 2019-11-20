# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 13:40:19 2018

@author: dkoczur
198504XX5, 254845GC8, 442403NQ0, 557363DH8, 5816637K1, 64990ED53, 677522ZB3, 686516KH7, 707332PT3, 709235TD7, 735240J38, 849476RU2, 87971HFB5, 93974DRR1


"""

import win32clipboard

win32clipboard.OpenClipboard()
text = win32clipboard.GetClipboardData().strip()

output = "'"+ "','".join([str(i.strip()) for i in set(text.split(","))]) + "'"

win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(output)
win32clipboard.CloseClipboard()
print(output)


