# TAADT: Tone-sensitive Acne Grading via Aligned Augmented Domain Transfer
## AcneHDU、AcneHDUP、AcnePGP
___
The ACNE04 dataset is used as the source domain and the AcneHdu, AcneHdup and AcnePGP dataset is used as the target domian respectively.
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
>### AcneHdu
>>We collect a facial acne image dataset from the public
websites and [shutterstock.com](http://shutterstock.com/).The AcneHDU dataset can be downloaded from [Baidu](https://pan.baidu.com/s/1APEcaR9dL8msEs-vOkFQpg)(pw:ha75).The AcneHDU annotation can be downloaded from [Baidu](https://pan.baidu.com/s/1-sOirE18_-35zKrJ9-Ji7w)(pw:r507).
>### AcneHdup
>>To ensure privacy, we
crop the whole facial images in “Acnehdu”, and build a subset
named “AcnehduP” only using cropped facial patches.The AcneHDU dataset can be downloaded from [Baidu](https://pan.baidu.com/s/1APEcaR9dL8msEs-vOkFQpg)(pw:ha75).
>### AcnePGP
>>we collect a beauty-oriented facial acne
dataset, namely “AcnePGP”. The facial images are collected
by P&G in their research studies with consent from
the subjects. Similarly, in “AcnePGP”, only facial patches
cropped from the original whole facial images are included.Currently, “AcnePGP” dataset can not be released for copyright issues.
>### ACNE04
>>The ACNE04 dataset can be downloaded from [LDL](https://github.com/xpwu95/ldl).
# Pre-trained model
>>The pre-trained model can be used for testing.The pre-trained model can be downloaded from [Baidu](https://pan.baidu.com/s/1E5yZ8dhDouCYIJ0_SZGhzQ)(pw:w49o).

### The AcneHDUP annotation information of the data is being sorted out and will be uploaded later.
