message = open('313-message.txt','w')
message.write('Testing file for player configuration')
message.write('Testing file for player score')
message.close()

message_test = open('313-message.txt','r')
msg = message_test.read()
print(msg)
message_test.close()