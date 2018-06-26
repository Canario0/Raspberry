import schedule
from time import sleep

f = open("/sys/class/thermal/thermal_zone0/temp", "r")

def temp():
    global f
    t =int(f.read())
    f.seek(0)
    t = t/1000.0
    print("Leo mi temperatura", t)

schedule.every(10).seconds.do(temp)

try:
    while True:
        schedule.run_pending()
        sleep(1)
except KeyboardInterrupt:
    print("Cerrando el programa...")
    schedule.cancel_job(temp)
    f.close