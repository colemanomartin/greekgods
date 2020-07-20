# Program to generate a light show for the logo during attract
# Invoke by typing python3 GGLogoSparker1.py > nameOfShow.yaml
# import the random module
tbl = ('000044','000066','000088','0000aa','0000cc','0000ee','aaaaff') #tuplet list cannot be changed
print('#show_version=5')
for i in range(0, 7):
   print('- duration: 1')
   print('  lights:')
   for j in range(0,7):
     index = i + j
     if index > 6:
         index = index - 7
     print('    l_serial_{0}: {1}'.format(j,tbl[index]))
