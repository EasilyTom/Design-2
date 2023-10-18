from math import pi
ap = 1  #* 10**-3
vc = 75
f = 0.05  #* 10**-3


# Roughing

rough_F_f = 120*(ap**1.2006)*(f**0.3108)
rough_F_r = 177*(ap**0.3965)*(f**0.4930)
rough_F_c = 519*(ap**0.8676)*(f**0.6943)

rough_resultant = (rough_F_f**2 + rough_F_r**2 + rough_F_c**2)**0.5
print("Task 1:")
print("rough_F_f " + str(rough_F_f))
print("rough_F_r " + str(rough_F_r))
print("rough_F_c " + str(rough_F_c))
print("rough_resultant " + str(rough_resultant))

# Spindle
P_c = (rough_F_r**2 + rough_F_c**2)**0.5
E = 200_000_000_000
a = 62.5 *10**-3
b = 106.5 * 10**-3
d_int = 0.02376
L = 0.1
x = a + b + L

I = pi*((0.045**4)-(d_int**4))/64
beam_deflection = (-P_c / (6*E*I)) * (
                                  - ((a+b)/L)*(x**3)
                                  + (1+ ((a+b)/L))*((x-L)**3)
                                  + ((a+b)*L*x)
                              )

print("Task 2: \nbeam_deflection " + str(beam_deflection*1000000) + 'um')
# Bearings

K_A = 350_000_000
K_B = 190_000_000

R_A = ((L+a+b)/L) * P_c
R_B = ((a+b)/L) * P_c

D_b_A = R_A / K_A
D_b_B = R_B / K_B
bearing_deflection = (((D_b_A + D_b_B)/L) * (a+b)) + D_b_A
print("bearing_deflection " +str(bearing_deflection*1000000) + 'um')

# Total
total_deflection = beam_deflection + bearing_deflection
print("Total deflection " + str(total_deflection*1000000) + 'um')
print("L: " + str(L) + "m")
print("d_ext: 0.045m")
print("d_int: " + str(d_int) + "m")
print("Total volume: " + str(pi*L*(0.045**2 - d_int**2)) + "m^3")


# Task 3
print("Task 3: ")
print("C_r A: " + str(R_A*4))
print("C_r B: " + str(R_B*4))
print("C_a: " + str(rough_F_f*2))
print("Front: 7309BEA")
print("Rear: 6009")
print("TODO, draw schematic diagram. Flange on one side, groove for circlip on other")
# Task 4
print("Task 4:")
F_v = rough_F_c
  # Say there's 100mm between rails
z_1 = 0.030
z_2 = 0.100
R_3z = z_1*F_v/z_2
R_1z = (z_1+z_2)*F_v/z_2

print("R_1z: " + str(R_1z))
print("R_3z: " + str(R_3z))

print("Min x carriage req: " + str(max([R_1z, R_3z])*2))

# Z
z_3 = 0.015
z_4 = 0.100
R_7z = z_3*F_v/z_4
R_5z = (z_3+z_4)*F_v/z_4

print("R_5z: " + str(R_5z))
print("R_7z: " + str(R_7z))

print("Min z carriage req: " + str(max([R_5z, R_7z])*2))

# Task 5
print("Task 5: ")
print("Axial load on lead screw: " + str(rough_F_f))
lead = 4
efficiency = 0.59
torque = rough_F_f*lead/(2*pi*efficiency)
print("Torque: " + str(torque) + "N/mm")
rpm = 75/(0.04 * pi)
linear_speed = rpm * 0.05
print('Linear speed: ' + str(linear_speed) + 'mm/min')
print()

#print("Shaft: 10mm diameter, 4mm lead")
#print("Nut: XCB3700")
#print("Screw bearing: 6000")

