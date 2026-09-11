#this is my diagnostic file for the mini IS Project. 
# a range of voltages from 2.4-2.6 will be considered normal.
# close to 0V means the resistor is disconnected from Power
# close to 5V means the resistor is disconnected from GND

voltage = float(input("Enter the voltage reading from the resistor: "))

if voltage < 1.5:
    print("\nThe resistor is disconnected from Power")
elif 1.5 <= voltage < 2.4:
    print("\nabnormal behavior, unknown fault")
elif 2.6 < voltage <= 3.7:
    print("\nabnormal behavior, unknown fault")
elif voltage > 3.7:
    print("\nThe resistor is disconnected from GND")
else:
    print("\nThe resistor is connected properly")