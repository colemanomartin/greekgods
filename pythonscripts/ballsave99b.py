# Program to generate a light show for the ball save counter
# Invoke by typing python3 ballsave99b > nameOfShow.yaml
import math
#  aaaa
#  f  b
#  f  b
#  gggg
#  e  c
#  e  c
#  dddd
def printengine (value,color):
  tens = (math.trunc (value/10))*10
  ones = value - tens
  if tens == 0:
    print('    l_tens_a: '+ color)
    print('    l_tens_f: '+ color)
    print('    l_tens_b: '+ color)
    print('    l_tens_g: '+ "000000")
    print('    l_tens_e: '+ color)
    print('    l_tens_c: '+ color)
    print('    l_tens_d: '+ color)
  elif tens == 10:
    print('    l_tens_a: '+ "000000")
    print('    l_tens_f: '+ "000000")
    print('    l_tens_b: '+ color)
    print('    l_tens_g: '+ "000000")
    print('    l_tens_e: '+ "000000")
    print('    l_tens_c: '+ color)
    print('    l_tens_d: '+ "000000")
  elif tens == 20:
    print('    l_tens_a: '+ color)
    print('    l_tens_f: '+ "000000")
    print('    l_tens_b: '+ color)
    print('    l_tens_g: '+ color)
    print('    l_tens_e: '+ color)
    print('    l_tens_c: '+ "000000")
    print('    l_tens_d: '+ color)
  elif tens == 30:
    print('    l_tens_a: '+ color)
    print('    l_tens_f: '+ "000000")
    print('    l_tens_b: '+ color)
    print('    l_tens_g: '+ color)
    print('    l_tens_e: '+ "000000")
    print('    l_tens_c: '+ color)
    print('    l_tens_d: '+ color)
  elif tens == 40:
    print('    l_tens_a: '+ "000000")
    print('    l_tens_f: '+ color)
    print('    l_tens_b: '+ color)
    print('    l_tens_g: '+ color)
    print('    l_tens_e: '+ "000000")
    print('    l_tens_c: '+ color)
    print('    l_tens_d: '+ "000000")
  elif tens == 50:
    print('    l_tens_a: '+ color)
    print('    l_tens_f: '+ color)
    print('    l_tens_b: '+ "000000")
    print('    l_tens_g: '+ color)
    print('    l_tens_e: '+ "000000")
    print('    l_tens_c: '+ color)
    print('    l_tens_d: '+ color)
  elif tens == 60:
     print('    l_tens_a: '+ color)
     print('    l_tens_f: '+ color)
     print('    l_tens_b: '+ "000000")
     print('    l_tens_g: '+ color)
     print('    l_tens_e: '+ color)
     print('    l_tens_c: '+ color)
     print('    l_tens_d: '+ color)
  elif tens == 70:
     print('    l_tens_a: '+ color)
     print('    l_tens_f: '+ "000000")
     print('    l_tens_b: '+ color)
     print('    l_tens_g: '+ "000000")
     print('    l_tens_e: '+ "000000")
     print('    l_tens_c: '+ color)
     print('    l_tens_d: '+ "000000")
  elif tens == 80:
     print('    l_tens_a: '+ color)
     print('    l_tens_f: '+ color)
     print('    l_tens_b: '+ color)
     print('    l_tens_g: '+ color)
     print('    l_tens_e: '+ color)
     print('    l_tens_c: '+ color)
     print('    l_tens_d: '+ color)
  elif tens == 90:
    print('    l_tens_a: '+ color)
    print('    l_tens_f: '+ color)
    print('    l_tens_b: '+ color)
    print('    l_tens_g: '+ color)
    print('    l_tens_e: '+ "000000")
    print('    l_tens_c: '+ color)
    print('    l_tens_d: '+ "000000")
  else:
    print ('bad tens value = ',tens)
#
  if ones == 0:
    print('    l_ones_a: '+ color)
    print('    l_ones_f: '+ color)
    print('    l_ones_b: '+ color)
    print('    l_ones_g: '+ "000000")
    print('    l_ones_e: '+ color)
    print('    l_ones_c: '+ color)
    print('    l_ones_d: '+ color)
  elif ones == 1:
    print('    l_ones_a: '+ "000000")
    print('    l_ones_f: '+ "000000")
    print('    l_ones_b: '+ color)
    print('    l_ones_g: '+ "000000")
    print('    l_ones_e: '+ "000000")
    print('    l_ones_c: '+ color)
    print('    l_ones_d: '+ "000000")
  elif ones == 2:
    print('    l_ones_a: '+ color)
    print('    l_ones_f: '+ "000000")
    print('    l_ones_b: '+ color)
    print('    l_ones_g: '+ color)
    print('    l_ones_e: '+ color)
    print('    l_ones_c: '+ "000000")
    print('    l_ones_d: '+ color)
  elif ones == 3:
    print('    l_ones_a: '+ color)
    print('    l_ones_f: '+ "000000")
    print('    l_ones_b: '+ color)
    print('    l_ones_g: '+ color)
    print('    l_ones_e: '+ "000000")
    print('    l_ones_c: '+ color)
    print('    l_ones_d: '+ color)
  elif ones == 4:
    print('    l_ones_a: '+ "000000")
    print('    l_ones_f: '+ color)
    print('    l_ones_b: '+ color)
    print('    l_ones_g: '+ color)
    print('    l_ones_e: '+ "000000")
    print('    l_ones_c: '+ color)
    print('    l_ones_d: '+ "000000")
  elif ones == 5:
    print('    l_ones_a: '+ color)
    print('    l_ones_f: '+ color)
    print('    l_ones_b: '+ "000000")
    print('    l_ones_g: '+ color)
    print('    l_ones_e: '+ "000000")
    print('    l_ones_c: '+ color)
    print('    l_ones_d: '+ color)
  elif ones == 6:
     print('    l_ones_a: '+ color)
     print('    l_ones_f: '+ color)
     print('    l_ones_b: '+ "000000")
     print('    l_ones_g: '+ color)
     print('    l_ones_e: '+ color)
     print('    l_ones_c: '+ color)
     print('    l_ones_d: '+ color)
  elif ones == 7:
     print('    l_ones_a: '+ color)
     print('    l_ones_f: '+ "000000")
     print('    l_ones_b: '+ color)
     print('    l_ones_g: '+ "000000")
     print('    l_ones_e: '+ "000000")
     print('    l_ones_c: '+ color)
     print('    l_ones_d: '+ "000000")
  elif ones == 8:
     print('    l_ones_a: '+ color)
     print('    l_ones_f: '+ color)
     print('    l_ones_b: '+ color)
     print('    l_ones_g: '+ color)
     print('    l_ones_e: '+ color)
     print('    l_ones_c: '+ color)
     print('    l_ones_d: '+ color)
  elif ones == 9:
    print('    l_ones_a: '+ color)
    print('    l_ones_f: '+ color)
    print('    l_ones_b: '+ color)
    print('    l_ones_g: '+ color)
    print('    l_ones_e: '+ "000000")
    print('    l_ones_c: '+ color)
    print('    l_ones_d: '+ "000000")
  else:
    print ('bad ones value = ',ones)

# main loop
color = "00FF80"
print('#show_version=5')
for i in range(99, -1, -1):
  if i == 89:
    color = "00FF40"
  if i == 79:
    color = "00FF00" #GREEN
  if i == 69:
    color = "40FF00"
  if i == 59:
    color = "80FF00"
  if i == 49:
    color = "FFFF00" #YELLOW
  if i == 39:
    color = "FFC000"
  if i == 29:
    color = "FF8000"
  if i == 19:
    color = "FF4000"
  if i == 9:
    color = "FF0000"
  print('- duration: 1')
  print('  lights:')
  print("# i = ", i)
  printengine (i,color)
print('- duration: 4')
print('  lights:')
print("# timer expired blinks")
printengine (0,"FF0000")
print('- duration: 4')
print('  lights:')
print("# timer expired blinks")
printengine (0,"000000")
print('- duration: 4')
print('  lights:')
print("# timer expired blinks")
printengine (0,"FF0000")
print('- duration: 4')
print('  lights:')
print("# timer expired blinks")
printengine (0,"000000")
print('- duration: 4')
print('  lights:')
print("# timer expired blinks")
printengine (0,"FF0000")
print('- duration: 20')
print('  lights:')
print("# timer expired blinks")
printengine (0,"000000")
