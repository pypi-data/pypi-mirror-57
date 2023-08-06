# -*- coding: utf-8 -*-

import threading

from .gateway import WSClient

class KeepAlivePls(threading.Thread):
    # noinspection PyMissingConstructor
    def __init__(self, *args, ws: WSClient, **kwargs) -> None: ...

    ws: WSClient
    interval: float
    stop_event: threading.Event
    _last_ack: float
    _last_send: float
    latency: float

    def run(self) -> None: ...

    def stop(self) -> None: ...

    def ack(self) -> None: ...
