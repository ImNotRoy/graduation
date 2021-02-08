import os

"""show the number of total images"""
base_dir = 'D:\毕设\graduation project\data'
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')
test_dir = os.path.join(base_dir, 'test')

train_real_dir = os.path.join(train_dir, 'real')
train_synthesis_dir = os.path.join(train_dir, 'synthesis')

validation_real_dir = os.path.join(validation_dir, 'real')
validation_synthesis_dir = os.path.join(validation_dir, 'synthesis')

test_real_dir = os.path.join(test_dir, 'real')
test_synthesis_dir = os.path.join(test_dir, 'synthesis')

print('total training real images:', len(os.listdir(train_real_dir)))
print('total training synthesis images:', len(os.listdir(train_synthesis_dir)))
print('')
print('total validation real images:', len(os.listdir(validation_real_dir)))
print('total validation synthesis images:', len(os.listdir(validation_synthesis_dir)))
print('')
print('total test real images:', len(os.listdir(test_real_dir)))
print('total test synthesis images:', len(os.listdir(test_synthesis_dir)))
