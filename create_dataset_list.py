import os
clean_trainPath =r"C:\Users\ssrikrishnan6\Audio-Denoising\clean_trainset_28spk_wav"
noisy_trainPath =r"C:\Users\ssrikrishnan6\Audio-Denoising\noisy_trainset_28spk_wav"
train_files = os.listdir(clean_trainPath)

print(clean_trainPath)

with open(r'C:\Users\ssrikrishnan6\Audio-Denoising\train_dataset.txt', 'w+') as f:
    for file in train_files:
        f.write(noisy_trainPath+"\\"+file+' '+clean_trainPath+"\\"+file+'\n')

clean_testPath =r"C:\Users\ssrikrishnan6\Audio-Denoising\clean_testset_wav\clean_testset_wav"
noisy_testPath =r"C:\Users\ssrikrishnan6\Audio-Denoising\noisy_testset_wav\noisy_testset_wav"

test_files = os.listdir(clean_testPath)
with open(r'C:\Users\ssrikrishnan6\Audio-Denoising\test_dataset.txt', 'w+') as f:
    for file in test_files:
        f.write(noisy_testPath+"\\"+file+' '+clean_testPath+"\\"+file+'\n')
