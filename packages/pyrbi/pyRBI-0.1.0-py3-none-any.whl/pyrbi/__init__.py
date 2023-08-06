"""
Provides a simple Python client for RBI REST API
"""
from . import exceptions

import requests


__version__ = "0.1.0"


class PyRBI:
    """
    A client for RBI Blockchain's REST API

    Usage:

    Create a new instance using your credentials

    >>> cli = PyRBI("user", "pass")

    From there on you can create a new wallet, sync a wallet and put/retrieve
    data from a wallet.
    """

    def __init__(self, username, password, home="http://portohack.rbiblockchain.io"):
        """
        Creates a new client and authenticates the given user and password.

        Accepts an optional argument regarding the root of the API.
        """
        self.username = username
        self.password = password
        self.home = home

        self.auth_data = self.auth()
        self.token = self.auth_data["access_token"]

    def _call(
        self, path: str, headers=None, payload=None, method="GET", authenticate=True
    ) -> requests.Response:
        """
        _call makes a generic HTTP request to the API. It wraps around Requests
        capabilities.
        """

        # If path does no start with a '/', we add one
        path = path if (path[0] == "/") else f"/{path}"

        url = f"{self.home}{path}"
        kwargs = {}

        handler = getattr(requests, method.lower())

        if authenticate:
            if not headers:
                headers = {}

            headers["Authorization"] = f"Bearer {self.token}"

        if headers:
            # Sending the headers back to kwargs, in order to pass to handler
            kwargs["headers"] = headers

        if payload:
            if method.upper() == "POST":
                kwargs["json"] = payload
            elif method.upper() == "GET":
                kwargs["params"] = payload

        return handler(url, **kwargs)

    def auth(self):
        """
        performs an OAuth2 password-based authentication against the API
        """
        url = f"{self.home}/oauth/token"
        header = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "grant_type": "password",
            "username": self.username,
            "password": self.password,
        }
        return requests.post(url, data, headers=header).json()

    def get_mnemonic(self):
        """
        returns 12 words that can be used as mnemonics in wallet creation
        """
        return self._call("/stcpconnector/createmnemonic").json()["data"]

    def create_wallet(self):
        """
        creates a new wallet using new mnemonics
        """
        mnemonic = self.get_mnemonic()
        return self._call(
            "/stcpconnector/createwallet", method="POST", payload={"mnemonic": mnemonic}
        ).json()["data"]

    def sync_wallet(self, name, address):
        """
        syncs a wallet identified by its name and address
        """
        if not address.startswith("0x"):
            raise exceptions.InvalidWalletAddress()

        payload = {"name": name, "address": address}
        return self._call("/stcpconnector/sync", method="POST", payload=payload).json()

    def put_data(self, data, address, private_key):
        """
        puts a data string into an wallet
        """
        if not address.startswith("0x"):
            raise exceptions.InvalidWalletAddress()

        payload = {"data": data, "to": address, "from": address, "pk": private_key}

        return self._call(
            "/stcpconnector/registerdata", method="POST", payload=payload
        ).json()

    def get_data(self, transaction_hash):
        """
        returns the data input at a given transaction
        """
        payload = self._call(
            f"/stcpconnector/querytransaction/{transaction_hash}"
        ).json()

        data = payload["data"]["input"][2:]
        data = bytearray.fromhex(data).decode()[2:]
        return data
