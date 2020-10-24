# Program to generate a light show for the playfield during attract
# Invoke by typing python3 randomparalell.py > nameOfShow.yaml
# import the random modules

import random

tbl = ('l_hydra_2',
'l_hydra_center',
'l_hydra_top',
'l_hydra_7',
'l_hydra_10',
'l_left_ss_bottom',
'l_left_ss_middle',
'l_left_ss_top',
'l_ones_a',
'l_ones_b',
'l_ones_c',
'l_ones_d',
'l_ones_e',
'l_ones_f',
'l_ones_g',
'l_tens_a',
'l_tens_b',
'l_tens_c',
'l_tens_d',
'l_tens_e',
'l_tens_f',
'l_tens_g',
'l_hydra_4',
'l_hydra_bottom',
'l_3xflasher',
'l_2xflasher',
'l_left_inlane',
'l_left_pop_band',
'l_left_pop_lower_arrow',
'l_left_pop_upper_arrow',
'l_left_outlane',
'l_left_spinner_band_lower',
'l_left_orbit_spinner',
'l_left_spinner_band_upper',
'l_left_orbit_lower_triangle',
'l_malstrom_4',
'l_malstrom_3',
'l_left_sis_arrow',
'l_malstrom_triangle',
'l_poseidon_fish_right',
'l_poseidon_right_sling_upper',
'l_poseidon_right_sling_lower',
'l_poseidon_fish_left',
'l_poseidon_left_sling_upper',
'l_poseidon_left_sling_middle',
'l_poseidon_left_sling_lower',
'l_poseidon_fish_middle',
'l_malstrom_2',
'l_malstrom_1',
'l_malstrom_0',
'l_left_orbit_upper_triangle',
'l_poseidon_band_right_lower',
'l_poseidon_band_left_lower',
'l_poseidon_pop',
'l_left_side_pop',
'l_ramp_left',
'l_ramp_right',
'l_olympus_magnet',
'l_olympus_band_upper_left',
'l_roof_left_2',
'l_roof_left_3',
'l_poseidon_lock_distal',
'l_poseidon_lock_prox',
'l_poseidon_magnet', # driver 2 header 6
'l_poseidon_band_left_upper',
'l_roof_left_5',
'l_roof_left_4',
'l_roof_center', #Driver 2 J7
'l_hideyhole',
'l_roof_left_1',
'l_poseidion_band_right_upper',
'l_roof_right_2',
'l_roof_right_3',
'l_roof_right_4',
'l_roof_right_1',
'l_roof_right_5',
'l_olympus_band_upper_right',
'l_olympus_band_lower_right',
'l_olympus_cloud',
'l_revealed_slingshot_flasher',
'l_olympus_lock_distal',
'l_olympus_lock_prox',
'l_right_sis_arrow',
'l_middle_drop_arrow',
'l_right_outlane',
'l_distal_drop_arrow',
'l_backlight_rgb',
'l_sis_flash_right',
'l_sis_flash_left',
'l_prox_drop_arrow',
'l_ramp_arrow',
'l_right_ss_bottom',
'l_right_ss_middle',
'l_right_ss_top',
'l_right_inlane',
'l_lightning',
'l_olympus_gate_triangle',
'l_olympus_spinner',
'l_right_orbit_triangle')
print('#show_version=5')
for i in range(0, 10):
   print('- duration: 1')
   print('  lights:')
   for j in range(0,99):
     r = random.randint(0,255)
     g = random.randint(0,255)
     b = random.randint(0,255)
     print('    {0}: {1}{2}{3}'.format(tbl[j],hex(r)[2:],hex(g)[2:],hex(b)[2:]))