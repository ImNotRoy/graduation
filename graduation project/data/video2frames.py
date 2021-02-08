import csv
import glob
import os
import os.path
from subprocess import call

"""run it before delete_mp4"""


def video2frames():
    """make the video to the frames"""
    base_dir = '/graduation project/data'
    data_file = []
    folders = ['train', 'validation', 'test']
    i = 0
    for folder in folders:
        class_folders = glob.glob(os.path.join(base_dir, folder))
        ##训练或者验证或者测试
        ##       print(class_folders)

        for class_folder in class_folders:
            video_classes = glob.glob(os.path.join(class_folder, '*'))
            ##分类-真或假
            ##            print(video_classes)

            for video_class in video_classes:
                video_dir = glob.glob(os.path.join(video_class, '*.mp4'))
                ##文件地址
                ##                print(video_dir)

                for video_path in video_dir:
                    video_parts = get_video_parts(video_path, folder, class_folder, video_class)
                    purpose, classname, filename_no_ext, filename = video_parts

                    if not check_already_extracted(video_class, filename_no_ext):
                        src = video_path
                        dest = os.path.join(video_class, filename_no_ext + '-%04d.jpg')
                        call(["ffmpeg", "-i", src, dest])
                    i += 1
                    video_frames = get_frames_for_video(video_class, filename_no_ext)
                    print('totally %d videos have been extracted' % i)
                    data_file.append([purpose, classname, filename_no_ext, video_frames])
                    print(filename_no_ext + '   frames   ')
                    print(video_frames)

    with open('data_file.csv', 'w', newline='') as fout:
        writer = csv.writer(fout)
        writer.writerows(data_file)


def get_video_parts(video_path, folder, class_folder, video_class):
    """give a full path to a video, return its parts"""
    filename = video_path.replace(video_class + '\\', '')
    filename_no_ext = filename.replace('.mp4', '')
    classname = video_class.replace(class_folder + '\\', '')
    purpose = folder
    return purpose, classname, filename_no_ext, filename


def check_already_extracted(video_class, filename_no_ext):
    return bool(os.path.exists(os.path.join(video_class, filename_no_ext + '-0001.jpg')))


def get_frames_for_video(video_class, filename_no_ext):
    video_frames = glob.glob(os.path.join(video_class, filename_no_ext + '*.jpg'))
    return len(video_frames)


video2frames()
