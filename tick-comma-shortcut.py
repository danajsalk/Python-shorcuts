"""
Simple shortcut to add ticks to a comma seperated string

"""

import win32clipboard

win32clipboard.OpenClipboard()
text = win32clipboard.GetClipboardData().strip()

output = "'"+ "','".join([str(i.strip()) for i in set(text.split(","))]) + "'"

win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(output)
win32clipboard.CloseClipboard()
print(output)


