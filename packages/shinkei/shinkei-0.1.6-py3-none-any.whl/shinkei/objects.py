# -*- coding: utf-8 -*-

import re


class Version:
    """An object representing the API and singyeong version.

    Attributes
    ----------
    api: :class:`str`
        The API version, in ``vN`` format.
    singyeong: :class:`str`
        The singyeong version, in ``x.y.z`` format.
    """

    __slots__ = ("api", "singyeong")

    def __init__(self, data):
        self.api = data["api"]
        self.singyeong = data["singyeong"]

    def __repr__(self):
        return "<Version api={0.api} singyeong={0.singyeong}>".format(self)


class MetadataPayload:
    """An object representing a payload of data received from a client.

    Attributes
    ----------
    nonce
        A unique nonce used to identify the payload.
    payload: Union[:class:`str`, :class:`int`, :class:`float`, :class:`list`, :class:`dict`]
        The payload.
    """

    __slots__ = ("nonce", "payload")

    def __init__(self, data):
        self.nonce = data["nonce"]

        self.payload = data["payload"]

    def __repr__(self):
        return "<MetadataPayload nonce={0.nonce!r}>".format(self)


class VersionMetadata:
    """An object to represent a version object in :meth:`Client.update_metadata`.

    This is *NOT* the same as :class:`Version`.

    Parameters
    ----------
    fmt: :class:`str`
        The version string.
        Must be complient to the `elixir specification <https://hexdocs.pm/elixir/Version.html>`_.
    """

    __slots__ = ("fmt", "_groups")

    # from the official Semantic Versioning repo.
    VALIDATION_REGEX = re.compile(r"""
    ^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)
    (?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)
    (?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?
    (?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$
    """, re.VERBOSE)

    def __init__(self, fmt):
        match = self.VALIDATION_REGEX.match(fmt)
        if not match or not match.group(0):
            raise ValueError("Invalid version format.")

        self.fmt = fmt
        self._groups = match.groups(default="0")

    def __str__(self):
        return self.fmt

    def __repr__(self):
        return "<VersionMetadata fmt={0.fmt!r}>".format(self)

    def __eq__(self, other):
        return isinstance(other, VersionMetadata) and self._groups == other._groups

    def __ne__(self, other):
        return not self.__eq__(other)

    # this comparison with strings instead of ints is very odd
    # TODO: either remove it or change it

    def __le__(self, other):
        if isinstance(other, VersionMetadata):
            return self._groups <= other._groups
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, VersionMetadata):
            return self._groups < other._groups
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, VersionMetadata):
            return self._groups >= other._groups
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, VersionMetadata):
            return self._groups > other._groups
        return NotImplemented
