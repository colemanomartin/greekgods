# Program to generate a light show for the logo during attract
# Invoke by typing python3 callmystery.py > nameOfShow.yaml
# import the random module
tbl = ('l_orbit_37','l_orbit_36','l_orbit_35','l_orbit_34','l_orbit_33','l_orbit_32','l_orbit_31','l_orbit_30',
'l_orbit_29','l_orbit_28','l_orbit_27','l_orbit_26','l_orbit_25','l_orbit_24','l_orbit_23',
'l_orbit_22','l_orbit_21','l_orbit_20','l_orbit_19','l_orbit_18','l_orbit_17','l_orbit_16',
'l_orbit_15','l_orbit_14','l_orbit_13','l_orbit_12','l_orbit_11','l_orbit_10','l_orbit_9',
'l_orbit_8','l_orbit_7','l_orbit_6','l_orbit_5','l_orbit_4','l_orbit_3','l_orbit_2',
'l_orbit_1','l_orbit_0') #tuplet list cannot be changed

print('#show_version=5')
for i in range(1,36):
   print('- duration: 1')
   print('  lights:')
   print('    {0}: 000033'.format(tbl[i-1]))
   print('    {0}: FFFFFF'.format(tbl[i]))
   print('    {0}: FFFFFF'.format(tbl[i+1]))
   print('    {0}: FFFFFF'.format(tbl[i+2]))
