#!/bin/sh
echo -n `head -n1337 /dev/urandom | sha512sum | cut -d' ' -f1` > steg0_initial_root_password
