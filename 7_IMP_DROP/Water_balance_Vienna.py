
PC_annual_mean = 0.583 #m³  #583 mm -> l/m² -> 0.001m³/m²
Area_Wien = 414600000 #   #414.6 km²

Water_per_day = (Area_Wien*PC_annual_mean)/365
print(Water_per_day)

Donau_hw = 14000*60*60*24 # 14000 m³/s Hochwasser
Donau_mw = 2000*60*60*24 # 2000 m³/s Mittelwasser

print(Donau_hw) #1209600000