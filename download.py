from roboflow import Roboflow

rf = Roboflow(api_key="7sNyYpjEXKvMUCRptLhk")  # a tua API key
project = rf.workspace("gustavos").project("ppe-2-ynh14-saokn")
version = project.version(1)
dataset = version.download("yolov8")  # Isto vai criar uma pasta como 'PPE-2-1'
