from distutils.core import setup
import os
#from setuptools import setup, find_packages
setup(
  name = 'saenews',        
  packages = ['saenews','saenews.hello'],  
  version = '0.0.1',       
  license='MIT',        
  description = 'required code for sae.news',   
  author = 'saenews',        
  author_email = 'contact@advaitlabs.com',      # Type in your E-Mail
  url = 'https://github.com/dheerajmpai/saenews/',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/dheerajmpai/saenews/archive/v_033.tar.gz',
  keywords = ['OPENCV', 'IMAGE PROCESSING', 'NEWS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'beautifulsoup4',
          'opencv-contrib-python',
          'Pillow',
          'matplotlib',
          'requests'
          
      
      ],
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
)

print ('Installed')
#os.popen('mkdir /home/pai/HELLO_BOBO1234')

