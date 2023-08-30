import os
import time

os.system('cls')

print('Welcome to the Python Package Installer.'.upper())
print('Developed by Joboy-Dev\n')
print('NOTE: If you want to install more than one package, separate the packages with a comma(,).')

process = True

while process:
    package_name = input('Enter package(s) you want to install:')

    if len(package_name) > 0:
        if ',' in package_name:
            package_list = [package.strip() for package in package_name.split(',') if len(package) > 0]
        else:
            package_list = [package_name]

        # print(package_list)
        process = False
    else:
        print('Package name cannot be empty')

for package in package_list:
    try:
        os.system(f'pip install {package}')
    except Exception as e:
        print(f"Package '{package}' not found.")

time.sleep(7)