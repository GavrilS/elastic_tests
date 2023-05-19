# Create a docker container to install ElastAlerts:

docker pull ubuntu
docker run -i -t ubuntu bash

# Install necessary tools:

1. Python 3:

- Using apt
  (sudo) apt update
  (sudo) apt install software-properties-common
  sudo add-apt-repository ppa:deadsnakes/ppa
  sudo apt update
  sudo apt install python3.8
  python --version

- Install from source
  sudo apt update
  sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget
  cd /tmp
  wget https://www.python.org/ftp/python/3.11.3/Python-3.11.3.tgz
  tar -xf Python-3.11.3.tgz
  cd python-3.11.3
  ./configure --enable-optimizations
  sudo make altinstall(to not override existing python installation)
  or sudo make install(to override existing installation)
  python3 --version

  sudo apt install python3-pip
  pip install --upgrade pip
  sudo apt install git

# Save changes made to container and make it into a new image:

sudo docker commit <container_id> <new_image_name>
docker commit 482fda53a312 ubuntu-python3

# Set up elastalert

- https://elastalert.readthedocs.io/en/latest/running_elastalert.html

git clone https://github.com/Yelp/elastalert.git
pip install "setuptools>=11.3"
python setup.py install
