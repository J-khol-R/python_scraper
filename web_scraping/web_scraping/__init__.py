from __future__ import absolute_import, unicode_literals

# Asegúrate de que la aplicación siempre se importe cuando Django se inicie.
from .celery import app as celery_app

__all__ = ('celery_app',)