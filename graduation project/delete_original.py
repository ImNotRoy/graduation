import os

base_dir='D:\毕设\graduation project\data'
train_dir=os.path.join(base_dir,'train')
validation_dir=os.path.join(base_dir,'validation')
train_real_dir=os.path.join(train_dir,'real')
train_synthesis_dir=os.path.join(train_dir,'synthesis')
files=os.listdir(train_real_dir)
print(files)