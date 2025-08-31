#!/usr/bin/env python3
import click
import requests
import json

@click.command()
@click.option('-f', '--fast', is_flag=True, help='These are suitable for high-bandwidth circuits.')
@click.option('-e', '--exitnodes', is_flag=True, help='These are more useful for building general-purpose exit circuits than for relay circuits.')
@click.option('-g', '--guard', is_flag=True, help='These are suitable for use as an entry gaurd.')
@click.option('-h', '--hsdir', is_flag=True, help='These are considered a v2 hidden service directory.')
@click.option('-r', '--running', is_flag=True, help='These are currently usable.')
@click.option('-s', '--stable', is_flag=True, help='These are suitable for long-lived circuits.')
@click.option('-v2', '--v2dir', is_flag=True, help='These implement the v2 directory protocol or higher.')
@click.option('-v', '--valid', is_flag=True, help='These have been \'validated\'.')
def cli(fast, exitnodes, guard, hsdir, running, stable, v2dir, valid):
    """Command-line client for the Tor Onionoo API that fetches lists of relays. """

    if not any([fast, exitnodes, guard, hsdir, running, stable, v2dir, valid]):
        raise click.ClickException('Use --help if you need help but please use some flag.')
    if sum(arg is not False for arg in (fast, exitnodes, guard, hsdir, running, stable, v2dir, valid)) > 1:
        raise click.ClickException('Please use just one flag at a time.')

    params='?search=flag:'
    if fast: params+='Fast'
    if exitnodes: params+='Exit'
    if guard: params+='Guard'
    if hsdir: params+='HSDir'
    if running: params+='Running'
    if stable: params+='Stable'
    if v2dir: params+='V2Dir'
    if valid: params+='Valid'

    #not using params= because the api doesn't like when we percent-encode the colon
    r = requests.get('https://onionoo.torproject.org/summary%s'%params) 
    try: 
        results = json.loads(r.text)
        for relay in results['relays']:
            if relay.get('a'): click.echo(relay['a'][0])
            #[0] will grab only the ipv4 address 
    except:
        print(r.status_code)
        print(r.headers)
        print(r.text)
if __name__ == '__main__':
    cli()
