# Program to generate a light show for the whirlpool during attract
# Invoke by typing python3 malstrom.py > nameOfShow.yaml
# import the random module


tbl = ('000011','000033','000055','000088','0000FF') #tuplet list cannot be changed
#tbl = ('0000FF','000088','000055','000033','000011') #tuplet list clockwise

print('#show_version=5')
for i in range(0, 5):
   print('- duration: 1')
   print('  lights:')
   for j in range(0,5):
     index = i + (j)
     if index > 4:
         index = index - 5
     print('    l_malstrom_{0}: {1}'.format(j,tbl[index]))
