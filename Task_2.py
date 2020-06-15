t = int(input("Enter the time in seconds: "))
h = t // 3600
m = (t // 60) - (h * 60)
s = t % 60
print(f"{h:02}:{m:02}:{s:02}")
