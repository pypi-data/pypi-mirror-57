from setuptools import setup, find_packages 
  
with open('requirements.txt',encoding="utf-16", errors="surrogateescape") as f: 
    requirements = f.readlines() #utf-16 might be crucial, other wise unreadble numbers 
  
long_description = 'dont not use it without acknowledgement-useless.' #optional
  
setup( 
        name ='test_deploy_package', #package name 
        version ='1.0.8', #need to change every time you make any modification
        author ='Qi', 
        author_email ='lihqih@gmail.com', 
        url ='https://github.com/Qili-test/test-deploy', 
        description ='Demo', 
        long_description = long_description, 
        long_description_content_type ="text/markdown", 
        license ='MIT', 
        packages = find_packages(), 
        entry_points ={ 
            'console_scripts': [ 
                'test_deploy = test_deploy_package.test_deploy:main'
            ] #package_name(foldername).(main script)
        }, 
        classifiers =( 
            "Programming Language :: Python :: 3", 
            "License :: OSI Approved :: MIT License", 
            "Operating System :: OS Independent", 
        ), 
        python_requires='>=3.5',#only python 3 supported no python 2 support
        keywords ='test deploy ', 
        install_requires = requirements, #all necessary packages will be downloaded and compiled
        zip_safe = False
) 