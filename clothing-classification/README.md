# 스마트 옷장을 위한 의류 분류 AI

# How To Test

### 1. 환경 세팅

- conda 가상 환경 설치

    python version 3.9

- requirements 설치
`pip3 install -r requirements.txt`

### 2. test

- test image 저장

  `root(clothing-classification)/data/test/imgaes` 폴더 생성 후 `images/` 폴더 내부에 이미지 저장하기

- script 실행 

  `python tools/jetson_nano_test.py`

실행 과정과 test에 걸린 시간이 콘솔에 출력됩니다. 실행이 완료되면 `results/` 폴더 내부에 결과물이 저장 됩니다.
  

### 설명

`jetson_nano_test.py`는 아래 과정을 python 코드로 변환한 파일 입니다.

1. coco dataset 형식 어노테이션 준비

  `python tools/dataset_converters/images2coco.py ../data/test/images classes.txt test.json`

  - `../data/test/images`: test image files path

  - `classes.txt`: the text file with a list of categories.

  - `test.json`: output annotation json file name

=>   `data/test/annotations/test.json`으로 저장됨

[참고](https://mmdetection.readthedocs.io/en/latest/user_guides/test.html#test-without-ground-truth-annotations)

2. test 실행

`python tools/test.py configs/clothes/mask-rcnn_r50_fpn_1x_clothes.py work_dirs/mask-rcnn_r50_fpn_1x_clothes/epoch_1.pth --out results/results.pkl --work-dir results/word_dirs --show-dir results/result_images`

=> `results/` 폴더 내부에  결과물 저장 됨!
