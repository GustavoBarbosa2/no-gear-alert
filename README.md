# no-gear-alert

Este projeto utiliza o modelo YOLOv8 para detetar a ausência de equipamento de proteção (gear) em vídeos ou através da webcam. Pode ser utilizado para monitorização em ambientes industriais, estaleiros de obras ou outros locais onde seja essencial o uso de equipamento de segurança.

---

## Estrutura do projeto

- **detector.py**: Script principal para deteção em vídeos.  
- **webcam_detector.py**: Deteção em direto através da webcam.  
- **treinar_modelo.py**: Script para treinar ou ajustar o modelo YOLO.  
- **download.py**: Descarrega os recursos necessários para a execução.  
- **registo_alertas.xlsx**: Ficheiro Excel onde são registados os alertas detetados.  
- **yolov8n.pt**: Pesos do modelo YOLOv8 pré-treinado.  
- **video.mp4**, **video2.mp4**: Exemplos de vídeos de teste.  

---

## Requisitos

O projeto utiliza Python e as seguintes bibliotecas:

```bash
pip install ultralytics opencv-python pandas
```

## Como utilizar

### Deteção em video
```bash
python detector.py
```

### Deteção em direto (webcam)
```bash
python webcam_detector.py
```

## Treinar o modelo
```bash
python treinar_modelo.py
```

## Registo de alertas
Os alertas gerados (por exemplo, quando alguém não está a usar equipamento de proteção) são registados no ficheiro registo_alertas.xlsx. Podes abrir este ficheiro em qualquer editor de folhas de cálculo para consultar os registos.


## Observações

O modelo YOLOv8 pré-treinado (yolov8n.pt) incluído no projeto pode ser substituído por outro ficheiro de pesos, caso queiras experimentar outro modelo YOLO.

As deteções utilizam a biblioteca ultralytics, que simplifica a utilização do YOLOv8 e integra funcionalidades como treino, deteção e exportação.

Os vídeos de exemplo incluídos (video.mp4 e video2.mp4) podem ser usados para testar imediatamente o funcionamento do sistema.

Os scripts detector.py e webcam_detector.py usam o modelo YOLOv8 para detetar a presença ou ausência de equipamento de proteção e, se necessário, registam automaticamente os alertas no ficheiro registo_alertas.xlsx.

Para personalizar o modelo ou as classes detetadas, podes ajustar o script treinar_modelo.py e treinar o modelo YOLOv8 com o teu próprio conjunto de dados, que deve estar devidamente anotado.

Certifica-te que tens uma webcam funcional para utilizares o webcam_detector.py.

