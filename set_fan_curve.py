import time

ec_filename = "/sys/kernel/debug/ec/ec0/io" 

gpu_fan_speeds = [60, 100, 150, 150, 150, 150] # Fan speeds(%) for lowest to highest temperatures
cpu_fan_speeds = [60, 100, 150, 150, 150, 150] # Fan speeds(%) for lowest to highest temperatures

trial_number = 1
while(True):
    print("Trial {}".format(trial_number))
    print("Reading EC Memory...")
    with open(ec_filename, "rb") as ec_file:
        data = bytearray(ec_file.read())
        print(data)
        
    # GPU Temp - Fan Curve (0% - 150%) 
    print("Setting GPU Fan Curve...")
    data[114] = gpu_fan_speeds[0] # Lowest temperature fan speed %
    data[115] = gpu_fan_speeds[1]
    data[116] = gpu_fan_speeds[2]
    data[117] = gpu_fan_speeds[3]
    data[118] = gpu_fan_speeds[4]
    data[119] = gpu_fan_speeds[5] # Highest temperature fan speed %


    # CPU Temp - Fan Curve (0% - 150%) 
    print("Setting CPU Fan Curve...")
    data[138] = cpu_fan_speeds[0] # Lowest temperature fan speed %
    data[139] = cpu_fan_speeds[1]
    data[140] = cpu_fan_speeds[2]
    data[141] = cpu_fan_speeds[3]
    data[142] = cpu_fan_speeds[4]
    data[143] = cpu_fan_speeds[5] # Highest temperature fan speed %

    # Fan Profile Mode
    print("Setting Fan Profile...")
    data[244] = 140

    print("Writing data to EC Memory...")
    with open(ec_filename, "wb") as ec_file:
        ec_file.write(data)

    print("Verifying changes...")
    with open(ec_filename, "rb") as ec_file:
        data = bytearray(ec_file.read())
        print(data)
        if data[114] == gpu_fan_speeds[0] and data[115] == gpu_fan_speeds[1] and data[116] == gpu_fan_speeds[2] and data[117] == gpu_fan_speeds[3] and data[118] == gpu_fan_speeds[4] and data[119] == gpu_fan_speeds[5] and data[138] == cpu_fan_speeds[0] and data[139] == cpu_fan_speeds[1] and data[140] == cpu_fan_speeds[2] and data[141] == cpu_fan_speeds[3] and data[142] == cpu_fan_speeds[4] and data[143] == cpu_fan_speeds[5] and data[244] == 140:
            print("Verified.")
            break
        else:
            trial_number += 1
            print("Retrying in 5 seconds...\n\n")
            time.sleep(5)
