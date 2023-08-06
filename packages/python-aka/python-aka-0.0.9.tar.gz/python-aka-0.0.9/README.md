## Synopsis

Misc scripts and libraries to run junk against aka

## Using this on your own

Use this module with the following in your script

```
import logging
from akapy import Colorer
from akapy.helpers import CredentialParser, cidr_to_netmask, is_pingable, wait_until_it_pings
from akapy.aka import Api

if os.environ.has_key('AKA_BASE_URL'):
    AKA_BASE = os.environ['AKA_BASE_URL']
else:
    AKA_BASE = "https://aka.oit.duke.edu"

cred_parser = CredentialParser(AKA_BASE)
cred = cred_parser.import_credentials()
AKA = Api(AKA_BASE, cred)
```

# Setup

Make sure you have ~/.akarc set up like this:

```
    [https://aka.oit.duke.edu]
    user = joeuser
    key = 11111111-2222-3333-4444-555555555555

    [https://aka-test.oit.duke.edu]
    user = joeuser
    key = aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee
```

The script will default to using 'https://aka.oit.duke.edu'.  If you would like to change it to test (or any other URL), set your environment variable

```
export AKA_BASE_URL=https://aka-test.oit.duke.edu
```
