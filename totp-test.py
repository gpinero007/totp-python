import pyotp
import pyqrcode

print ("--- Testing TOTP with python libraries \n\n")
print ('Generating OTPAuth QR Code in file otpauth_qr.png (scan it with your app)')

random_n = pyotp.random_base32()
totp = pyotp.TOTP(random_n)
qr = totp.provisioning_uri("gpinero@testing.com", issuer_name="TEST TOTP Python")
url = pyqrcode.create(qr)
big_code = pyqrcode.create(qr, error='L', version=27, mode='binary')
big_code.png('otpauth_qr.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
print ('-- Test TOTP code -- \n')

loop=True
while loop:
	print ('TOTP code now is: '+ totp.now())
	totp_input = input("Input the app code (0 - to exit):")
	if totp.verify(str(totp_input)):
		print ('\n ## OK your code is valid !!!'+str(totp_input))
	else:
		print ('\n WRONG code, not is '+str(totp_input))
	if totp_input==0:
		print "Bye..."
		loop=False	
