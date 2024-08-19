# 📊 데이터 폴더 구조
```text
data/
├─ clothes/ # 옷 카테고리 분류
├────────── images/ # 데이터
├────────── train.json # 학습용 어노테이션
├────────── test.json # 테스트용 어노테이션
├─ patterns/ # 옷 패턴 분류
├────────── images/ # 데이터
├────────── train.json # 학습용 어노테이션
├────────── test.json # 테스트용 어노테이션
```

- [Merge_COCO_FILES](https://github.com/mohamadmansourX/Merge_COCO_FILES)를 활용하여 COCO Datasets의 어노테이션 형태를 따르고 하나의 어노테이션 파일을 가지도록 변경 함.

  - 우리의 프로젝트에 맞게 코드를 조금 변경 함. `data/merge_annotation.py`

- [cocosplit](https://github.com/akarazniewicz/cocosplit)를 활용하여 하나의 파일로 있던 어노테이션을 train 8 : test 2 비율로 분리하여 train.json, test.json으로 분리 함.

  - 우리의 프로젝트에 맞게 코드를 조금 변경 함.
      `tools/cocosplit/`

# 🦾 train
`python tools/train.py configs/clothes/mask-rcnn_r50_fpn_1x_clothes.py`

또는 

`python tools/train.py configs/clothes/mask-rcnn_r50_fpn_1x_patterns.py`

# 💛 테스트 결과
![test_image1](https://github.com/user-attachments/assets/6556391d-7311-47e9-9aa4-f5c41c70d3e2)
![test_image2](https://github.com/user-attachments/assets/ca5d9888-cd8e-40a9-9a00-c17811bbf6a0)
![test_image4](https://github.com/user-attachments/assets/128ed4ae-972d-4254-99d6-2cd3400d2c79)
![test_image5](https://github.com/user-attachments/assets/5dd8dcf0-6713-4dce-a2aa-05c13e3f86c7)
![test_image7](https://github.com/user-attachments/assets/849933af-9535-44b9-9c1c-967dc470bb9f)
![test_image8](https://github.com/user-attachments/assets/c27a50c6-eb41-4491-8014-ecda14452f3a)


# 🔢 학습 데이터

## 실제 학습에 사용한 데이터
![traindata](https://github.com/user-attachments/assets/5b50511b-601c-4dcf-9791-a7d9419e632a)

## 구축된 데이터

### 👚 의류 통합 데이터 (옷 카테고리 분류)
| 카테고리 | 구축 수량 | Train (80%) | Validation (20%) |
| --- | --- | --- | --- |
| blouse | 29,719 | 23,775 | 5,944 |
| cardigan | 27,285 | 21,828 | 5,457 |
| coat | 30,538 | 24,430 | 6,108 |
| jacket | 31,084 | 24,867 | 6,217 |
| jumper | 34,675 | 27,740 | 6,935 |
| shirt | 38,669 | 30,935 | 7,734 |
| sweater | 34,878 | 27,902 | 6,976 |
| t-shirt | 118,139 | 94,511 | 23,628 |
| vest | 23,134 | 18,507 | 4,627 |
| bottom | 123,500 | 98,800 | 24,700 |
| dress | 57,428 | 45,942 | 11,486 |
| jumpsuite | 1,585 | 1,268 | 317 |
| 총 수량 | 550,634 | 440,507 | 110,127 |


### 👚 의류 디자인 패턴 데이터 (옷 패턴 분류)
| 카테고리 | 구축 수량 | Train (80%) | Validation (20%) |
| --- | --- | --- | --- |
| animal | 20,500 | 16,400 | 4,100 |
| artifact | 18,807 | 15,046 | 3,761 |
| check | 39,109 | 31,287 | 7,822 |
| dot | 15,184 | 12,147 | 3,037 |
| etc | 87,379 | 69,903 | 17,476 |
| etcnature | 17,004 | 13,603 | 3,401 |
| geometric | 34,624 | 27,699 | 6,925 |
| plants | 97,600 | 78,080 | 19,520 |
| stripe | 67,444 | 53,955 | 13,489 |
| symbol | 17,382 | 13,906 | 3,476 |
| 총 수량 | 415,033 | 344,027 | 71,006 |



# 📚 출처

## 학습 데이터: AIhub
- [의류 통합 데이터(착용 이미지, 치수 및 원단 정보)](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71501)
- [의류 디자인 패턴 데이터](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71445)

## MaskRCNN 모델
1. 논문 [링크](https://arxiv.org/abs/1703.06870)
2. mmdetection 오픈 소스 활용
   - [github](https://github.com/open-mmlab/mmdetection)
   - [공식 문서](https://mmdetection.readthedocs.io/en/latest/overview.html)


## Special Thanks😌
K-Fashion-MMDetection
  - [github](https://github.com/ossw-team4/K-Fashion-MMDetection)
  - 잘 정리된 한국어 자료와 질문에 대한 빠르고 친절한 답변 감사드립니다.
    
