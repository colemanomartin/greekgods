# Program to generate a light show for the logo during attract
# Invoke by typing python3 callmystery.py > nameOfShow.yaml
# import the random module

print('#show_version=5')
r = 66
for i in range(7,40):
   print('- duration: 1')
   print('  lights:')
   if (i<37):
     print('    l_orbit_{0}: FFFFFFFF'.format(i))
     print('    l_orbit_{0}: FFFFFFFF'.format(r))
   if (i<36):
     print('    l_orbit_{0}: FFFFFFFF'.format(i-1))
     print('    l_orbit_{0}: FFFFFFFF'.format(r+1))
   if (i<35):
     print('    l_orbit_{0}: FFFFFFFF'.format(i-2))
     print('    l_orbit_{0}: FFFFFFFF'.format(r+2))
   print('    l_orbit_{0}: FFFFFF00'.format(i-3))
   print('    l_orbit_{0}: FFFFFF00'.format(r+3))
   print('    l_orbit_{0}: FFFFFF00'.format(i-4))
   print('    l_orbit_{0}: FFFFFF00'.format(r+4))
   print('    l_orbit_{0}: FFFFFF00'.format(i-5))
   print('    l_orbit_{0}: FFFFFF00'.format(r+5))
   r = r -1
