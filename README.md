# speech-recognition-and-translate
This is a speech recognition and translate backend , it's could be translate en to chinese
THis project is only the Backend and code with Python3 
Pls run the request.txt with py3 -Flask (Q:Why not Django and fast Api? A: Both of them are many issues)
In the directory pls in the src create the venv (virtualenv)
 step :
安装虚拟环境库    Pip3 install virtualenv

 python安装  虚拟环境 Python3 -m virtualenv venv

启动虚拟环境。source venv/bin/activate

安装 django 
pip3 install djangorestframework markdown django-filter

在虚拟环境下执行，如果断开了虚拟环境，再执行一次source
django-admin startproject cmbackend .

 安装cloudinary
pip3 install cloudinary

src 下
python3 manage.py makemigrations

python3 manage.py migrate
