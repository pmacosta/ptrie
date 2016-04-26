#!/bin/bash
# rtest.sh
# Copyright (c) 2013-2016 Pablo Acosta-Serafini
# See LICENSE for details

opath=${PATH}
export PATH=${HOME}/python/python2.6/bin:${HOME}/python/python2.7/bin:${HOME}/python/python3.3/bin:${HOME}/python/python3.4/bin:${HOME}/python/python3.5/bin:${PATH}
tox "$@"
export PATH=${opath}
