email = 'something@gmail.com'
passwd = 'password'

new_keys = ('albumMatchedId', 'pending')

##

from gmusicapi.api import Api
from collections import Counter

api = Api()
api.login(email, passwd)

lib = api.get_all_songs()
print "%s total songs" % len(lib)

for new_key in new_keys:
    matching = [s for s in lib if new_key in s]
    print
    print new_key
    print "  %s matches" % len(matching)
    if len(matching) > 0:
        for key, occurs in Counter(s[new_key] for s in matching).items():
            print "   %s: %r" % (occurs, key)
