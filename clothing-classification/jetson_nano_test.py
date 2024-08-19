import pickle
import subprocess

# 1. COCO 포맷으로 변환
def convert_images_to_coco(images_path, classes_file, output_json):
    print("================================== 테스트 데이터 어노테이션 생성 중... ===================================")
    command = [
        'python', 'tools/dataset_converters/images2coco.py',
        images_path, classes_file, output_json
    ]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.decode()}")

# 2. 모델 테스트 실행
def run_model_test(config_file, checkpoint_file, output_pkl, work_dir):
    command = [
        'python', 'tools/test.py',
        config_file, checkpoint_file,
        '--out', output_pkl,
        '--work-dir', work_dir,
        '--show-dir', 'vis/',
    ]
    try:
        subprocess.run(command, check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        print("======================================== 테스트 완료!! ==============================================")
        print("=============================== 결과 출력 중 잠시만 기다려 주세요... ==================================")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr.decode()}")

# 3. 예측 결과 출력
def print_prediction(labels, scores, translations):
    if labels.numel() == 0:
        print("==================================== 예측된 값이 없습니다. ===========================================")
    else:
        labels = labels.tolist()
        scores = scores.tolist()
        print( "가장 정확한 예측: ", translations[labels[0]][1], "(", round(scores[0], 3) * 100, "%)")
        if len(labels) > 1 and len(scores) > 1:
            print("다음으로 가장 정확한 예측: ", translations[labels[1]][1], "(", round(scores[1], 3) * 100, "%)")

if __name__ == "__main__":
    # 1단계: COCO 포맷으로 변환 (옷 종류)
    images_path = 'data/test/images'  
    classes_file = 'clothes_classes.txt'
    output_json = 'test.json'
    
    convert_images_to_coco(images_path, classes_file, output_json)
    
    # 2단계: 옷 종류 모델 테스트 실행
    clothes_config_file = 'configs/clothes/mask-rcnn_r50_fpn_1x_clothes.py'
    clothes_checkpoint_file = 'work_dirs/mask-rcnn_r50_fpn_1x_clothes/epoch_9.pth'
    clothes_output_pkl = 'results/clothes/results.pkl'
    clothes_work_dir = 'results/clothes/work_dirs'

    print("============================== 옷 종류 구분을 시작합니다. ===================================================")
    run_model_test(clothes_config_file, clothes_checkpoint_file, clothes_output_pkl, clothes_work_dir)
    
    # 옷 종류 결과 로드 및 예측
    with open(clothes_output_pkl, "rb") as fr:
        data = pickle.load(fr)

    labels = data[0]['pred_instances']['labels']
    scores = data[0]['pred_instances']['scores']
    clothes_translations = [
        ["blouse", "블라우스"], ["cardigan", "가디건"], ["coat", "코트"],
        ["jacket", "재킷"], ["jumper", "점퍼"], ["shirt", "셔츠"],
        ["sweater", "스웨터"], ["t-shirt", "티셔츠"], ["vest", "조끼"],
        ["pants", "바지"], ["skirt", "치마"], ["dress", "드레스"],
        ["jumpsuite", "점프수트"]
    ]

    print_prediction(labels, scores, clothes_translations)

    # 3단계: COCO 포맷으로 변환 (패턴)
    classes_file = 'pattern_classes.txt'
    convert_images_to_coco(images_path, classes_file, output_json)

    # 4단계: 패턴 모델 테스트 실행
    pattern_config_file = 'configs/pattern/mask-rcnn_r50_fpn_1x_pattern.py'
    pattern_checkpoint_file = 'work_dirs/mask-rcnn_r50_fpn_1x_pattern/epoch_10.pth'
    pattern_output_pkl = 'results/pattern/results.pkl'
    pattern_work_dir = 'results/pattern/work_dirs'
    
    print("=============================== 옷 패턴 구분을 시작합니다. =================================================")
    run_model_test(pattern_config_file, pattern_checkpoint_file, pattern_output_pkl, pattern_work_dir)
    
    # 패턴 결과 로드 및 예측
    with open(pattern_output_pkl, "rb") as fr:
        pattern_data = pickle.load(fr)

    labels = pattern_data[0]['pred_instances']['labels']
    scores = data[0]['pred_instances']['scores']
    # 'check', 'dot', 'stripe', 'plants'
    pattern_translations = [
        ["check", "체크"], ["dot", "도트"], 
        ["stripe", "스트라이프"], ["plants", "꽃무늬"], ["etc", "기타"]
    ]

    print_prediction(labels, scores, pattern_translations)