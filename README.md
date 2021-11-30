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
# Dataset
>### AcneHDU
>>We collect a facial acne image dataset from the public
websites and [shutterstock.com](http://shutterstock.com/).The AcneHDU dataset can be downloaded from [Baidu]().
>### AcneHDUP
>>To ensure privacy, we
crop the whole facial images in “Acnehdu”, and build a subset
named “AcnehduP” only using cropped facial patches.The AcneHDU dataset can be downloaded from [Baidu]().
>### AcnePGP
>>we collect a beauty-oriented facial acne
dataset, namely “AcnePGP”. The facial images are collected
by P&G in their research studies with consent from
the subjects. Similarly, in “AcnePGP”, only facial patches
cropped from the original whole facial images are included.Currently, “AcnePGP” dataset can not be released for copyright issues.
>### ACNE04
>>The ACNE04 dataset can be downloaded from [LDL](https://github.com/xpwu95/ldl).

