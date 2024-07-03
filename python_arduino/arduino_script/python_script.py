import serial;
import time;
import sys; sys.path.append('.pylsl')
from pylsl import StreamInlet, resolve_stream

#Connection to Arduino
serialPort=serial.Serial('COM9',9600,timeout=1) #COMX serial port to Arduino
thresh=0.5
time.sleep(2)
#Resolve an EEG stream
print("Looking for LSL stream")
streams=resolve_stream('type','EEG')
#Create a new inlet to read from stream
inlet=StreamInlet(streams[0])
print("Stream inlet created")


if not streams:
    print("No stream found")

def enviar_comando(comando):
    serialPort.write(comando.encode()) #envia comando al arduino
    time.sleep(0.1) #espera un poco para asegurar que le comando se envie
    while serialPort.in_waiting>0: #Si hay algo en el buffer de entrada
        print(serialPort.readline().decode('utf-8').strip()) #Imprime la respuest del arduino


while True:
    sample, timestamp=inlet.pull_sample()
    hyperplane_distance=sample[0]
    stimulation=sample[1]
    print(hyperplane_distance)

    sum=hyperplane_distance+stimulation

    if sum == 0:
        res = 0
    else:
        res = stimulation/sum - hyperplane_distance/sum  
    
    print(sum)
    print(res)

            
    # Determine hand opening or closing based on 'res'
    if res < 0:
        print("Hand closing detected.")
        enviar_comando('c')
    elif res > 0:
        print("Hand opening detected.")
        enviar_comando('o')
    else:
        print("No hand movement detected.")

    time.sleep(0.1)
