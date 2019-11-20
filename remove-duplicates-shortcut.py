"""
Simple Shortcut removes duplicate values from clipboard
"""

import win32clipboard

win32clipboard.OpenClipboard()
values = win32clipboard.GetClipboardData().strip()

output = "\n".join([str(i) for i in set(values.split())])

win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(output)
win32clipboard.CloseClipboard()

