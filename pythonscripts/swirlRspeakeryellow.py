# Program to generate a light show for the logo during attract
# Invoke by typing python3 GGLogoSparker1.py > nameOfShow.yaml
# import the random module

# Next time just put the table in backwards!
tbl = ('0f0f00','222200','444400','888800','cccc00','eeee00','ffff44') #tuplet list cannot be changed
#tbl = ('44ff44','00ee00','00cc00','008800','004400','002200','000f00')
#print('#show_version=5')
#for i in range(6, 0, -1):
#   print('- duration: 1')
#   print('  lights:')
 #  for j in range(49, 42, -1):
#     index = i + (j - 44)
#     print('i =',i)
#     print('j =',j)
#     print('index = ',index)
#     if index > 6:
#         index = index - 7
#     print('    l_serial_{0}: {1}'.format(j,tbl[index]))

print('#show_version=5')
for i in range(0, 7):
   print('- duration: 1')
   print('  lights:')
   for j in range(43,50):
     index = i + (j-43)
     if index > 6:
         index = index - 7
     print('    l_serial_{0}: {1}'.format(j,tbl[index]))
