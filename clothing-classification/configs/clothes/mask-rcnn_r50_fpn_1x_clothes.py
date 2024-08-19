_base_ = [
    '../_base_/models/mask-rcnn_r50_fpn.py',
    '../_base_/datasets/coco_instance.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]

# We also need to change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=13),
        mask_head=dict(num_classes=13)))

# Checkpoint 설정
# checkpoint_config = dict(
#     interval=1, 
#     filename_tmpl='mini_dataset_epoch_{}.pth'
# )

# data_root = 'data/clothes/'
data_root = 'data/mini-clothes/'

metainfo = {
    'classes': ("blouse", "cardigan", "coat", "jacket", "jumper", "shirt", "sweater", "t-shirt", "vest", "pants", "skirt", "dress", "jumpsuite",)
}

train_dataloader = dict(
    batch_size=1,
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='train.json',
        data_prefix=dict(img='images/')))

val_dataloader = dict(
    dataset=dict(
        data_root=data_root,
        metainfo=metainfo,
        ann_file='test.json',
        data_prefix=dict(img='images/')))

# test_dataloader=dict(
#     batch_size=1,
#     dataset=dict(
#         data_root=data_root,
#         metainfo=metainfo,
#         ann_file='test.json',
#         data_prefix=dict(img='images/') 
#     )
# )

test_dataloader=dict(
    batch_size=1,
    dataset=dict(
        data_root='',
        metainfo=metainfo,
        ann_file='data/test/annotations/test.json',
        data_prefix=dict(img='data/test/images/') 
    )
)

# Modify metric related settings
val_evaluator = dict(ann_file=data_root + 'test.json')
test_evaluator = dict(ann_file='data/test/annotations/test.json') 
# test_evaluator = dict(ann_file=data_root + 'test.json') 

# We can use the pre-trained Mask RCNN model to obtain higher performance
load_from = 'https://download.openmmlab.com/mmdetection/v2.0/mask_rcnn/mask_rcnn_r50_fpn_mstrain-poly_3x_coco/mask_rcnn_r50_fpn_mstrain-poly_3x_coco_20210524_201154-21b550bb.pth'