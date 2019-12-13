# -*- coding: utf-8 -*-

# flake8: noqa
from .serializer import EncryptedSerializer
from .session import EncryptedCookieSessionFactory
from .scripts import generate_secret
from .utils import session_factory_from_settings


def includeme(config):
    session_factory = session_factory_from_settings(config.registry.settings)
    config.set_session_factory(session_factory)
