from mpf.core.mode import Mode

from mpf.core.platform import SwitchSettings, DriverSettings

from mpf.platforms.interfaces.driver_platform_interface import PulseSettings

#based on popup post code NBX
# Adding custom code at a machine level http://developer.missionpinball.org/en/dev/code/machine_code.html
# [...]

class river_a_fast(Mode):
    def mode_start(self, **kwargs):
        self.log.info('******************** registering mode A handler')
        self.add_mode_event_handler('accelerate_a', self.enable_a)


    def enable_a(self, **kwargs):
        self.log.info('******************** sending Jans A rules')
        enable_switch = self.machine.switches['s_u_left_ear_3']
        disable_switch = self.machine.switches['s_u_left_ear_2']
        coil = self.machine.coils['c_u_left_magnet']
        pulse_settings = PulseSettings(duration=150, power=1.0)
        # add rule to pulse coil when switch is hit. this will work with any platform in MPF
        # https://github.com/missionpinball/mpf/blob/aca0d81a3b873514090af18ef80a9627419aed23/mpf/core/platform.py#L430
        self.machine.default_platform.set_pulse_on_hit_rule(SwitchSettings(enable_switch.hw_switch, invert=True, debounce=False),
                                                            DriverSettings(coil.hw_driver, pulse_settings, None, True))
        # p-roc specific part for disable
        self.machine.default_platform._add_release_disable_rule_to_switch(SwitchSettings(disable_switch.hw_switch, invert=True, debounce=False),
                                                                          DriverSettings(coil.hw_driver, None, None, True))
        self.machine.default_platform._write_rules_to_switch(SwitchSettings(disable_switch.hw_switch, False, False),
                                                             DriverSettings(coil.hw_driver, None, None, True), False)

    def mode_stop(self, **kwargs):
        self.log.info('******************** clearing Jans A rules')
        enable_switch = self.machine.switches['s_u_left_ear_3']
        disable_switch = self.machine.switches['s_u_left_ear_2']
        coil = self.machine.coils['c_u_left_magnet']
        self.machine.default_platform.clear_hw_rule(SwitchSettings(enable_switch.hw_switch, invert=True, debounce=False),
                                                            DriverSettings(coil.hw_driver, None, None, True))

        self.machine.default_platform.clear_hw_rule(SwitchSettings(disable_switch.hw_switch, invert=True, debounce=False),
                                                                          DriverSettings(coil.hw_driver, None, None, True))
