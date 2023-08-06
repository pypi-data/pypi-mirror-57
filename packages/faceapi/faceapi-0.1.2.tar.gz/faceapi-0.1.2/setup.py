from setuptools import setup
import os

PATH_ROOT = os.path.dirname(__file__)

with open("README.org", "r") as fh:
    long_description = fh.read()


def load_requirements(path_dir=PATH_ROOT, comment_char='#'):
    with open(os.path.join(path_dir, 'requirements.txt'), 'r') as file:
        lines = [ln.strip() for ln in file.readlines()]
    reqs = []
    for ln in lines:
        # filer all comments
        if comment_char in ln:
            ln = ln[:ln.index(comment_char)]
        if ln:  # if requirement is not empty
            reqs.append(ln)
    return reqs


setup(name='faceapi',
      version='0.1.2',
      description='Face detector and recognition',
      author='Ellery Wang',
      author_email='elleryq92@gmail.com',
      # long_description=long_description,
      packages=['faceapi'],
      package_data={'faceapi': ['faceapi/face_recognition_models/models/*.dat',
                                "faceapi/resource/ui/*.ui"]},
      install_requires=load_requirements())
