from abc import ABC, abstractmethod


class Command(ABC):
    @staticmethod
    @abstractmethod
    def static_command_name() -> str:
        pass

    @property
    @abstractmethod
    def command_args(self) -> tuple[str]:
        pass

    def to_message(self) -> str:
        return str(self)

    def __str__(self):
        return f"/bot_{self.static_command_name()} {' '.join(self.command_args)}"

    def __repr__(self):
        return str(self)


class KillCommand(Command):
    def __init__(self, reason=""):
        super().__init__()
        if reason == "":
            self._command_args = ()
        else:
            self._command_args = (reason,)

    @staticmethod
    def static_command_name() -> str:
        return "kill"

    @property
    def command_args(self) -> tuple[str]:
        return self._command_args
