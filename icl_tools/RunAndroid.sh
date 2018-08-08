#! /bin/bash

make clean
. build/envsetup.sh
lunch android_x86_64-eng
m -j4 iso_img
