# TAADT
AcneHDUP
 Test ADT Model
   python test_adt.py --dataset_mode adt
 Test AADT Model
   python test_aadt.py --dataset_mode adt
 Test TAADT Model
   python test_taadt.py --dataset_mode taadt
 Train ADT Model
   python train.py --model aadt --lambda_mmd 0 --dataset_mode adt
 Train AADT Modle
   python train.py --model aadt --lambda_mmd 1 --dataset_mode adt
 Train TAADT Modle
   python train_taadt.py --model taadt --dataset_mode taadt
