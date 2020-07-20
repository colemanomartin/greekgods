# Program to generate a light show for the logo during attract
# Invoke by typing python3 GGLogoSparker1.py > nameOfShow.yaml
# import the random module
tbl = ('000f00','002200','004400','008800','00cc00','00ee00','44ff44') #tuplet list cannot be changed
print('#show_version=5')
for i in range(0, 7):
   print('- duration: 1')
   print('  lights:')
   for j in range(0,7):
     index = i + j
     if index > 6:
         index = index - 7
     print('    l_serial_{0}: {1}'.format(j,tbl[index]))
