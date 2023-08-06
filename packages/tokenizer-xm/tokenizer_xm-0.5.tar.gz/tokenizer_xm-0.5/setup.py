from setuptools import setup, Extension

with open('./README.md') as f:
    long_description = f.read()

setup(
  name = 'tokenizer_xm',         # How you named your package folder (MyLib)
  packages = ['tokenizer_xm'],   # Chose the same as "name"
  version = '0.5',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Tokenizing with options to include contractions, lemmatize and stem.',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type='text/markdown', 
  author = 'Xiao Ma',                   # Type in your name
  author_email = 'Marshalma0923@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/ALaughingHorse/tokenizer_xm',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/ALaughingHorse/tokenizer_xm/archive/v_05.tar.gz',    # I explain this later on
  keywords = ['text preprocessing', 'tokenize', 'NLP'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'nltk',
          'gensim',
          'pandas'
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