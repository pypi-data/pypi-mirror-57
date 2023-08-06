#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup
setup(
    name = 'ImageDiffOps',
    version = '0.0.1',
    py_modules = ['ImageDiffOps'],
    author = 'nikhil130yadav',
    author_email = 'nikhil.nikhil2008@gmail.com',
    url = 'https://github.com/nikhil130yadav/',
    #dependency_links=['https://github.com/nikhil130yadav/']
    description = 'A library to find similarity between two Image files and finding changes in them.',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'scikit-image','numpy','opencv-python'
      ],
)


# In[ ]:




