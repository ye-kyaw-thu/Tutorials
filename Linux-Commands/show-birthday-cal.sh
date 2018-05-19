#!/usr/bin/env bash

read -p "Enter your birth year.  (Example: 1980) : " birth_year
read -p "Enter your birth month. (Example: 01) " birth_month

echo -e "\n One month birthday calendar for you ...\n"
cal $birth_month $birth_year  
