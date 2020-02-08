#!/usr/bin/env bash

pip3 install --user imgurpython
pip3 install --user selenium
tar -xzf bin/geckodriver-v0.26.0-linux64.tar.gz -C bin
sudo mv bin/geckodriver /usr/local/bin/geckodriver
