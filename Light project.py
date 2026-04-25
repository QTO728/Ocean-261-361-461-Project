from machine import I2C, SoftI2C, Pin
import TSL2591
import urtc
from time import sleep_ms
# ── Set up each bus individually ──────────────────────────────────────────────
# Sets up the i2c pin
i2c = I2C(0, sda =(0), scl=(1), freq=400000)
# Assigns i2c pin to the clock
rtc = urtc.DS3231(i2c)
#rtc.datetime((2026, 4, 22, 4, 3, 14, 0, 0)) 
#i2c0 = I2C(0, sda=Pin(0), scl=Pin(1), freq=100000)
#i2c1 = I2C(1, sda=Pin(2), scl=Pin(3), freq=400000)
i2c2 = SoftI2C(sda=Pin(10), scl=Pin(11), freq=100_000) # works
i2c3 = SoftI2C(sda=Pin(26), scl=Pin(27), freq=100_000)

#sensor0 = TSL2591.TSL2591(i2c0)
#sensor1 = TSL2591.TSL2591(i2c1)
sensor2 = TSL2591.TSL2591(i2c2) #works
sensor3 = TSL2591.TSL2591(i2c3)

# ── Read each sensor ──────────────────────────────────────────────────────────
 
#print(f"Sensor 0 — lux: {sensor0.lux:.2f}, full: {sensor0.full_spectrum}, IR: {sensor0.infrared}")
#print(f"Sensor 1 — lux: {sensor1.lux:.2f}, full: {sensor1.full_spectrum}, IR: {sensor1.infrared}")
print(f"Sensor 2 — lux: {sensor2.lux:.2f}, full: {sensor2.full_spectrum}, IR: {sensor2.infrared}")
print(f"Sensor 3 — lux: {sensor3.lux:.2f}, full: {sensor3.full_spectrum}, IR: {sensor3.infrared}")

# Read each sensor per second as needed and store data in csv file
def getLight(x):
    recordSheet = open("dataLight.csv", "a")
    for i in range(x):
        light1 = sensor2.lux
        light2 = sensor3.lux
        d = rtc.datetime()
        hours = str(d.hour) + ':' + str(d.minute) + ':' +str(d.second)
        date = str(d.year) + '/' + str(d.month) + '/' +str(d.day)
        print(date, hours, light1, light2)
        #print(date, hours, light2)
        recordSheet.write(str(hours)+ "," + str(date) + "," + str(light1) + str(light2) +  "/n")
        sleep_ms(500)
    recordSheet.close() 
getLight(6)
