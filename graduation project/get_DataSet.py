import os
import glob
import random
import shutil
"""only have to be done once"""
base_dir='D:\毕设\graduation project'
ori_real_dir=os.path.join(base_dir,'Celeb-real')
ori_synthesis_dir=os.path.join(base_dir,'Celeb-synthesis')

train_real_dir=os.path.join(base_dir,'data','train','real')
train_syn_dir=os.path.join(base_dir,'data','train','synthesis')

val_real_dir=os.path.join(base_dir,'data','validation','real')
val_syn_dir=os.path.join(base_dir,'data','validation','synthesis')

test_real_dir=os.path.join(base_dir,'data','test','real')
test_syn_dir=os.path.join(base_dir,'data','test','synthesis')

real_files=glob.glob(os.path.join(ori_real_dir,'*'))
random.shuffle(real_files)

synthesis_files=glob.glob(os.path.join(ori_synthesis_dir,'*'))
random.shuffle(synthesis_files)


for real_file in real_files[:int(len(real_files)*0.6)]:
    real_fname=real_file.replace(ori_real_dir+'\\','')
    dst=os.path.join(train_real_dir,real_fname)
    shutil.copyfile(real_file,dst)

print('total training real videos:',len(os.listdir(train_real_dir)))

for synthesis_file in synthesis_files[:int(len(synthesis_files)*0.6)]:
    synthesis_fname=synthesis_file.replace(ori_synthesis_dir+'\\','')
    dst=os.path.join(train_syn_dir,synthesis_fname)
    shutil.copyfile(synthesis_file,dst)

print('total training synthesis videos:',len(os.listdir(train_syn_dir)))

for real_file in real_files[int(len(real_files)*0.6):int(len(real_files)*0.8)]:
    real_fname=real_file.replace(ori_real_dir+'\\','')
    dst=os.path.join(val_real_dir,real_fname)
    shutil.copyfile(real_file,dst)

print('total validation real videos:',len(os.listdir(val_real_dir)))

for synthesis_file in synthesis_files[int(len(synthesis_files) * 0.6):int(len(synthesis_files) * 0.8)]:
    synthesis_fname = synthesis_file.replace(ori_synthesis_dir + '\\', '')
    dst = os.path.join(val_syn_dir, synthesis_fname)
    shutil.copyfile(synthesis_file, dst)

print('total validation synthesis videos:', len(os.listdir(val_syn_dir)))

for real_file in real_files[int(len(real_files)*0.8):]:
    real_fname=real_file.replace(ori_real_dir+'\\','')
    dst=os.path.join(test_real_dir,real_fname)
    shutil.copyfile(real_file,dst)

print('total test real videos:',len(os.listdir(test_real_dir)))

for synthesis_file in synthesis_files[int(len(synthesis_files)*0.8):]:
    synthesis_fname=synthesis_file.replace(ori_synthesis_dir+'\\','')
    dst=os.path.join(test_syn_dir,synthesis_fname)
    shutil.copyfile(synthesis_file,dst)

print('total test synthesis videos:',len(os.listdir(test_syn_dir)))