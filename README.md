# relays
Usage: relays.py [OPTIONS]

  Simple command-line client for the Tor Onionoo API that fetches lists of relays.

Options:

  -f, --fast       These are suitable for high-bandwidth circuits.  
  -e, --exitnodes  These are more useful for building general-purpose exit circuits than for relay circuits.  
  -g, --guard      These are suitable for use as an entry gaurd.  
  -h, --hsdir      These are considered a v2 hidden service directory.  
  -r, --running    These are currently usable.  
  -s, --stable     These are suitable for long-lived circuits.  
  -v2, --v2dir     These implement the v2 directory protocol or higher.  
  -v, --valid      These have been 'validated'.  
  --help           Show this message and exit.  
