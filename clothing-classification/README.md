# 스마트 옷장을 위한 의류 분류 AI

# How To Use

## 0. 모델 다운로드  링크

- 옷 종류 구분 모델: https://drive.google.com/file/d/1EOr14ZlGGUKT57H9uPTWhfyMN3CIltYC/view?usp=drive_link
- 옷 패턴 구분 모델:https://drive.google.com/file/d/1kTwZTYoF8EqLWZekN3SJSopCbJLG3sqp/view?usp=drive_link

모델 다운로드 후, clothing-classification/work_dirs/mask-rcnn_r50_fpn_1x_clothes/ 또는 clothing-classification/work_dirs/mask-rcnn_r50_fpn_1x_pattern/ 폴더 내부에 저장해 주세요.

## 1. 환경 세팅

1) conda 가상 환경 설치 (python version 3.9)

2) requirements 설치
   `pip3 install -r requirements.txt`

## 2. test

1) test image 저장

- `root(clothing-classification)/data/test/imgaes` 폴더 내부에 테스트 이미지 저장
- 여러 사진이 있어도 가장 최근에 저장한 사진만 test 하도록 구현 되어 있음

2) `python tools/jetson_nano_test.py` 실행

- 사진에 대한 옷 종류와 옷 패턴에 대한 분류가 실행 되고, 실행이 완료되면 콘솔창에 출력되며 `results/` 폴더 내부에도 결과물이 저장 됩니다.

- results/vis/ 폴더 내부에서 시각화 결과를 확인 할 수 있습니다.





### 설명

`jetson_nano_test.py`는 아래 과정을 python 코드로 변환한 파일 입니다.

1) coco dataset 형식 어노테이션 준비

`python tools/dataset_converters/images2coco.py ../data/test/images classes.txt test.json`

- `../data/test/images`: test image files path

- `classes.txt`: the text file with a list of categories.

- `test.json`: output annotation json file name

`data/test/annotations/test.json`으로 저장됨

    [참고](https://mmdetection.readthedocs.io/en/latest/user_guides/test.html#test-without-ground-truth-annotations)

2) test 실행

`python tools/test.py configs/clothes/mask-rcnn_r50_fpn_1x_clothes.py work_dirs/mask-rcnn_r50_fpn_1x_clothes/epoch_1.pth --out results/results.pkl --work-dir results/word_dirs --show-dir vis/`
