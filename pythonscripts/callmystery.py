# Program to generate a light show for the logo during attract
# Invoke by typing python3 callmystery.py > nameOfShow.yaml
# import the random module

print('#show_version=5')
for i in range(7,37):
   print('- duration: 1')
   print('  lights:')
   print('    l_orbit_{0}: FFFFFFFF'.format(i+2))
   print('    l_orbit_{0}: FFFFFFFF'.format(i+61))
   print('    l_orbit_{0}: FFFFFFFF'.format(i+1))
   print('    l_orbit_{0}: FFFFFFFF'.format(i+62))
   print('    l_orbit_{0}: FFFFFFFF'.format(i+0))
   print('    l_orbit_{0}: FFFFFFFF'.format(i+63))
   print('    l_orbit_{0}: FFFFFF00'.format(i-1))
   print('    l_orbit_{0}: FFFFFF00'.format(i+64))
   print('    l_orbit_{0}: FFFFFF00'.format(i-2))
   print('    l_orbit_{0}: FFFFFF00'.format(i+65))
   print('    l_orbit_{0}: FFFFFF00'.format(i-3))
   print('    l_orbit_{0}: FFFFFF00'.format(i+66))
