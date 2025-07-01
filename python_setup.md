# pip
## check if pip is installed
pip --V

## executing python programs
py modulename.py
py -m modulename

Example: py C:\Users\jiaern_foo\Learning\advance_python\src\optional_param.py

## update pip
pip install --upgrade pip

## install package with pip from pypi
pip install <package_name>
pip install <package_name> == 2.1.1

## install package with pip from GitHub
pip install <git_repo_url.git>

## install package with pip from offline file
py -m pip install <xxxx.tar.gz>
py -m pip install <xxxx.whl>

## install package from requirements.txt
pip install -r requirements.txt

## view installed lib
pip list

## uninstall lib
pip uninstall <package_name>

## list outdated lib
pip list --outdated --verbose

## get info of the package installed
pip show <package_name>
