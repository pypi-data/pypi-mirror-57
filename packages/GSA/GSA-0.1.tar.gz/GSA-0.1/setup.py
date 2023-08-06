from distutils.core import setup
setup(
  name = 'GSA',         # How you named your package folder (MyLib)
  packages = ['GSA'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Python Package to implement Gravitational Search Algorithm',   # Give a short description about your library
  author = 'Deepanshu Aggarwal',                   # Type in your name
  author_email = 'deepanshu4929@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/deepanshu1999/GSA',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/deepanshu1999/GSA/archive/0.1.tar.gz',    # I explain this later on
  keywords = ['GRAVITATIONAL', 'SEARCH', 'ALGORITHM','GSA','NATURE','NATURE-INSPIRED','GRAVITATIONAL-SEARCH'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'numpy'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)