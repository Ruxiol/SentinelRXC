![](https://crypto.ba/uploads/default/original/1X/b208f356085ca24f7dd57fcd304fad8f8b0552b5.png)
# RXC Sentinel
[![Build Status](https://travis-ci.org/dashpay/sentinel.svg?branch=master)](https://travis-ci.org/dashpay/sentinel)

> An automated governance helper for RXC Masternodes.

Sentinel is an autonomous agent for persisting, processing and automating RXC governance objects and tasks. It is a Python application which runs alongside the RXC Core instance on each RXC Masternode.

## Table of Contents
- [Install](#install)
  - [Dependencies](#dependencies)
- [Usage](#usage)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Maintainer](#maintainer)
- [Contributing](#contributing)
- [License](#license)

## Install

These instructions cover installing Sentinel on Ubuntu 16.04 / 18.04.

### Dependencies

Make sure Python version 2.7.x or above is installed:

    python --version

Update system packages and ensure virtualenv is installed:

    $ sudo apt-get update
    $ sudo apt-get -y install python-virtualenv

### Install Sentinel

Clone the Sentinel repo and install Python dependencies.

    $ git clone https://github.com/Ruxiol/SentinelRXC && cd SentinelRXC
    $ virtualenv ./venv
    $ ./venv/bin/pip install -r requirements.txt

## Usage

Sentinel is "used" as a script called from cron every minute.

### Set up Cron

Set up a crontab entry to call Sentinel every minute:

    $ sudo crontab -e

In the crontab editor, add the lines below, replacing '/path/to/sentinel' to the path where you cloned sentinel to:

    * * * * * cd /path/to/sentinel && ./venv/bin/python bin/sentinel.py >/dev/null 2>&1

### Test Configuration

Test the config by running tests:

    $ ./venv/bin/py.test ./test

With all tests passing and crontab setup, Sentinel will stay in sync with dashd and the installation is complete

## Configuration

An alternative (non-default) path to the `ruxcrypto.conf` file can be specified in `sentinel.conf`:

    dash_conf=/path/to/ruxcrypto.conf

## Troubleshooting

To view debug output, set the `SENTINEL_DEBUG` environment variable to anything non-zero, then run the script manually:

    $ SENTINEL_DEBUG=1 ./venv/bin/python bin/sentinel.py

## Maintainer

[@rux](https://github.com/ruxiol)

![](https://crypto.ba/uploads/default/original/1X/b208f356085ca24f7dd57fcd304fad8f8b0552b5.png)
