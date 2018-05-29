
sudo apt-get install build-essential libbz2-dev libssl-dev \
                     libreadline-dev libsqlite3-dev tk-dev -y

curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> /home/vagrant/.bashrc
echo 'eval "$(pyenv init -)"' >> /home/vagrant/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> /home/vagrant/.bashrc

export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

pyenv install 3.6.0
pyenv virtualenv 3.6.0 general
pyenv global general

pip install django djongo \
            pymongo \
            scrapy xmltodict
