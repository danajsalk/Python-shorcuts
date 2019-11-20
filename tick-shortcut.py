"""
Simple Shortcut tick wraps list of values from clipboard

"""
import win32clipboard  

win32clipboard.OpenClipboard()
values = win32clipboard.GetClipboardData().strip()

output = "'" + "','".join([str(i) for i in set(values.split())]) + "'"  

win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText(output)
win32clipboard.CloseClipboard()
