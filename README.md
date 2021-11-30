# TAADT
## AcneHDU
___
The ACNE04 dataset is used as the source domain and the AcneHDU dataset is used as the target domian.
+ ### ADT Model

>#### test the model

>>python test_adt.py --dataset_mode adt

>#### train the model

>>python train.py --model aadt --lambda_mmd 0 --dataset_mode adt

+ ### AADT Model

>#### test the model

>>python test_aadt.py --dataset_mode adt

>#### train the model

>>python train.py --model aadt --lambda_mmd 1 --dataset_mode adt

+ ### TAADT Model

>#### test the model

>>python test_taadt.py --dataset_mode taadt

>#### train the model

>>python train_taadt.py --model taadt --dataset_mode taadt


## AcneHDUP
___
The ACNE04 dataset is used as the source domain and the AcneHDUP dataset is used as the target domian.

+ ### ADT Model

>#### test the model

>>python test_adt.py --dataset_mode adt

>#### train the model

>>python train.py --model aadt --lambda_mmd 0 --dataset_mode adt

+ ### AADT Model

>#### test the model

>>python test_aadt.py --dataset_mode adt

>#### train the model

>>python train.py --model aadt --lambda_mmd 1 --dataset_mode adt

+ ### TAADT Model

>#### test the model

>>python test_taadt.py --dataset_mode taadt

>#### train the model

>>python train_taadt.py --model taadt --dataset_mode taadt

## AcnePGP
___
The ACNE04 dataset is used as the source domain and the AcnePGP dataset is used as the target domian.

+ ### ADT Model

>#### test the model

>>python test_adt.py --dataset_mode adt

>#### train the model

>>python train.py --model aadt --lambda_mmd 0 --dataset_mode adt

+ ### AADT Model

>#### test the model

>>python test_aadt.py --dataset_mode adt

>#### train the model

>>python train.py --model aadt --lambda_mmd 1 --dataset_mode adt

+ ### TAADT Model

>#### test the model

>>python test_taadt.py --dataset_mode taadt

>#### train the model

>>python train_taadt.py --model taadt --dataset_mode taadt
