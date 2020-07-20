# Program to generate a light show for the celestrial mb modet
# Invoke by typing python3 randomparalell.py > nameOfShow.yaml
## https://htmlcolorcodes.com/color-names/


#table includes all lights except ball save, light curtain, sis flashers
tbl = ('l_hydra_2',
'l_scoop_tongue',
'l_left_side_pop',
'l_poseidon_pop',
'l_olympus_lower_pop',
'l_olympus_right_pop',
'l_olympus_left_pop',
'l_hydra_center',
'l_hydra_top',
'l_hydra_7',
'l_hydra_10',
'l_left_sling_prox',
'l_left_sling_middle',
'l_left_sling_distal',
'l_hydra_4',
'l_hydra_bottom',
'l_3xflasher',
'l_2xflasher',
'l_left_inlane',
'l_left_pop_band',
'l_left_pop_lower_arrow',
'l_left_pop_upper_arrow',
'l_left_outlane',
'l_left_spinner_band_prox',
'l_left_orbit_spinner',
'l_left_spinner_band_distal',
'l_left_orbit_lower_triangle',
'l_malstrom_4',
'l_malstrom_3',
'l_left_sis_arrow',
'l_malstrom_triangle',
'l_poseidon_fish_right',
'l_poseidon_right_sling',
'l_poseidon_fish_left',
'l_poseidon_left_sling_distal',
'l_poseidon_left_sling_middle',
'l_poseidon_left_sling_prox',
'l_poseidon_fish_middle',
'l_malstrom_2',
'l_malstrom_1',
'l_malstrom_0',
'l_left_orbit_upper_triangle',
'l_poseidon_band_right_prox',
'l_poseidon_band_left_prox',
'l_ramp_left',
'l_ramp_right',
'l_olympus_magnet',
'l_olympus_band_upper_left',
'l_roof_left_2',
'l_roof_left_3',
'l_poseidon_lock_distal',
'l_poseidon_lock_prox',
'l_poseidon_magnet', # driver 2 header 6
'l_poseidon_band_left_distal',
'l_roof_left_5',
'l_roof_left_4',
'l_roof_center', #Driver 2 J7
'l_hideyhole',
'l_roof_left_1',
'l_poseidion_band_right_distal',
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
#'l_backlight_rgb',
#'l_sis_flash_right',
#'l_sis_flash_left',
'l_prox_drop_arrow',
'l_ramp_arrow',
'l_right_sling_prox',
'l_right_sling_middle',
'l_right_sling_distal',
'l_right_inlane',
'l_lightning',
'l_olympus_gate_triangle',
'l_olympus_spinner',
'l_right_orbit_triangle',
'l_r_inlane_0',
'l_r_inlane_1',
'l_r_inlane_2',
'l_r_inlane_3',
'l_r_inlane_4',
'l_r_inlane_5',
'l_r_inlane_6',
'l_r_inlane_7',
'l_r_inlane_8',
'l_r_inlane_9',
'l_r_inlane_10',
'l_r_inlane_11',
'l_r_inlane_12',
'l_r_outlane_0',
'l_r_outlane_1',
'l_r_outlane_2',
'l_r_outlane_3',
'l_r_outlane_4',
'l_r_outlane_5',
'l_r_outlane_6',
'l_r_outlane_7',
'l_r_outlane_8',
'l_r_outlane_9',
'l_r_outlane_10',
'l_r_outlane_11',
'l_r_outlane_12',
'l_r_outlane_13',
'l_l_inlane_0',
'l_l_inlane_1',
'l_l_inlane_2',
'l_l_inlane_3',
'l_l_inlane_4',
'l_l_inlane_5',
'l_l_inlane_6',
'l_l_inlane_7',
'l_l_inlane_8',
'l_l_inlane_9',
'l_l_inlane_10',
'l_l_inlane_11',
'l_l_inlane_12',
'l_l_outlane_0',
'l_l_outlane_1',
'l_l_outlane_2',
'l_l_outlane_3',
'l_l_outlane_4',
'l_l_outlane_5',
'l_l_outlane_6',
'l_l_outlane_7',
'l_l_outlane_8',
'l_l_outlane_9',
'l_l_outlane_10',
'l_l_outlane_11',
'l_l_outlane_12',
'l_l_outlane_13',
'l_shooter_0',
'l_shooter_1',
'l_shooter_2',
'l_shooter_3',
'l_shooter_4',
'l_shooter_5',
'l_shooter_6',
'l_shooter_7',
'l_shooter_8',
'l_shooter_9',
'l_shooter_10',
'l_shooter_11',
'l_shooter_12',
'l_shooter_13',
'l_shooter_14',
'l_shooter_15',
'l_shooter_16',
'l_shooter_17',
'l_shooter_18',
'l_shooter_19',
'l_shooter_20',
'l_shooter_21',
'l_shooter_22',
'l_shooter_23',
'l_shooter_24',
'l_shooter_25',
'l_shooter_26',
'l_shooter_27',
'l_shooter_28',
'l_shooter_29',
'l_shooter_30',
'l_shooter_31',
'l_shooter_32',
'l_shooter_33',
'l_shooter_34',
'l_shooter_35',
'l_shooter_36',
'l_shooter_37',
'l_shooter_38',
'l_shooter_39',
'l_shooter_40',
'l_shooter_41',
'l_right_shoulder_15',
'l_right_shoulder_14',
'l_right_shoulder_13',
'l_right_shoulder_12',
'l_right_shoulder_11',
'l_right_shoulder_10',
'l_right_shoulder_9',
'l_right_shoulder_8',
'l_right_shoulder_7',
'l_right_shoulder_6',
'l_right_shoulder_5',
'l_right_shoulder_4',
'l_right_shoulder_3',
'l_right_shoulder_2',
'l_right_shoulder_1',
'l_right_shoulder_0',
'l_orbit_0',
'l_orbit_1',
'l_orbit_2',
'l_orbit_3',
'l_orbit_4',
'l_orbit_5',
'l_orbit_6',
'l_orbit_7',
'l_orbit_8',
'l_orbit_9',
'l_orbit_10',
'l_orbit_11',
'l_orbit_12',
'l_orbit_13',
'l_orbit_14',
'l_orbit_15',
'l_orbit_16',
'l_orbit_17',
'l_orbit_18',
'l_orbit_19',
'l_orbit_20',
'l_orbit_21',
'l_orbit_22',
'l_orbit_23',
'l_orbit_24',
'l_orbit_25',
'l_orbit_26',
'l_orbit_27',
'l_orbit_28',
'l_orbit_29',
'l_orbit_30',
'l_orbit_31',
'l_orbit_32',
'l_orbit_33',
'l_orbit_34',
'l_orbit_35',
'l_orbit_36',
'l_orbit_37',
'l_orbit_38',
'l_orbit_39',
'l_orbit_40',
'l_orbit_41',
'l_orbit_42',
'l_orbit_43',
'l_orbit_44',
'l_orbit_45',
'l_orbit_46',
'l_orbit_47',
'l_orbit_48',
'l_orbit_49',
'l_orbit_50',
'l_orbit_51',
'l_orbit_52',
'l_orbit_53',
'l_orbit_54',
'l_orbit_55',
'l_orbit_56',
'l_orbit_57',
'l_orbit_58',
'l_orbit_59',
'l_orbit_60',
'l_orbit_61',
'l_orbit_62',
'l_orbit_63',
'l_orbit_64',
'l_orbit_65',
'l_orbit_66',
'l_orbit_67',
'l_orbit_68',
'l_left_pop_13',
'l_left_pop_12',
'l_left_pop_11',
'l_left_pop_10',
'l_left_pop_9',
'l_left_pop_8',
'l_left_pop_7',
'l_left_pop_6',
'l_left_pop_5',
'l_left_pop_4',
'l_left_pop_3',
'l_left_pop_2',
'l_left_pop_1',
'l_left_pop_0',
'l_left_shoulder_14',
'l_left_shoulder_13',
'l_left_shoulder_12',
'l_left_shoulder_11',
'l_left_shoulder_10',
'l_left_shoulder_9',
'l_left_shoulder_8',
'l_left_shoulder_7',
'l_left_shoulder_6',
'l_left_shoulder_5',
'l_left_shoulder_4',
'l_left_shoulder_3',
'l_left_shoulder_2',
'l_left_shoulder_1',
'l_left_shoulder_0')

print('#show_version=5')
print('- duration: 1')
print('  lights:')
for j in range(0,85):
  print('    {0}:'.format(tbl[j]))
  print('      color: FF0000') #RED
  print('      fade: 500ms')
for j in range(86,295):
  print('    {0}:'.format(tbl[j]))
  print('      color: 360000') #Calculator hex color/4
  print('      fade: 500ms')
print('- duration: 1')
print('  lights:')
for j in range(0,85):
  print('    {0}:'.format(tbl[j]))
  print('      color: FFA500') #full brightness orange
  print('      fade: 500ms')
for j in range(86,295):
  print('    {0}:'.format(tbl[j]))
  print('      color: 362900') #Calculator hex color/4
  print('      fade: 500ms')
print('- duration: 1')
print('  lights:')
for j in range(0,85):
  print('    {0}:'.format(tbl[j]))
  print('      color: FFFF00') #Yellow
  print('      fade: 500ms')
for j in range(86,295):
  print('    {0}:'.format(tbl[j]))
  print('      color: 363600') #Calculator hex color/4
  print('      fade: 500ms')
print('- duration: 1')
print('  lights:')
for j in range(0,85):
  print('    {0}:'.format(tbl[j])) #Green
  print('      color: 00FF00')
  print('      fade: 500ms')
for j in range(86,295):
  print('    {0}:'.format(tbl[j]))
  print('      color: 003600') #Calculator hex color/4
  print('      fade: 500ms')
print('- duration: 1')
print('  lights:')
for j in range(0,85):
  print('    {0}:'.format(tbl[j])) #Blue
  print('      color: 0000FF')
  print('      fade: 500ms')
for j in range(86,295):
  print('    {0}:'.format(tbl[j]))
  print('      color: 000036') #Calculator hex color/4
  print('      fade: 500ms')
print('- duration: 1')
print('  lights:')
for j in range(0,85):
  print('    {0}:'.format(tbl[j])) #Indigo
  print('      color: 4B0082')
  print('      fade: 500ms')
for j in range(86,295):
  print('    {0}:'.format(tbl[j]))
  print('      color: 130061') #Calculator hex color/4
  print('      fade: 500ms')
print('- duration: 1')
print('  lights:')
for j in range(0,85):
  print('    {0}:'.format(tbl[j])) #Violet
  print('      color: EE82EE')
  print('      fade: 500ms')
for j in range(86,295):
  print('    {0}:'.format(tbl[j]))
  print('      color: 392139') #Calculator hex color/4
  print('      fade: 500ms')
