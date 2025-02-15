import cv2
import pickle
from db import *

#conexion a Data 
fdb = DataBase()


cascPath = "Cascades/haarcascade_frontalface_alt2.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

eyeCascade = cv2.CascadeClassifier("Cascades/haarcascade_eye.xml")
smileCascade = cv2.CascadeClassifier("Cascades/haarcascade_smile.xml")

reconocimiento = cv2.face.LBPHFaceRecognizer_create()
reconocimiento.read("entrenamiento.yml")

etiquetas = {"nombre_persona" : 1 }
with open("labels.pickle",'rb') as f:
    pre_etiquetas = pickle.load(f)
    etiquetas = { v:k for k,v in pre_etiquetas.items()}

web_cam = cv2.VideoCapture(0)

while True:
    # Capture el marco
    ret, marco = web_cam.read()
    grises = cv2.cvtColor(marco, cv2.COLOR_BGR2GRAY)    
    rostros = faceCascade.detectMultiScale(grises, 1.5, 2)

    # Dibujar un rectángulo alrededor de las rostros
    for (x, y, w, h) in rostros:
        #print(x,y,w,h)
        roi_gray = grises[y:y+h, x:x+w]
        roi_color = marco[y:y+h, x:x+w]

        # reconocimiento
        id_, conf = reconocimiento.predict(roi_gray)
        if conf >= 4  and conf < 100:
            #print(id_)
            #datos del estudiante
            #print(fdb.true_user(etiquetas[id_]))
            #db.true_user(etiquetas[id_])
            font = cv2.FONT_HERSHEY_PLAIN            

            nombre = etiquetas[id_]
            data=fdb.true_user(nombre)

            if conf > 60:
                #print(conf)
                nombre = "Desconocido"

            color = (255,255,255)
            grosor = 1
            cv2.putText(marco, data, (x,y), font, 1, color, grosor, cv2.LINE_4)

        img_item = "my-image.png"
        cv2.imwrite(img_item, roi_gray)
        
        cv2.rectangle(marco, (x, y), (x+w, y+h), (255, 255, 255), 1)

        rasgos = smileCascade.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in rasgos:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 255, 255), 1)
    
    # Display resize del marco  
    marco_display = cv2.resize(marco, (1200, 650), interpolation = cv2.INTER_CUBIC)
    cv2.imshow('XDface UVG', marco_display)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cuando todo está hecho, liberamos la captura
web_cam.release()
cv2.destroyAllWindows()
