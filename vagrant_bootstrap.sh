#!/bin/bash


# Install git for version control, pip for install python packages
echo 'Installing git, Python 3, and pip...'
sudo apt-get install -y language-pack-es libfreetype6-dev
#ziblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
sudo apt-get -qq install build-essential git python3 python3-dev libjpeg-dev libtiff5-dev zlib1g-dev postgresql-9.5 libpq5 libpq-dev > /dev/null 2>&1
curl -s https://bootstrap.pypa.io/get-pip.py | python3.5 > /dev/null 2>&1

# Install virtualenv / virtualenvwrapper
echo 'Installing and configuring virtualenv and virtualenvwrapper...'
pip install --quiet virtualenvwrapper==4.7.0 Pygments==2.1.1
mkdir -p ~ubuntu/virtualenvs
chown ubuntu:ubuntu ~ubuntu/virtualenvs
printf "\n\n# Virtualenv settings\n" >> ~ubuntu/.bashrc
printf "export PYTHONPATH=/usr/lib/python3\n" >> ~ubuntu/.bashrc
printf "export WORKON_HOME=~ubuntu/virtualenvs\n" >> ~ubuntu/.bashrc
printf "export PROJECT_HOME=/srv/webapp\n" >> ~ubuntu/.bashrc
printf "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3\n" >> ~ubuntu/.bashrc
printf "source /usr/local/bin/virtualenvwrapper.sh\n" >> ~ubuntu/.bashrc

# Some useful aliases for getting started, MotD
echo 'Setting up message of the day, and some aliases...'

printf "# \nUseful Aliases:\n" >> ~ubuntu/.bashrc
printf "alias menu='cat /etc/motd'\n" >> ~ubuntu/.bashrc
printf "alias runserver='python manage.py runserver 0.0.0.0:8000'\n" >> ~ubuntu/.bashrc
printf "alias ccat='pygmentize -O style=monokai -f terminal -g'\n" >> ~ubuntu/.bashrc

# Complete
echo ""
echo "Vagrant install complete."
echo "Now try logging in:"
echo "    $ vagrant ssh"

echo """
mkvirtualenv webapp
workon webapp
pip install -r /srv/webapp/requirements.txt
"""
