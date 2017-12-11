#!/bin/bash

mkdir -p Database
mkdir -p DirectoryServerFiles/7001
mkdir -p DirectoryServerFiles/7002
mkdir -p DirectoryServerFiles/7003

python directoryServer.py 7333 &
python fileServer.py 7001 &
python fileServer.py 7002 &

sleep 10 
python initdatabase.py
