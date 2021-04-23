from pyfingerprint import PyFingerprint
from pyfingerprint import FINGERPRINT_CHARBUFFER1
from pyfingerprint import FINGERPRINT_CHARBUFFER2
from machine import UART
import time




try:
    print("start")
    print("SERIAL SET UP")
    sensorSerial = UART(0, 57600, bits=8, parity=None, stop=1)
    print("FP SET UP")
    f = PyFingerprint(sensorSerial, 0xFFFFFFFF, 0x00000000)
    print("setting baud")
    f.setSystemParameter(4, 57600)
    print("FP PASSWORD VERIFICATION")
    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')
    else:
        print("FP PASSWORD VERIFIED")
except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))

## Gets some sensor information
print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))
f.loadTemplate(0, charBufferNumber=FINGERPRINT_CHARBUFFER1)
print(FINGERPRINT_CHARBUFFER1)

## Tries to search the finger and calculate hash
try:
    print('Waiting for finger...')

    ## Wait that finger is read
    while ( f.readImage() == False ):
        pass

    ## Converts read image to characteristics and stores it in charbuffer 1
    f.convertImage(FINGERPRINT_CHARBUFFER1)

    ## Searchs template
    result = f.searchTemplate()

    positionNumber = result[0]
    accuracyScore = result[1]

    if ( positionNumber == -1 ):
        print('No match found!')

    else:
        print('Found template at position #' + str(positionNumber))
        print('The accuracy score is: ' + str(accuracyScore))

except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))

print("end")

