from distutils.core import setup
import os
#from setuptools import setup, find_packages
setup(

  name = 'inspyre',        
  packages = ['inspyre'],  
  version = '1.0.1',       
  license='MIT',        
  description = 'Code to quickly create Instagram Grids and continuos posts',   
  author = 'Dheeraj Pai',        
  author_email = 'contact@advaitlabs.com',      # Type in your E-Mail
  url = 'https://github.com/dheerajmpai/saenews/',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/dheerajmpai/saenews/archive/v_033.tar.gz',
  keywords = ['Instagram','Social Media','Photo editing','Photo Cutting', 'Instagram Grid' , 'OPENCV', 'IMAGE PROCESSING'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'beautifulsoup4',
          'opencv-contrib-python',
          'Pillow',
          'matplotlib',
          'requests',
          'saenews'
      
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
#    'Intended Audience :: Image Processing Scientists',
#    'Intended Audience :: Social Media Influencers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
)

print ('HHHHEEEEInstalled')
os.popen('mkdir /home/pai/HELLO_BOBO12345678')

