import psutil

print("CPU Usage:", psutil.cpu_percent(interval=1), "%")
print("RAM Usage:", psutil.virtual_memory().percent, "%")