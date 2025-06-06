# SPADA IoT — Sistema de Prevenção de Acidentes Domésticos durante Apagões

---

## 📌 Descrição do Problema

Durante apagões, é comum que moradores utilizem velas para iluminação temporária.  
Entretanto, isso gera um **risco elevado de incêndios domésticos**, principalmente quando as velas são posicionadas próximas a cortinas, papéis ou móveis inflamáveis.

Diante desse cenário, propomos uma solução de **visão computacional** que detecta comportamentos de risco em tempo real.

---

## 🎯 Visão Geral da Solução

O **SPADA IoT** é um sistema implementado em **Python**, utilizando as bibliotecas **MediaPipe** e **OpenCV**, capaz de detectar:

✅ A presença da mão em uma **área de risco** previamente definida.  
✅ O **acendimento de uma vela** ou aumento súbito de claridade nessa área.  
✅ Manutenção do alerta enquanto o risco permanece.  
✅ Cancelamento do alerta automaticamente quando a vela é apagada ou a mão sai da área.

A solução **não requer hardware adicional** — funciona apenas com uma câmera padrão.

---

## ✅ Requisitos

- Python 3.7 ou superior
- OpenCV
- MediaPipe
- Anaconda Navigator

---

## 🚀 Instruções de Uso

### ✅ Instalação das dependências

Executar o **CMD.exe Prompt** do Anaconda Navigator, e realizar o seguinte comando para a instalação das dependências necessarias:

```bash
pip install opencv-python mediapipe
```

### ✅ Execultando o codigo: 

Após a instalção das dependencias, execute o **VS Code** do Anaconda Navigator e procure o projeto clonado. 

---

##  🎥 Link do vídeo demonstrativo



---

## 🚀 Considerações Finais

O SPADA IoT demonstra como tecnologias simples de visão computacional podem contribuir com a segurança doméstica durante apagões.
Seu uso é viável tanto em residências quanto em ambientes como hospitais e centros de cuidado, ajudando a prevenir acidentes evitáveis.

O código foi desenvolvido para ser leve, reutilizável e fácil de ser adaptado para outros cenários.

---

## 👨‍💻 Integrantes

João Pedro de Souza Vieira - RM 99805

Gabriel Riqueto Reis - RM 98685

Leonardo Nicastro Mansur Castillo - RM 551659

---

## 📚 Referências Técnicas

- [MediaPipe Hands](https://mediapipe-readthedocs-io.translate.goog/en/latest/solutions/hands.html?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc)
- [OpenCV Documentation](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html)
