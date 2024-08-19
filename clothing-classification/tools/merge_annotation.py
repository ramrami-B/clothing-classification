import os
import json
from shapely.geometry import Polygon

# JSON 파일이 있는 최상위 디렉토리 경로
input_dirs = ["../../new-pattern-data/json"]

# COCO 형식으로 변환된 어노테이션을 저장할 파일 경로
output_file = "../data/patterns/coco_annotations.json"

# 주어진 annotation_point를 사용하여 area 계산 함수 정의
def calculate_area(annotation_point):
    points = list(zip(annotation_point[0::2], annotation_point[1::2]))
    polygon = Polygon(points)
    return polygon.area

def coco_dataset():
    # COCO 형식의 데이터 구조를 초기화합니다.
    coco_format = {
        "images": [],
        "categories": [],
        "annotations": []
    }
    
    # 어노테이션과 이미지 ID를 위한 초기화
    annotation_id = 0
    image_id = 0
    
    # 카테고리 이름과 ID 매핑을 위한 초기화
    category_id_map = {}
    category_counter = 0
    
    # 카테고리 설정
    # categories = ["blouse", "cardigan", "coat", "jacket", "jumper", "shirt", "sweater", "t-shirt", "vest", "pants", "skirt", "dress", "jumpsuite"]
    categories = ['check', 'dot', 'stripe', 'plants', 'etc']
    
    for idx, category_name in enumerate(categories):
        category_info = {
            "id": idx,
            "name": category_name,
            "supercategory": ""
        }
        coco_format["categories"].append(category_info)
        category_id_map[category_name] = idx
    
    # 주어진 폴더 내의 모든 JSON 파일을 읽어 COCO 형식으로 변환
    count = 1
    for input_dir in input_dirs:
        for root, dirs, files in os.walk(input_dir):
            print(f"count: {count}, 파일 갯수: {len(files)}")

            for filename in files:
                if filename.endswith(".json"):
                    file_path = os.path.join(root, filename)
                    
                    with open(file_path, 'r') as f:
                        data = json.load(f)

                        if "dataset" in data:
                            image_filename = os.path.basename(data["dataset"]["dataset.image_path"])
                        else:
                            image_filename = os.path.basename(data["images"][0]["file_name"])

                        image_path = os.path.join("../data/patterns/images", image_filename)
                        
                        if not os.path.exists(image_path):
                            print(f"이미지 파일이 없습니다: {image_filename}")
                            continue  # 이미지 파일이 없는 경우, 해당 어노테이션을 건너뜀
                        
                        # 이미지 정보 추출 및 COCO 형식으로 변환
                        if "dataset" in data:
                            image_info = {
                                "id": image_id,
                                "width": data["dataset"]["dataset.width"],
                                "height": data["dataset"]["dataset.height"],
                                "file_name": image_filename
                                }
                        else:
                            image_info = {
                                    "id": image_id,
                                    "width": 907,
                                    "height": 1613,
                                    "file_name": image_filename
                                }
                        
                        # 이후 image_info를 사용하여 COCO 형식에 추가
                        if image_info:
                            coco_format["images"].append(image_info)
                        
                        # 파일 이름에서 카테고리 추출
                        detected_category = None
                        for category in categories:
                            if category in image_filename:
                                detected_category = category
                                break
                                
                        if detected_category in category_id_map:
                            category_id = category_id_map.get(detected_category)
                        else:
                            print(detected_category)
                            
                        if "annotations" in data:
                            annotation_info = {
                                "id": annotation_id,
                                "image_id": image_id,
                                "category_id": category_id,
                                "segmentation": [[100, 100, 150, 100, 150, 150, 100, 150]],
                                "area": 2500, 
                                "bbox": [100, 100, 50, 50], 
                                "iscrowd": 0
                            }
                            coco_format["annotations"].append(annotation_info)
                            annotation_id += 1
                        else:
                            for ann in data["annotation"]:
                                area = calculate_area(ann["annotation_point"])
                                annotation_info = {
                                    "id": annotation_id,
                                    "image_id": image_id,
                                    "category_id": category_id,
                                    "segmentation": [ann["annotation_point"]],
                                    "area": area,
                                    "bbox": [
                                        min(ann["annotation_point"][::2]),
                                        min(ann["annotation_point"][1::2]),
                                        max(ann["annotation_point"][::2]) - min(ann["annotation_point"][::2]),
                                        max(ann["annotation_point"][1::2]) - min(ann["annotation_point"][1::2])
                                    ],
                                    "iscrowd": 0
                                }
                                coco_format["annotations"].append(annotation_info)
                                annotation_id += 1
                        
                        image_id += 1
                        
            count = count + 1
            
    return coco_format
                
                        
if __name__ == '__main__':
    coco_format = coco_dataset()
    
    # COCO 형식의 데이터를 json 파일로 저장합니다.
    with open(output_file, 'w') as f:
        json.dump(coco_format, f, indent=4)

    print(f"모든 작업이 완료되었습니다. COCO 형식의 어노테이션이 '{output_file}'에 저장되었습니다.")