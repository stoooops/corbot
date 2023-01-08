import abc


class CorbotRunner(abc.ABC):
    """
    A runner is a class that implements a command-line interface for a
    specific task. It is responsible for parsing command-line arguments
    and executing the task.
    """

    @abc.abstractmethod
    def run(self, *args):
        """
        Execute the runner with the given command-line arguments.
        """
        pass
