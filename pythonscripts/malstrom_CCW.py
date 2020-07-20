# Program to generate a light show for the whirlpool during attract
# Invoke by typing python3 malstrom.py > nameOfShow.yaml
# import the random module


tbl = ('000011','000033','000055','000088','0000FF') #tuplet list cannot be changed
#tbl = ('0000FF','000088','000055','000033','000011') #tuplet list clockwise

print('#show_version=5')
for i in range(4, -1, -1):
   print('- duration: 1')
   print('  lights:')
   print('  i={0}'.format(i))
   for j in range(4,-1,-1):
     index = i + j
     print('  j={0}'.format(j))
     print('  index={0}'.format(index))
     print('    l_malstrom_{0}: {1}'.format(j,tbl[index]))
