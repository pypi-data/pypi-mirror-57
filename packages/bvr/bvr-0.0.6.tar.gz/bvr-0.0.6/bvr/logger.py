

class Logger:

    def __init__(self):
        self.error_prefix = "ERROR"
        self.info_prefix = "INFO"

    def error(self, msg):
        print(self.error_prefix + ": " + msg)

    def info(self, msg):  # TODO: use or delete
        print(self.info_prefix + ": " + msg)
