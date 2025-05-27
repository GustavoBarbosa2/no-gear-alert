from roboflow import Roboflow

rf = Roboflow(api_key="7sNyYpjEXKvMUCRptLhk")  
project = rf.workspace("gustavos").project("ppe-2-ynh14-saokn")
version = project.version(1)
dataset = version.download("yolov8")  
