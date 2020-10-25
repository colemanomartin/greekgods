# Program to generate a light show for the logo during attract
# Invoke by typing python3 callmystery.py > nameOfShow.yaml
# import the random module

print('#show_version=5')
for i in range(66,0,-1):
   print('- duration: 1')
   print('  lights:')
   print('    l_orbit_{0}: FFFFFF'.format(i))
   print('    l_orbit_{0}: FFFFFF'.format(i+1))
   print('    l_orbit_{0}: FFFFFF'.format(i+2))
   if (i<66):
     print('    l_orbit_{0}: 000033'.format(i+3))
