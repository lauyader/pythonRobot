#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import RPi.GPIO as GPIO    #Importamos la librería GPIO
import time                #Importamos time (time.sleep)
GPIO.setmode(GPIO.BCM)     #Ponemos la placa en modo BCM
GPIO_TRIGGER = 9          #Usamos el pin GPIO 25 como TRIGGER
GPIO_ECHO    = 10           #Usamos el pin GPIO 7 como ECHO
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  #Configuramos Trigger como salida
GPIO.setup(GPIO_ECHO,GPIO.IN)      #Configuramos Echo como entrada
GPIO.output(GPIO_TRIGGER,False)    #Ponemos el pin 25 como LOW

#########################
# Variables de los led de las luces
###########################
led =15
GPIO.setup(led, GPIO.OUT)

lista=[0]
n=0
try:
    while True:     #Iniciamos un loop infinito
        GPIO.output(GPIO_TRIGGER,True)   #Enviamos un pulso de ultrasonidos
        time.sleep(0.00001)              #Una pequeñña pausa
        GPIO.output(GPIO_TRIGGER,False)  #Apagamos el pulso
        start = time.time()              #Guarda el tiempo actual mediante time.time()
        while GPIO.input(GPIO_ECHO)==0:  #Mientras el sensor no reciba señal...
            start = time.time()          #Mantenemos el tiempo actual mediante time.time()
        while GPIO.input(GPIO_ECHO)==1:  #Si el sensor recibe señal...
            stop = time.time()           #Guarda el tiempo actual mediante time.time() en otra variable
        elapsed = stop-start             #Obtenemos el tiempo transcurrido entre envío y recepción
        distance = (elapsed * 34300)/2   #Distancia es igual a tiempo por velocidad partido por 2   D = (T x V)/2
        print round(distance,2)                   #Devolvemos la distancia (en centímetros) por pantalla
#        with open('data.csv', 'w') as csvfile:
#            spamwriter = csv.writer(csvfile, delimiter=' ',
#                                     quoting=csv.QUOTE_MINIMAL)
            #spamwriter.writerow(['Spam'] * 4 + ['Baked Beans'])
            #spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
#            spamwriter.writerow([lista] )
#            lista.append(distance)
#            print lista
        if distance<40:
            print "Obstaculo en en la vía"
            #Y le damos un valor logico alto para encender el LED
	
            GPIO.output(led, GPIO.HIGH)
	else:
            print "luces apagadas" 
	    GPIO.output(led, GPIO.LOW)

        time.sleep(1)                    #Pequeña pausa para no saturar el procesador de la Raspberry
except KeyboardInterrupt:                #Si el usuario pulsa CONTROL+C...
    print "quit"                         #Avisamos del cierre al usuario
    GPIO.cleanup()                       #Limpiamos los pines GPIO y salimos






