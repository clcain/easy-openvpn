#!/usr/bin/env python3

import argparse
import os
import sys

class OVPN:

    def __init__(self):
        self.commands = [
            'init',
            'status',
            'server-config',
            'client-config',
            'clients',
            'add-client',
            'revoke-client',
            'export-ovpn',
            'update',
        ]

    def checkenv(self):
        if not os.path.isfile('/usr/sbin/openvpn'):
            print('Error: Unable to find openvpn at /usr/sbin/openvpn.')
            print('Check that it has been installed properly.')
            sys.exit(1)

        if not os.path.isfile('/usr/share/easy-rsa/easyrsa'):
            print('Error: Unable to find easyrsa at /usr/share/easy-rsa/easyrsa')
            print('Check that it has been installed properly.')
            sys.exit(1)

    def parse_args(self):
        parser = argparse.ArgumentParser(prog='ovpn')
        parser.add_argument('command', choices=self.commands)
        self.args = parser.parse_args()

    def cmd_init(self):
        print('Performing initial server initialization...')

    def cmd_status(self):
        print('Checking for status...')

    def cmd_server_config(self):
        print('Editing server config file...')

    def cmd_client_config(self):
        print('Editing client config file...')

    def cmd_clients(self):
        print('Listing clients...')

    def cmd_add_client(self):
        print('Adding new client...')

    def cmd_revoke_client(self):
        print('Revoking existing client...')

    def cmd_export_ovpn(self):
        print('Exporting client .ovpn...', file=sys.stderr)

    def cmd_update(self):
        print('Updating easy-openvpn')

    def run(self):
        self.checkenv()
        self.parse_args()
        getattr(self, f'cmd_{self.args.command}'.lower().replace('-', '_'))()

def main():
    ovpn = OVPN()
    ovpn.run()

if __name__ == '__main__':
    main()
