from mpf.core.mode import Mode
import random

class stop_player_add(Mode):

    def mode_init(self):
        self.log.info('stop_player_add mode_init')

    def mode_start(self, **kwargs):
        self.log.info('stop_player_add mode_start')
        self.add_mode_event_handler('player_add_request', self.block_add)

    def block_add(self, **kwargs):
        return False

    def mode_stop(self, **kwargs):
        self.machine.events.post('stop_player_add_mode_ended')
        self.log.info('stop_player_add mode_stop')
#based on wolfmarch
# Adding custom code at a machine level http://developer.missionpinball.org/en/dev/code/machine_code.html
# I'm told this registers a device handler that returns false to add_player when mode is running
