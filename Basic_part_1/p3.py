from datetime import datetime

x = datetime.now()
print("the current date and time is")
print(x.strftime("%Y") + "-" + x.strftime("%m") + "-" + x.strftime("%d") + "  " + x.strftime("%X"))
