# Morse Code converter
文字列をモールス信号に変換する

## About
対応している文字: 
- 数字: 0~9
- アルファベット: A ~ Z, a ~ z
- 和文: ア~ン
- 記号: +-*/:(),.'"?@゛゜ー、（）

## Requirement
- lang: python3
-  CUI

### How to Use:

  *text to convert*
  ```
  $python3 morse-code.py -i 'text to convert'
  --*-- MorseCode --*--
  input: 'text to convert'
  - ･ -･･- - - --- -･-･ --- -･ ･･･- ･ ･-･ -
  ```
  *Detail view*
  ```
  $python3 morse-code.py -d -i 'detail view'
  --*-- MorseCode --*--
  input: 'detail view'
  D:: -･･
  E:: ･
  T:: -
  A:: ･-
  I:: ･･
  L:: ･-･･
  V:: ･･･-
  I:: ･･
  E:: ･
  W:: ･--
  ```
  *tools help*
  ```
  $python3 morse-code.py -h
  usage: morse-code.py [-h] [-i INPUT] [-a] [-d]

  optional arguments:
    -h, --help            show this help message and exit
    -i INPUT, --input INPUT
                          input string
    -a, --all             all print
    -d, --detail          Detail deiplay of results
  ```
  *Morse tables All view*
  ```
  $python3 morse-code.py -a
  --*-- MorseCode --*--
  --All view mode--
  key:1, value:･----
  key:2, value:･･---
  key:3, value:･･･--
  key:4, value:････-
  key:5, value:･････
  key:6, value:-････
  key:7, value:--･･･
  key:8, value:---･･
  key:9, value:----･
  key:0, value:-----
  key:A, value:･-
  key:B, value:-･･･
  key:C, value:-･-･
  key:D, value:-･･
  key:E, value:･
  key:F, value:･･-･
  
  -- 略 --
  
  key:セ, value:･---･
  key:ス, value:---･-
  key:ン, value:･-･-･
  key:゛, value:･･
  key:゜, value:･･--･
  key:ー, value:･--･-
  key:、, value:･-･-･-
  key:（, value:-･--･-
  key:）, value:･-･･-･
  ```
