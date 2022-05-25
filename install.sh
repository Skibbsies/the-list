#!/bin/bash

echo "Creating virtual environment..."

pip install virtualenv

virtualenv env_list

echo "Copying program files to virtual environment..."

for file in resources/*; do cp -r $file env_list; done

echo "Deleting original program files..."

rm -rf resources

rm install.sh

echo "Upgrading pip..."

env_list/bin/python -m pip install --upgrade pip

echo "Installing packages..."

env_list/bin/pip install pysimplegui
