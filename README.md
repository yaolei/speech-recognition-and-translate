# speech-recognition-and-translate
This is a speech recognition and translate backend , it's could be translate en to chinese
THis project is only the Backend and code with Python3 
Pls run the request.txt with py3 -Flask (Q:Why not Django and fast Api? A: Both of them are many issues)
In the directory pls in the src create the venv (virtualenv)

提前必须安装
Mac : 
   brew install flac
   brew install PyAudio (麦克风作为音源)
   pip install pyaudio
windows: 
    sudo apt-get install flac
    pip install pyaudio
PIP 环境下：
    step :
    安装虚拟环境库    Pip3 install virtualenv
    python安装  虚拟环境 Python3 -m virtualenv venv
    启动虚拟环境。source venv/bin/activate

Conda 环境下
    Conda create --name venv python=3.10
    Conda activate venv

安装：  
git clone https://github.com/yaolei/speech-recognition-and-translate.git 

cd speech-recognition-and-translate
pip install -r requirements.txt

语言包
 执行language.sh： sh language.sh 加载中文语言包

执行
 python app.py
 前端程序会发送sockie请求，可实时监控并编译

