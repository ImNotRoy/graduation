import os

"""remove original *.mp4"""
base_dir = '/graduation project/data'
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')
test_dir = os.path.join(base_dir, 'test')

train_real_dir = os.path.join(train_dir, 'real')
train_synthesis_dir = os.path.join(train_dir, 'synthesis')
validation_real_dir = os.path.join(validation_dir, 'real')
validation_synthesis_dir = os.path.join(validation_dir, 'synthesis')
test_real_dir = os.path.join(test_dir, 'real')
test_synthesis_dir = os.path.join(test_dir, 'synthesis')

files = os.listdir(train_real_dir)
for file in files:
    if file.endswith(".mp4"):
        print(os.path.join(train_real_dir, file))
        os.remove(os.path.join(train_real_dir, file))
        print("successfully remove")
files = os.listdir(train_synthesis_dir)
for file in files:
    if file.endswith(".mp4"):
        print(os.path.join(train_synthesis_dir, file))
        os.remove(os.path.join(train_synthesis_dir, file))
        print("successfully remove")
files = os.listdir(validation_synthesis_dir)
for file in files:
    if file.endswith(".mp4"):
        print(os.path.join(validation_synthesis_dir, file))
        os.remove(os.path.join(validation_synthesis_dir, file))
        print("successfully remove")
files = os.listdir(validation_real_dir)
for file in files:
    if file.endswith(".mp4"):
        print(os.path.join(validation_real_dir, file))
        os.remove(os.path.join(validation_real_dir, file))
        print("successfully remove")
files = os.listdir(test_synthesis_dir)
for file in files:
    if file.endswith(".mp4"):
        print(os.path.join(test_synthesis_dir, file))
        os.remove(os.path.join(test_synthesis_dir, file))
        print("successfully remove")
files = os.listdir(test_real_dir)
for file in files:
    if file.endswith(".mp4"):
        print(os.path.join(test_real_dir, file))
        os.remove(os.path.join(test_real_dir, file))
        print("successfully remove")
