# !/bin/sh

# curl -fsSL https://raw.githubusercontent.com/cloudmesh/cloudmesh.robot/master/bin/osx/setup.sh | sh 

xcode-select --install

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

brew update
brew install pyenv pyenv-virtualenv pyenv-virtualenvwrapper
brew install readline xz


pip install pyserial
brew tap mengbo/ch340g-ch34g-ch34x-mac-os-x-driver https://github.com/mengbo/ch340g-ch34g-ch34x-mac-os-x-driver
brew cask install wch-ch34x-usb-serial-driver

brew install lua
brew install picocom
brew install wget

brew install libusb
brew install mosquitto

brew cask install aquamacs
brew cask install adafruit-arduino
brew cask install pycharm-ce

pip install numpy
pip install matplotlib
echo "backend : TkAgg" > ~/.matplotlib/matplotlibrc

pyenv install 3.6.1
pyenv virtualenv 3.6.1 ENV3
