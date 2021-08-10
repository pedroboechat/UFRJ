@ECHO off

cd .\c
gcc main.c -o main

cd ..\fortran
gfortran main.f95 -o main

cd ..