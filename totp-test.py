import pyotp
import pyqrcode

print ('Ejemplo validacion TOTP Python\n\n')
print ('Generando QR Code ...')
random_n = pyotp.random_base32()
totp = pyotp.TOTP(random_n)
qr = totp.provisioning_uri("gpinero@gmail.com", issuer_name="MasterCiberseguridad")
url = pyqrcode.create(qr)
big_code = pyqrcode.create(qr, error='L', version=27, mode='binary')
big_code.png('codigo_qr.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
print ('Escanea la imagen png generado y valida un codigo----- \n')

loop=True
while loop:
	print ('El codigo TOTP en este instante es: '+ totp.now())
	totp_input = input("Introduce el codigo generado por la aplicacion: (0 - salir)")
	if totp.verify(str(totp_input)):
		print ('El codigo ES VALIDO en este instante '+str(totp_input))
	else:
		print ('El codigo NO ES VALIDO '+str(totp_input))
	if totp_input==0:
		print "Adios ..."
		loop=False
	