import cv2

# Carregar o modelo de detecção de face do OpenCV
face_cascade = cv2.CascadeClassifier('path/to/haarcascade_frontalface_default.xml')

# Iniciar a captura de vídeo
video_capture = cv2.VideoCapture(0)  # Use 0 para a câmera padrão ou o caminho para um arquivo de vídeo

while True:
    ret, frame = video_capture.read()
    
    # Converter o frame para escala de cinza
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar faces no frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Desenhar retângulos ao redor das faces detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Exibir o frame resultante
    cv2.imshow('Video', frame)

    # Encerrar o loop quando a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar os recursos
video_capture.release()
cv2.destroyAllWindows()
