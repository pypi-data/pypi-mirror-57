# -*- coding: utf-8 -*-

import asyncio

# noinspection PyPackageRequirements
from yarl import URL

from ..api import APIClient
from ..client import Client
from ..gateway import WSClient


class BotWSClient(WSClient):
    @staticmethod
    def set_attrs(ws, client, *, reconnect):
        super().set_attrs(ws, client, reconnect=reconnect)

        # noinspection PyUnresolvedReferences
        ws.bot = client.bot

    def _dispatch(self, name, *args):
        self.bot.dispatch("shinkei_{0}".format(name), *args)


class BotClient(Client):
    # noinspection PyMethodOverriding
    @classmethod
    async def _connect(cls, url, rest_url, application_id, client_id, auth=None, *, reconnect=True,
                       session=None, loop=None, tags=None, **kwargs):
        self = cls()

        try:
            self.bot = kwargs.pop("bot")
        except KeyError:
            raise TypeError("bot must always be provided when using BotClient")

        self.loop = loop or self.bot.loop

        self.auth = auth
        self.id = client_id
        self.app_id = application_id
        self.tags = tags

        ws_url = URL(url).with_query("encoding=json") / "gateway" / "websocket"
        scheme = self.schema_map.get(ws_url.scheme, ws_url.scheme)

        self.ws_url = ws_url.with_scheme(scheme)
        self.reconnect = reconnect

        coro = BotWSClient.create(self, self.ws_url, reconnect=self.reconnect)
        self._ws = await asyncio.wait_for(coro, timeout=20)

        self._rest = await APIClient.create(rest_url, session=session, auth=auth, loop=self.loop)

        self.version = self._rest.version

        self._task = self.loop.create_task(self._poll_data())

        return self

    def add_handler(self, handler):
        """Events are now handled by bot listeners so this method now raises a :exc:`NotImplementedError`."""
        raise NotImplementedError("add_handler() cannot be used with BotClient "
                                  "(events are dispatched through bot.dispatch('shinkei_{event_name}'))")

    def remove_handler(self, handler_name):
        """Events are now handled by bot listeners so this method now raises a :exc:`NotImplementedError`."""
        raise NotImplementedError("remove_handler() cannot be used with BotClient "
                                  "(events are dispatched through bot.dispatch('shinkei_{event_name}'))")

    async def wait_for(self, event, *, timeout=None, check=None):
        """Proxy to :meth:`discord.Client.wait_for`."""
        return await self.bot.wait_for(event, timeout=timeout, check=check)
