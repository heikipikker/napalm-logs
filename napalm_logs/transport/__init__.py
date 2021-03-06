# -*- coding: utf-8 -*-
'''
napalm-logs pluggable publisher.
'''
from __future__ import absolute_import
from __future__ import unicode_literals

# Import python std lib
import logging

# Import napalm-logs pkgs
# Exceptions
from napalm_logs.exceptions import InvalidTransportException
# Transport classes
from napalm_logs.transport.zeromq import ZMQTransport
from napalm_logs.transport.cli import CLITransport
from napalm_logs.transport.log import LogTransport
# extras: require additional underlying libraries
from napalm_logs.transport.kafka import HAS_KAFKA
from napalm_logs.transport.kafka import KafkaTransport
# from napalm_logs.transport.kafka import KafkaTransport
# from napalm_logs.transport.rabbitmq import RabbitMQTransport

log = logging.getLogger(__file__)

TRANSPORT_LOOKUP = {
    'zeromq': ZMQTransport,
    'zmq': ZMQTransport,
    'cli': CLITransport,
    'print': CLITransport,
    'console': CLITransport,
    'log': LogTransport,
    # 'rmq': RabbitMQransport,
    # 'rabbitmq': RabbitMQransport,
    '*': ZMQTransport
}

if HAS_KAFKA:
    log.info('Kafka dependency seems to be installed, making kafka transport available.')
    TRANSPORT_LOOKUP['kafka'] = KafkaTransport


def get_transport(name):
    '''
    Return the transport class.
    '''
    try:
        log.debug('Using %s as transport', name)
        return TRANSPORT_LOOKUP[name]
    except KeyError:
        msg = 'Transport {} is not available. Are the dependencies installed?'.format(name)
        log.error(msg, exc_info=True)
        raise InvalidTransportException(msg)


__all__ = (
    'get_transport',
)
