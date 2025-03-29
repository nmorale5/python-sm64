import keyboard
import time
import pygetwindow as gw
from abc import ABC, abstractmethod

from BotCommands import Command


class BotBase(ABC):
    application_window = "Super Mario 64 Coop Deluxe"
    message_delay = .1

    def __init__(self):
        super().__init__()
        # Register hotkey to stop the bot
        keyboard.add_hotkey("ctrl+shift+x", self.stop_bot)
        self.running = True

    def stop_bot(self) -> None:
        print("\n[!] Stopping bot...")
        self.running = False

    def send_message(self, message: str) -> None:
        active_window = gw.getActiveWindow()
        if self.application_window in active_window.title:
            keyboard.send("enter")
            time.sleep(BotBase.message_delay)
            keyboard.write(message)
            keyboard.send("enter")

    def write_command(self, command: Command) -> None:
        self.send_message(command.to_message())

    @abstractmethod
    def run(self):
        raise NotImplementedError("You must implement the run() method")
