import sys
import serial
import threading 
from queue import Queue
from collections import deque
import numpy as np 
from PyQt5 import QtWidgets, QtCore       # FIZ THIS 
import pyqtgraph as pg


# shared data queue 
q = Queue()
running = True 

#serial reading thread 
def read_serial(ser, q):
    global running 

    while running:
        line_bytes = ser.readline 

        try:
            value = int(line_bytes.decode('uf-8', errors='ignore').strip())
            q.put(value)
        except:
            continue

#Qt App 
app = QWidgets.QApplication([])

win = pg.GraphicsLayoutWidget(show =True, title = "real time serial plot")

#time domain 
plot_time = win.addPlot(title = "Time Domain")
curve_raw = plot_time.plot(pen=pg.mkPen(200,200,200))

plot_time.setVRange(-10,100)

data = []

ser = serial.Serial('COM5',115200)

thread = threading.Thread(target=read_serial,args=(ser,q))
thread.start

fs = 200 #sampling freq 

def update():
    global data 

    max_per_update = 50
    count = 0 

    while not q.empty() and count < max_per_update:
        value = q.get()
        data.append(value)
        count += 1 
    
    if len(data)<500:
        data = data[-500:]

#timer 
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(20) #update every 20 ms 

#cleanup 
def cleanup():
    global running 
    running = False 
    thread.join()
    ser.close()

app.aboutTQuit.connect(cleanup)

#run 
sys.exit(app, exec_())