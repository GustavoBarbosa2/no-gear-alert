from ultralytics import YOLO
import cv2

def main():
    # Caminho para o modelo treinado (usa o best.pt)
    model_path = "runs/detect/train/weights/best.pt"
    model = YOLO(model_path)

    # Tenta abrir a webcam (0 é a webcam principal)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("❌ Não foi possível abrir a webcam. Tenta usar outro número como 1 ou 2.")
        return

    print("✅ Webcam ligada. Pressiona 'q' para sair.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Erro ao ler frame da webcam.")
            break

        # Faz a predição com o modelo
        results = model(frame)

        # Desenha as deteções na imagem
        annotated_frame = results[0].plot()

        # Mostra imagem com deteções
        cv2.imshow("Detecção de EPIs", annotated_frame)

        # Sai se premir 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
