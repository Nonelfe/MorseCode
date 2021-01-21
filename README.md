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

### How to Use:
  *text to convert*
  ```
  $./morse-code.py -e 'text to convert'
  --*-- MorseCode --*--
  input: 'text to convert'
  - ･ -･･- - - --- -･-･ --- -･ ･･･- ･ ･-･ -
  ```
  *Detail view*
  ```
  $./morse-code.py -v -e 'detail view'
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
  *decode*
  ```
  $./morse-code.py -d '･･･ --- ･･･'
  --*-- MorseCode --*--
  input: '･･･ --- ･･･ '
  result:SOS
  ```
  *decode wabun*
  ```
  $./morse-code.py --wabun -d '--･-- ･- ･･- -･--- ･-･･･'
  --*-- MorseCode --*--
  input: '--･-- ･- ･･- -･--- ･-･･･'
  result:アイウエオ
  ```
  *tools help*
  ```
  $./morse-code.py -h
  uusage: morse-code.py [-h] [-e ENCODE] [-a] [-v] [-d DECODE]
                     [--wabun]

  optional arguments:
    -h, --help            show this help message and exit
    -e ENCODE, --encode ENCODE
                          input string
    -a, --all             all print
    -v, --verbose         Detail deiplay of results
    -d DECODE, --decode DECODE
                          morse code decoding
    --wabun               morse code decoding wabun

  ```
  *Morse tables All view*
  ```
  $./morse-code.py -a
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
