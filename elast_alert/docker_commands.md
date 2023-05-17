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

# Save changes made to container and make it into a new image:

sudo docker commit <container_id> <new_image_name>
