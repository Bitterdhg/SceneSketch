import os
import argparse
import subprocess as sp
from shutil import copyfile


# CUDA_VISIBLE_DEVICES=6 python scripts/resnet_vs_vit/baseline.py --mask 1 --fc 0.2

parser = argparse.ArgumentParser()
parser.add_argument("--mask", type=int, default=0)
parser.add_argument("--fc", type=float, default=0.1)
args = parser.parse_args()

# # ===================
# # ====== demo =======
# # ===================
# num_strokes = 64
# num_sketches = 1
# num_iter = 51
# use_wandb = 0
# wandb_project_name = "none"
# images = ["yael.jpg"]
# output_pref = f"background_project/experiements/resnet_vs_vit_demo"
# loss_mask = "none"
# mask_object_attention = 0
# if args.mask:
#         loss_mask = "for"
#         mask_object_attention = 1
# # ===================


# ===================
# ====== real =======
# ===================
num_strokes = 32
num_sketches = 2
num_iter = 2001
use_wandb = 1
wandb_project_name = "rn_vs_vit_18_07"
# images = ["yael.jpg", "forest.jpg", "semi-complex.jpeg", "complex-scene-crop.png", "assaf.jpg"]
images = ["semi-complex.jpeg"]

output_pref = f"background_project/experiements/resnet_vs_vit_07_18"
loss_mask = "none"
mask_object_attention = 0
if args.mask:
    mask_object = 1
    # loss_mask = "for"
    # mask_object_attention = 1
# ===================

path_to_files = "/home/vinker/dev/input_images/background_sketching/"
model = "RN101"
clip_conv_layer_weights = "0,0,1.0,1.0,0"
clip_fc_loss_weight = args.fc


for im_name in images:
        file_ = f"{path_to_files}/{im_name}"
        test_name = f"{model[:3]}_fc{clip_fc_loss_weight}_{num_strokes}s_mask{mask_object}_{os.path.splitext(os.path.basename(file_))[0]}"
        print(test_name)
        sp.run(["python", 
                "scripts/resnet_vs_vit/run_sketch.py", 
                "--target_file", file_,
                "--output_pref", output_pref,
                "--num_strokes", str(num_strokes),
                "--num_iter", str(num_iter),
                "--test_name", test_name,
                "--num_sketches", str(num_sketches),
                "--mask_object", str(mask_object),
                "--fix_scale", "0",
                "--clip_fc_loss_weight", str(clip_fc_loss_weight),
                "--clip_conv_layer_weights", clip_conv_layer_weights,
                "--clip_model_name", model,
                "--use_wandb", str(use_wandb),
                "--wandb_project_name", wandb_project_name,
                "--loss_mask",loss_mask,
                "--mask_object_attention", str(mask_object_attention)])



# parser.add_argument("--loss_mask", type=str, default="none", 
#                         help="mask the object during training, can be none|back|for, if you want to mask out the background choose back")
# parser.add_argument("--mask_object_attention", type=int, default=0)

# loss_mask = for