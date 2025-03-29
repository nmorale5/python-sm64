import time

from BotBase import BotBase
from BotCommands import KillCommand


class KillBot(BotBase):
    def __init__(self, kill_frequency=60):
        super().__init__()
        self.kill_frequency = kill_frequency

    def run(self):
        while self.running:
            self.write_command(KillCommand("60 second have passed"))
            time.sleep(self.kill_frequency)
