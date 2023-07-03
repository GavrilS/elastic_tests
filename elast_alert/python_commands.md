# Install Elastalert with python on Ubuntu
* Docs: https://elastalert.readthedocs.io/en/latest/running_elastalert.html

* Requirements:
    - Linux distribution(I am using ubuntu) or WSL on Windows
    - python version 3.10 or higher

<!-- * Steps:
    - Install virtualenv: sudo apt install python3.10-venv
    - Set up venv: python3 -m venv env
    - Activate the virtual environment: source env/bin/activate
    - Install Elastalert: pip install elastalert -->


* Steps:
    - Install virtualenv: sudo apt install python3.10-venv
    - Set up venv: python3 -m venv env
    - Activate the virtual environment: source env/bin/activate
    - pip3 install -r requirements.txt
    - Clone the repo: git clone https://github.com/Yelp/elastalert.git
    - pip3 install "setuptools>=11.3"
    - cd elastalert
    - python3 setup.py install 


* Run Elastalert:
python3 -m elastalert.elastalert --verbose
