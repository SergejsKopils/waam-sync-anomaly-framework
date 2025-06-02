import os

# Root folder (can be changed)
project_root = "project_root"

# Directory structure
structure = {
    "data": {
        "initial": ["CAM_WALLFORDATA2_1.csv"],
        "process": ["Log_Arc_at_15-Apr-2025_17-35.csv"],
        "sensor": {
            "points": ["2025-04-15_17-43-22_points_694020.csv"],
            "robot_coordinate": [f"LaserCoordinate{i}.csv" for i in range(1, 8)]
        }
    },
    "1MethodGroundTruth": {
        "output": [],
        "_files": ["run_ground_truth.py", "visualize_ground_truth.py"]
    },
    "2MethodClusterKMeansKnown": {
        "output": [],
        "_files": ["run_kmeans_known.py", "visualize_kmeans_known.py"]
    },
    "3MethodClusterKMeansAuto": {
        "output": [],
        "_files": ["run_kmeans_auto.py", "visualize_kmeans_auto.py"]
    },
    "4MethodClusterDBSCAN": {
        "output": [],
        "_files": ["run_dbscan.py", "visualize_dbscan.py"]
    },
    "common": {
        "_files": ["io_utils.py", "plot_utils.py", "config.py"]
    },
    "_files": ["main_compare.py"]
}

def create_structure(base, struct):
    for name, content in struct.items():
        if name == "_files":
            for file_name in content:
                file_path = os.path.join(base, file_name)
                open(file_path, "w").close()
        else:
            dir_path = os.path.join(base, name)
            os.makedirs(dir_path, exist_ok=True)
            if isinstance(content, dict):
                create_structure(dir_path, content)
            elif isinstance(content, list):
                for file_name in content:
                    file_path = os.path.join(dir_path, file_name)
                    open(file_path, "w").close()

# Create the structure
create_structure(project_root, structure)

print(f"✅ Structure created in folder: {project_root}")
