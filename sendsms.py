import sys
import pygvoicelib

print "The passed arguments are ", sys.argv[1], sys.argv[2]
username="GMAIL USERNAME"
apppass="APPLICATION SPECIFIC PASSWORD"
auth_token="AUTHENTICATION TOKEN - GET FROM get_auth.py"
rnr_se="RNR_SE - GET FROM get_auth.py"
client = pygvoicelib.GoogleVoice(username,apppass,auth_token,rnr_se)
# send sms
client.sms(sys.argv[1],sys.argv[2])
