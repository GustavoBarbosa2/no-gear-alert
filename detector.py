from ultralytics import YOLO
import cv2

def main():
    model = YOLO('runs/detect/train/weights/best.pt')  # Substitui com o nome do modelo se for diferente

    video_path = 'video.mp4'
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Erro ao abrir o vídeo: {video_path}")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        annotated_frame = results[0].plot()

        cv2.imshow('Detecção de EPI (vídeo)', annotated_frame)

        # Pressiona 'q' para sair antes do fim do vídeo
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
