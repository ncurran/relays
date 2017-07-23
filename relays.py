#!/usr/bin/env python
import click
import requests
import json

@click.command()
@click.option('-f', '--fast', is_flag=True, help='These are suitable for high-bandwidth circuits.')
@click.option('-e', '--exit', is_flag=True, help='These are more useful for building general-purpose exit circuits than for relay circuits.')
@click.option('-g', '--guard', is_flag=True, help='These are suitable for use as an entry gaurd.')
@click.option('-h', '--hsdir', is_flag=True, help='These are considered a v2 hidden service directory.')
@click.option('-r', '--running', is_flag=True, help='These are currently usable.')
@click.option('-s', '--stable', is_flag=True, help='These are suitable for long-lived circuits.')
@click.option('-v2', '--v2dir', is_flag=True, help='These implement the v2 directory protocol or higher.')
@click.option('-v', '--valid', is_flag=True, help='These have been \'validated\'.')
def cli(fast, exit, guard, hsdir, running, stable, v2dir, valid):
    """Command-line client for the Tor Onionoo API that fetches lists of relays. Only one flag should be used at a time."""
    params='?search=flag:'
    if fast: params+='Fast'
    if exit: params+='Exit'
    if guard: params+='Guard'
    if hsdir: params+='HSDir'
    if running: params+='Running'
    if stable: params+='Stable'
    if v2dir: params+='V2Dir'
    if valid: params+='Valid'

    #not using params= because the api doesn't like when we percent-encode the colon
    r = requests.get('https://onionoo.torproject.org/summary%s'%params) 
    results = json.loads(r.text)
    for relay in results['relays']:
        if relay.get('a'): print relay['a'][0] 
        #[0] will grab only the 
pv4 addressif __name__ == '__main__':
    cli()
