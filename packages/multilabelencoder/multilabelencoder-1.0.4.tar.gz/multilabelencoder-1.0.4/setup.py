from setuptools import setup
setup(  name = 'multilabelencoder',
        version = "1.0.4",
        license = 'MIT',
        description = 'Labelencoder for many pandas dataframe columns package',
#        scripts=['multilabelencoder.py'] ,
        packages = ['multilabelencoder'],
#        package_data = {'hmglib': ['readme.txt']},
        install_requires = ['sklearn'],
        zip_safe = False,
        author = "Emna Jaoua",
        author_email = 'emnajaoua1@gmail.com',
        maintainer = "Emna Jaoua",
        maintainer_email = "emnajaoua1@gmail.com",
        dependency_links= [''],
      url="https://github.com/emnajaoua/multilabelencoder"
     )