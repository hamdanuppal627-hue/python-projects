appliance = [] 
unit = [] 
print(" --------------------") 
print("|Welcome To Unit Hub!|") 
print(" --------------------") 
print("If you have both Fan and AC, write 'both'.") 
user_input = input("Do you have any of the following: 'Fan' or 'AC'? If yes, enter the name: ").lower() 
if user_input == "fan":
    inverter_fan = False 
    inverter_input = input("Do you have an inverter fan? (yes/no): ").lower() 
    if inverter_input == "yes":
        inverter_fan = True 
        amount_fan = int(input("Enter the number of inverter fans you have: ")) 
        hours = float(input("How many hours per day is it used?: "))
        total_unit_normalfan = (25 * amount_fan * hours * 30)
        print(f"Your fan consumes {25 * amount_fan} Wh!") 
        appliance.append("Inverter Fan") 
        unit.append(total_unit_normalfan) 
    elif inverter_input == "no":
        amount_fan_inverter = int(input("Enter the number of normal fans you have: ")) 
        hours = float(input("How many hours per day is it used?: "))
        total_unit_inverterfan = (75 * amount_fan_inverter * hours * 30)
        print(f"Your fan consumes {75 * amount_fan_inverter} Wh!") 
        appliance.append("Normal Fan") 
        unit.append(total_unit_inverterfan) 
    else:
        print("Invalid input. Please enter 'yes' or 'no'.") 
elif user_input == "ac":
    inverter_ac = False 
    inverter_ac_input = input("Do you have an inverter AC (air conditioner)? (yes/no): ").lower() 
    if inverter_ac_input == "yes":
        appliance.append("Inverter AC") 
        amount_inverter_ac = int(input("Enter the number of inverter ACs you have: ")) 
        inverter_ac = True 
        ac_size = int(input("What size is your AC? (1 Ton, 1.5 Ton, or 2 Ton): ")) 
        hours = float(input("How many hours per day is it used?: "))
        if ac_size == 1:
            ac_size_1 = amount_inverter_ac * 600 
            print(f"Your AC consumes around {ac_size_1} Wh!") 
            unit.append(ac_size_1 * hours * 30) 
        elif ac_size == 1.5:
            ac_size_2 = amount_inverter_ac * 850 
            print(f"Your AC consumes around {ac_size_2} Wh!") 
            unit.append(ac_size_2 * hours * 30) 
        elif ac_size == 2:
            ac_size_3 = amount_inverter_ac * 1200 
            print(f"Your AC consumes around {ac_size_3} Wh!") 
            unit.append(ac_size_3 * hours * 30) 
    elif inverter_ac_input == "no":
        inverter_ac = False 
        appliance.append("Normal AC") 
        amount_normal_ac = int(input("Enter the number of normal ACs you have: ")) 
        ac_size = int(input("What size is your AC? (1 Ton, 1.5 Ton, or 2 Ton): ")) 
        hours = float(input("How many hours per day is it used?: "))
        if ac_size == 1:
            ac_normal_1 = amount_normal_ac * 1100 
            print(f"Your AC consumes around {ac_normal_1} Wh!") 
            unit.append(ac_normal_1 * hours * 30) 
        elif ac_size == 1.5:
            ac_normal_2 = amount_normal_ac * 1700 
            print(f"Your AC consumes around {ac_normal_2} Wh!") 
            unit.append(ac_normal_2 * hours * 30) 
        elif ac_size == 2:
            ac_normal_3 = amount_normal_ac * 2400 
            print(f"Your AC consumes around {ac_normal_3} Wh!") 
            unit.append(ac_normal_3 * hours * 30) 
    else:
        print("Invalid input. Please enter 'yes' or 'no'.") 
elif user_input == "both":
    inverter_fan = False 
    inverter_input = input("Do you have an inverter fan? (yes/no): ").lower() 
    if inverter_input == "yes":
        inverter_fan = True 
        amount_fan = int(input("Enter the number of inverter fans you have: ")) 
        hours_fan = float(input("How many hours per day are the fans used?: "))
        total_unit_normalfan = (25 * amount_fan * hours_fan * 30)
        print(f"Your fan consumes {25 * amount_fan} Wh!") 
        appliance.append("Inverter Fan") 
        unit.append(total_unit_normalfan) 
    elif inverter_input == "no":
        amount_fan_inverter = int(input("Enter the number of normal fans you have: ")) 
        hours_fan = float(input("How many hours per day are the fans used?: "))
        total_unit_inverterfan = (75 * amount_fan_inverter * hours_fan * 30)
        print(f"Your fan consumes {75 * amount_fan_inverter} Wh!") 
        appliance.append("Normal Fan") 
        unit.append(total_unit_inverterfan) 
    else:
        print("Invalid input. Please enter 'yes' or 'no'.") 
    inverter_ac = False 
    inverter_ac_input = input("Do you have an inverter AC (air conditioner)? (yes/no): ").lower() 
    if inverter_ac_input == "yes":
        appliance.append("Inverter AC") 
        amount_inverter_ac = int(input("Enter the number of inverter ACs you have: ")) 
        inverter_ac = True 
        ac_size = float(input("What size is your AC? (1 Ton, 1.5 Ton, or 2 Ton): ")) 
        hours_ac = float(input("How many hours per day is the AC used?: "))
        if ac_size == 1:
            ac_size_1 = amount_inverter_ac * 600 
            print(f"Your AC consumes around {ac_size_1} Wh!") 
            unit.append(ac_size_1 * hours_ac * 30) 
        elif ac_size == 1.5:
            ac_size_2 = amount_inverter_ac * 850 
            print(f"Your AC consumes around {ac_size_2} Wh!") 
            unit.append(ac_size_2 * hours_ac * 30) 
        elif ac_size == 2:
            ac_size_3 = amount_inverter_ac * 1200 
            print(f"Your AC consumes around {ac_size_3} Wh!") 
            unit.append(ac_size_3 * hours_ac * 30) 
    elif inverter_ac_input == "no":
        inverter_ac = False 
        appliance.append("Normal AC") 
        amount_normal_ac = int(input("Enter the number of normal ACs you have: ")) 
        ac_size = float(input("What size is your AC? (1 Ton, 1.5 Ton, or 2 Ton): ")) 
        hours_ac = float(input("How many hours per day is the AC used?: "))
        if ac_size == 1:
            ac_normal_1 = amount_normal_ac * 1100 
            print(f"Your AC consumes around {ac_normal_1} Wh!") 
            unit.append(ac_normal_1 * hours_ac * 30) 
        elif ac_size == 1.5:
            ac_normal_2 = amount_normal_ac * 1700 
            print(f"Your AC consumes around {ac_normal_2} Wh!") 
            unit.append(ac_normal_2 * hours_ac * 30) 
        elif ac_size == 2:
            ac_normal_3 = amount_normal_ac * 2400 
            print(f"Your AC consumes around {ac_normal_3} Wh!") 
            unit.append(ac_normal_3 * hours_ac * 30) 
    else:
        print("Invalid input. Please enter 'yes' or 'no'.") 
flag = True 
user_input_leds = input("Do you have any bulbs or tube lights(yes-no): ").lower() 
if user_input_leds == "yes":
    bulbs_size = input("Enter the Size of Bulbs you have(small_medium_large): ").lower() 
    if bulbs_size == "small": 
        number_small = int(input("Enter the number of small bulbs: ")) 
        hours = float(input("How many hours per day are they used?: "))
        power_small_bulbs = number_small * 2.5 
        appliance.append("Small Bulb") 
        print(f"your Bulb takes {power_small_bulbs} Wh as input!") 
        unit.append(power_small_bulbs * hours * 30) 
    elif bulbs_size == "medium": 
        number_meduim = int(input("Enter the number of medium bulbs: ")) 
        hours = float(input("How many hours per day are they used?: "))
        power_meduim_bulbs = number_meduim * 10 
        appliance.append("Medium Bulb") 
        print(f"your Bulb takes {power_meduim_bulbs} Wh as input!") 
        unit.append(power_meduim_bulbs * hours * 30) 
    elif bulbs_size == "large": 
        number_large = int(input("Enter the number of large bulbs: ")) 
        hours = float(input("How many hours per day are they used?: "))
        power_large_bulbs = number_large * 80 
        appliance.append("Large Bulb") 
        print(f"your Bulb takes {power_large_bulbs} Wh as input !") 
        unit.append(power_large_bulbs * hours * 30) 
    else: 
        print("Invalid input")
led_lights = input("Do you have any Tube lights(yes-no): ").lower() 
if led_lights == "yes": 
    count_lights = int(input("Enter the number of tube lights you have: ")) 
    hours = float(input("How many hours per day are they used?: "))
    total_lights = count_lights * 20 
    appliance.append("Tube light") 
    print(f"Your tube light takes {total_lights} Wh as input!") 
    unit.append(total_lights * hours * 30) 
elif led_lights == "no": 
    print("Moving on!") 
else: 
    print("Invalid input! (yes-no) Only!") 
print() 
thing1 = input("Do you have a washing machine(yes-no): ").lower() 
if thing1 == "yes":
    thing1_count = int(input("Enter the number of washing machines: ")) 
    thing1_inv = input("Is it an inverter model(yes-no): ").lower() 
    hours = float(input("How many hours per day is it used?: "))
    if thing1_inv == "yes": 
        thing1_power = thing1_count * 300 
    else: 
        thing1_power = thing1_count * 500 
    appliance.append("Washing Machine") 
    print(f"your Washing Machine takes {thing1_power} Watt per hour as input!") 
    unit.append(thing1_power * hours * 30) 
elif thing1 == "no": 
    print("Moving on!") 
else: 
    print("Invalid input! (yes-no) Only!") 
thing2 = input("Do you have a fridge(yes-no): ").lower() 
if thing2 == "yes":
    thing2_count = int(input("Enter the number of fridges: ")) 
    thing2_inv = input("Is it an inverter model(yes-no): ").lower() 
    hours = float(input("How many hours per day is it active?: "))
    if thing2_inv == "yes": 
        thing2_power = thing2_count * 100 
    else: 
        thing2_power = thing2_count * 200 
    appliance.append("Fridge") 
    print(f"your Fridge takes {thing2_power} Watt per hour as input!") 
    unit.append(thing2_power * hours * 30) 
elif thing2 == "no": 
    print("Moving on!") 
else: 
    print("Invalid input! (yes-no) Only!") 
thing3 = input("Do you have a pc(yes-no): ").lower() 
if thing3 == "yes":
    thing3_count = int(input("Enter the number of pcs: ")) 
    thing3_watts = float(input("Enter the wattage of your PC: "))
    hours = float(input("How many hours per day is it used?: "))
    thing3_power = thing3_count * thing3_watts
    appliance.append("PC")
    print(f"your PC takes {thing3_power} Watt per hour as input!")
    unit.append(thing3_power * hours * 30)
    if thing3_watts > 600:
        print("Nice pc")
elif thing3 == "no":
    print("Moving on!")
else:
    print("Invalid input! (yes-no) Only!")
thing4 = input("Do you have an iron(yes-no): ").lower()
if thing4 == "yes":
    thing4_count = int(input("Enter the number of irons: "))
    hours = float(input("How many hours per day is it used?: "))
    thing4_power = thing4_count * 1000
    appliance.append("Iron")
    print(f"your Iron takes {thing4_power} Watt per hour as input!")
    unit.append(thing4_power * hours * 30)
elif thing4 == "no":
    print("Moving on!")
else:
    print("Invalid input! (yes-no) Only!")
print()
print(appliance)
total_monthly_wh = sum(unit)
total_kwh_units = total_monthly_wh / 1000
print(f"⚡ Monthly Electricity Units: {total_kwh_units} kWh (Units)")
if total_kwh_units <= 50:
    rate = 3.95
    fixed = 0
elif total_kwh_units <= 100:
    rate = 7.74
    fixed = 0
elif total_kwh_units <= 200:
    rate = 28.91
    fixed = 0
elif total_kwh_units <= 300:
    rate = 33.10
    fixed = 0
elif total_kwh_units <= 400:
    rate = 37.99
    fixed = 200
elif total_kwh_units <= 500:
    rate = 40.20
    fixed = 400
elif total_kwh_units <= 600:
    rate = 41.62
    fixed = 600
elif total_kwh_units <= 700:
    rate = 42.76
    fixed = 800
else:
    rate = 47.69
    fixed = 1000
base_bill = total_kwh_units * rate
total_bill = base_bill + fixed
print(f"💰 Calculated Base Tariff Rate: PKR {rate} per Unit")
print(f"🏢 Fixed Monthly Charges: PKR {fixed}")
print(f"💵 Estimated Monthly K-Electric Bill: PKR {total_bill}")
print()
