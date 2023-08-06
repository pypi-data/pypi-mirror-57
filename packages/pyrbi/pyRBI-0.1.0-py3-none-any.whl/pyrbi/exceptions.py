class PyRBIException(Exception):
    """
    Base exception
    """


class InvalidWalletAddress(PyRBIException):
    def __init__(self):
        super(InvalidWalletAddress, self).__init__(
            "Please check if the address starts with 0x"
        )

