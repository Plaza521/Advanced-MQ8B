class EmulatorError(Exception):
    def __init__(self, *args, **kwargs):
        super(EmulatorError, self).__init__(*args, **kwargs)
