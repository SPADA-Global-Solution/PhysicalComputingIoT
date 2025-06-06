import cv2
import mediapipe as mp

# Inicialização do MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Captura de vídeo (0 = webcam)
cap = cv2.VideoCapture(0)

# Definição da área de risco (ajuste conforme resolução da câmera)
risk_x1, risk_y1 = 400, 300
risk_x2, risk_y2 = 600, 480

# Parâmetro de brilho base
BRIGHTNESS_THRESHOLD = 15  # Ajuste conforme iluminação do ambiente
prev_brightness = 0

# Variável para manter estado do alerta
alerta_ativo = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Espelhar imagem para melhor interação
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    # Desenhar área de risco com linha vermelha
    cv2.rectangle(frame, (risk_x1, risk_y1), (risk_x2, risk_y2), (0, 0, 255), 2)

    # Convertendo para escala de cinza para medir claridade
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    risk_area = gray[risk_y1:risk_y2, risk_x1:risk_x2]
    brightness = risk_area.mean()

    hand_in_risk_area = False

    # Detecção de mãos
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Pega a posição do dedo indicador
            x = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * frame.shape[1])
            y = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * frame.shape[0])

            # Desenha landmarks na mão
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Checa se a mão está dentro da área de risco
            if risk_x1 < x < risk_x2 and risk_y1 < y < risk_y2:
                hand_in_risk_area = True
                cv2.putText(frame, 'Mao na area de risco!', (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Lógica de alerta
    if hand_in_risk_area:
        # Detecta aumento súbito de claridade
        if brightness > BRIGHTNESS_THRESHOLD and abs(brightness - prev_brightness) > 20:
            alerta_ativo = True
            cv2.putText(frame, 'ALERTA: Possivel vela acesa!', (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
            print('ALERTA: Possivel acendimento de vela detectado!')
        elif alerta_ativo:
            # Mantém o alerta ativo enquanto a mão estiver na área
            cv2.putText(frame, 'ALERTA: Vela acesa detectada!', (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        else:
            # Apenas a mão na área, sem aumento de claridade
            cv2.putText(frame, 'CUIDADO: mao proxima da area de risco.', (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
    else:
        # Se a mão sair da área, reseta o alerta
        alerta_ativo = False

    # Atualiza o brilho anterior
    prev_brightness = brightness

    # Exibe a imagem com as marcações
    cv2.imshow('SPADA IoT - Monitoramento', frame)

    # Pressione 'q' para sair
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Libera os recursos
cap.release()
cv2.destroyAllWindows()
