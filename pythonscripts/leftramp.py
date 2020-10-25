# Program to generate a light show for the logo during attract
# Invoke by typing python3 callmystery.py > nameOfShow.yaml
# import the random module

print('#show_version=5')
r = 66
for i in range(39,65):
   print('- duration: 1')
   print('  lights:')
   print('    l_orbit_{0}: FFFFFF'.format(i))
   if (i<65):
     print('    l_orbit_{0}: FFFFFF'.format(i-1))
   if (i<65):
     print('    l_orbit_{0}: FFFFFF'.format(i-2))
   if (i<65):
     print('    l_orbit_{0}: 000033'.format(i-3))
