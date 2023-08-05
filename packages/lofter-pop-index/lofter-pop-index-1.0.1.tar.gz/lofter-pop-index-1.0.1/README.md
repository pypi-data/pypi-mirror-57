# lofter-pop-index
An automatic tool used for increasing LOFTER blogs' popular index.

## Introduction
This is an an automatic tool used for increasing LOFTER blogs' popular index. The program can control a chrome browser, the process of login and click the buttons are totally automatic and high efficient.

To run the program, you should provide some lofter accounts and target blogs' list. Due to the illegal using detecting system of LOFTER, preparing a list of http proxies is highly recommended. 

## How to Use
* Install

```
pip3 install lofter-pop-index
```

* Run

To get the using guide:

```
python3 lofter-pop-index
```

## Attention
1. In some cases, there may have a robot detecting system during the process. Unfortunately, the problem still cannot be solved. However, we have found that if the account register place is same as login place (base on ip address), LOFTER will not require a robot detect.

2. A low speed proxy may cause a failure, if you want to use proxies, please make sure they have enough bandwidth.

## License
GPLv3