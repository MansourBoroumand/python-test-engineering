measured_voltage = 5.08
min_voltage = 4.90
max_voltage = 5.10

if min_voltage <= measured_voltage <= max_voltage:
    print("PASS")
else:
    print("FAIL")