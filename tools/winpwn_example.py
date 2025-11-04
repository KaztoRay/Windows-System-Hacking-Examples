from wpwn import *

# DEBUG = True

p = process("<prob>")

context.windbgx = r"C:\Users\<username>\AppData\Local\Microsoft\WindowsApps\WindbgX.exe"
context.newline = "\r\n"
context.noout

windbgx.attach(p, script = """
               
               <Commands>
               
               """
               
               )

p.interactive()