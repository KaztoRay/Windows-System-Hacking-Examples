from wpwn import *

# DEBUG = True

p = process("[prob_name]")

context.windbgx = r"C:\Users\<username>\AppData\Local\Microsoft\WindowsApps\WindbgX.exe"
context.newline = "\r\n"
context.noout

windbgx.attach(p, script = """
               
               .load /Users/user/Desktop/dreamhack/pykd/x86/pykd.dll
               !pykd.select -3.9
               
               !py /Users/user/Desktop/dreamhack/qwef/qwef.py
               
               """
               
               )

p.interactive()