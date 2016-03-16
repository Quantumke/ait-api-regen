# import the helper gateway class
#from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from AfricasTalkingGateway import *
# Specify your login credentials
username = "BENTHEDEV"
apikey   = "d508538a1af8a040188ea9e97ad502c9c108a23d741b2e95806da0f936247f34"

# Specify the numbers that you want to send to in a comma-separated list
# Please ensure you include the country code (+254 for Kenya)
to      = ""

# And of course we want our recipients to know what we really do
message = "MPESA CONFIRMED  YOU HAVE RECIEVED KSH.600 FROM  KENNETH KAUNDA"

# Create a new instance of our awesome gateway class
gateway = AfricasTalkingGateway(username, apikey)

# Any gateway errors will be captured by our custom Exception class below, 
# so wrap the call in a try-catch block
try:
    # Thats it, hit send and we'll take care of the rest.
    
    results = gateway.sendMessage(to, message)
    
    for recipient in results:
        # status is either "Success" or "error message"
        print ('number=%s;status=%s;messageId=%s;cost=%s' )
except AfricasTalkingGatewayException:
    print ('Encountered an error while sending')
