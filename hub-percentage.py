from pybricks.hubs import InventorHub
from pybricks.tools import wait

hub = InventorHub()

def display_battery_info():
    voltage = hub.battery.voltage()
    current = hub.battery.current()

    charger_connected = hub.charger.connected()
    charging_current = hub.charger.current()
    charging_status = hub.charger.status()

    min_voltage = 6000  # 6.0V
    max_voltage = 8400  # 8.4V

    battery_percentage = (voltage - min_voltage) / (max_voltage - min_voltage) * 100
    battery_percentage = max(0, min(100, battery_percentage))  # Ensure percentage is between 0 and 100

    print("Battery Voltage: {} mV".format(voltage))
    print("Battery Current: {} mA".format(current))
    print("Battery Percentage: {:.2f}%".format(battery_percentage))

    if charger_connected:
        print("Charger Connected: Yes")
        print("Charging Current: {} mA".format(charging_current))
        print("Charging Status: {}".format(charging_status))
    else:
        print("Charger Connected: No")

display_battery_info()

wait(1000)
