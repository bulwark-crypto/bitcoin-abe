# Copyright(C) 2014 by Abe developers.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public
# License along with this program.  If not, see
# <http://www.gnu.org/licenses/agpl.html>.

from .NIST5Chain import NIST5Chain

class Bulwark(NIST5Chain):
    def __init__(chain, **kwargs):
        chain.name = 'Bulwark'
        chain.code3 = 'BWK'
        chain.address_version = '\x55'
        chain.script_addr_vers = '\x12'
        chain.magic = '\x08\x02\x01\x17'
        NIST5Chain.__init__(chain, **kwargs)

    datadir_conf_file_name = 'bulwark.conf'
    datadir_rpcport = 52541 
    datadir_p2pport = 52543
