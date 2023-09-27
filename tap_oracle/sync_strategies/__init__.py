class DBPrivilegeError(Exception):
    def __init__(self, msg, oracle_error, *args, **kwargs):
        super().__init__(msg, *args, **kwargs)
        self.oracle_error = oracle_error
