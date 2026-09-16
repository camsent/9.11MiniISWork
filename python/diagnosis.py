#this is my diagnostic file for the mini IS Project. 
# a range of voltages from 2.4-2.6 will be considered normal.
# close to 0V means the resistor is disconnected from Power
# close to 5V means the resistor is disconnected from GND
import serial

arduino = serial.Serial("COM5", 9600)


def diagnose_voltage(voltage): 
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
def diagnose_two_stage(tp1, tp2):
    tp1 = float(arduino.readline().decode().rstrip()) 
    tp2 = float(arduino.readline().decode().rstrip())

    print(f"\nVoltage at TP1: {tp1} V")
    print(f"Voltage at TP2: {tp2} V")

    if 3.2 <= tp1 <= 3.4 and 1.5 <= tp2 <= 1.7:
        print("\nThe resistors are connected properly")
    elif tp1 < 3.2:
        print("\nThe resistor connected to Power is disconnected")
    elif tp1 > 3.4 and tp2 < 1.5:
        print("\nThe second resistor is disconnected")
    elif tp1 > 3.4:
        print("\nThe resistor connected to GND is disconnected")
def circuit_choosing ():
    print("\nChoose the circuit you want to diagnose:")
    print("1. Single Resistor Circuit")
    print("2. Two Resistor Circuit")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        voltage = float(arduino.readline().decode().rstrip())
        print(f"\nVoltage: {voltage} V")
        diagnose_voltage(voltage)
    elif choice == '2':
        diagnose_two_stage(None, None)
    else:
        print("\nInvalid choice. Please select 1 or 2.")
    


circuit_choosing()



