# Program to create the yaml for the config for all those serial LEDs on the PF
# Invoke by typing python3 ledconfigmaker.py > scrap.yaml

boardID=0
first_valid_led_on_segment=500 #defigned as ws281x_n first address
led_width = 3 # RGB

first_yaml_num_in_ROI = 0 #derived from drawing showing my count of LEDs 
total_leds_in_AOI = 12

cntr = first_valid_led_on_segment #within loop counter
led_number_in_ROI = cntr - first_valid_led_on_segment
print('#right inlane serial leds')
for i in range(1, 55):
   print('  l_r_inlane_{0}:'.format(i))
   print('    number: {0}-{1}-{2}-{3} #flipper string LED {4}'.format(boardID,cntr,cntr+1,cntr+2,led_number_in_ROI))
   print('    type: grb')
   print('    subtype: led')
   cntr = cntr + led_width
   led_number_in_ROI = led_number_in_ROI + 1
index = 0
for i in range(28, 14, -1):
   index = index +3
print(index)
#print('#right outlane serial leds')
#for i in range(28, 14. -1):
#   print('  l_r_outlane_{0}:'.format(i))
#   print('    number: {0}-{1}-{2}-{3} #flipper string LED {4}'.format(boardID,cntr,cntr+1,cntr+2,led_number))
#   print('    type: grb')
#   print('    subtype: led')
#   cntr = cntr +3
#   led_number = led_number + 1

