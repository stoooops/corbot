import abc
import os


class CorbotRunner(abc.ABC):
    """
    A runner is a class that implements a command-line interface for a
    specific task. It is responsible for parsing command-line arguments
    and executing the task.
    """

    @property
    def corbot_dir(self) -> str:
        """
        .corbot directory stores configuration files and other data.
        """
        default = os.path.join(os.path.expanduser("~"), ".corbot")
        corbot_dir = os.environ.get("CORBOT_DIR", default)
        if corbot_dir == default and not os.path.exists(default):
            os.makedirs(default)
        return corbot_dir

    @abc.abstractmethod
    def run(self, *args):
        """
        Execute the runner with the given command-line arguments.
        """
        pass
