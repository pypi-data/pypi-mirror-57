"""
Copyright © 2019 Ralph Seichter

Graciously sponsored by sys4 AG <https://sys4.de/>

This file is part of automx2.

automx2 is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

automx2 is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with automx2. If not, see <https://www.gnu.org/licenses/>.
"""
import logging

IDENTIFIER = 'automx2'  # Do not change this!
VERSION = '2019.0'

PLACEHOLDER_ADDRESS = r'%EMAILADDRESS%'
PLACEHOLDER_DOMAIN = r'%EMAILDOMAIN%'
PLACEHOLDER_LOCALPART = r'%EMAILLOCALPART%'


class AutomxException(Exception):
    """Exception base class for this application."""
    pass


class InvalidEMailAddressError(AutomxException):
    """Email address is invalid/unparseable."""
    pass


class DomainNotFound(AutomxException):
    """Database did not contain the given domain."""
    pass


class NoProviderForDomain(AutomxException):
    """Database did not contain a provider for the given address."""
    pass


class NoServersForDomain(AutomxException):
    """Database did not contain any servers for the given address."""
    pass


class InvalidServerType(AutomxException):
    """Database contains an invalid server type."""
    pass


class InvalidAuthenticationType(AutomxException):
    """Database contains an invalid authentication type."""
    pass


log = logging.getLogger(__name__)
_handler = logging.StreamHandler()
_handler.setFormatter(logging.Formatter())
log.addHandler(_handler)
log.setLevel(logging.DEBUG)
log.warning(f'Running {IDENTIFIER} version {VERSION}')
