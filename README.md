# class_onet

## 安裝方法

要安裝套件，請運行以下命令：
```
pip install git+https://github.com/chengpeter88/Onet@v1.0.0
```

## 解除安裝方法

要解除安裝套件，請使用：
```
pip uninstall Onet
```


```python
#下載自己做標該計畫套件，只需需要下載一次，如果下次執行無法使用以下指令，再下載一次！
pip install git+https://github.com/chengpeter88/class_onet@v1.0.0
```

    Collecting git+https://github.com/chengpeter88/class_onet@v1.0.0
      Cloning https://github.com/chengpeter88/class_onet (to revision v1.0.0) to /tmp/pip-req-build-nf908628
      Running command git clone --filter=blob:none --quiet https://github.com/chengpeter88/class_onet /tmp/pip-req-build-nf908628
      Running command git checkout -q 37e29b50f884fd63a855be724bbee22965f0a9dc
      Resolved https://github.com/chengpeter88/class_onet to commit 37e29b50f884fd63a855be724bbee22965f0a9dc
      Preparing metadata (setup.py) ... [?25l[?25hdone
    Requirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from Onet==1.0.0) (2.31.0)
    Requirement already satisfied: pandas in /usr/local/lib/python3.10/dist-packages (from Onet==1.0.0) (1.5.3)
    Requirement already satisfied: bs4 in /usr/local/lib/python3.10/dist-packages (from Onet==1.0.0) (0.0.1)
    Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.10/dist-packages (from bs4->Onet==1.0.0) (4.11.2)
    Requirement already satisfied: python-dateutil>=2.8.1 in /usr/local/lib/python3.10/dist-packages (from pandas->Onet==1.0.0) (2.8.2)
    Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas->Onet==1.0.0) (2023.3.post1)
    Requirement already satisfied: numpy>=1.21.0 in /usr/local/lib/python3.10/dist-packages (from pandas->Onet==1.0.0) (1.23.5)
    Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests->Onet==1.0.0) (3.3.2)
    Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests->Onet==1.0.0) (3.6)
    Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->Onet==1.0.0) (2.0.7)
    Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests->Onet==1.0.0) (2023.11.17)
    Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.1->pandas->Onet==1.0.0) (1.16.0)
    Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.10/dist-packages (from beautifulsoup4->bs4->Onet==1.0.0) (2.5)



```python
#使用套件

from class_onet import Onet
```


```python
# 設定首先進入職業code總表：https://www.onetonline.org/find/all。 -> 選要的職業EX:Agricultural Engineers -> copy web link to url 可以替換
# 按下播放鍵，初始化模組，出現有打勾即可
url = 'https://www.onetonline.org/link/summary/17-2021.00'

onet=Onet(url=url)
```


```python
# 表格中職業前半資訊
# job zone
# SVP range
# Education
# Time pressure等
## NOTICE : 部分職業魔沒有資訊會出現not found 屬於正常
onet.get_info()
```




    {'Title': 'Job Zone Four: Considerable Preparation Needed',
     'SVP Range': '(7.0 to < 8.0)',
     'Education': "Most of these occupations require a four-year bachelor's degree, but some do not.",
     'Time Pressure': '46% responded “Once a month or more but not every week.”\nRelated occupations',
     'Projected growth': 'Faster than average (5% to 8%)'}




```python
# 表格中項，計算出特定性質出現次數，注意數字只會有1,0 出現不只1次代表有問題，需要人工檢查
onet.work_knowledge()
```

                             Arts and Humanities
    English Language                           1
    Fine Arts                                  0
    Foreign Language                           0
    History and Archeology                     0
    Philosophy and Theology                    0
    Education and Training                     1
                            Health Services
    Medicine and Dentistry                0
    Therapy and Counseling                0
                                   Business and Management
    Administration and Management                        1
    Administrative                                       0
    Customer and Personal Service                        1
    Economics and Accounting                             0
    Personnel and Human Resources                        0
    Sales and Marketing                                  0
                 Mathematics and Science
    Biology                            1
    Chemistry                          1
    Geography                          0
    Mathematics                        2
    Physics                            1
                                Engineering and IT
    Building and Construction                    1
    Computers and Electronics                    1
    Design                                       1
    Engineering and Technology                   1
    Mechanical                                   1
    Communications and Media                     0
    Telecommunications                           0
    Food Production                              1
    Production and Processing                    1
    Transportation                               0



```python
# 表格後半部 ，出現次數需注意有否超過1以上
onet.work_skill()
```

                                  Complex Problem Solving & Systems Skills
    Complex Problem Solving                                              1
    Judgment and Decision Making                                         1
    Systems Analysis                                                     1
    Systems Evaluation                                                   1
                                       Resource Management Skills
    Management of Financial Resources                           0
    Management of Material Resources                            0
    Management of Personnel Resources                           1
    Time Management                                             1
                           Social Skills
    Coordination                       1
    Instructing                        1
    Negotiation                        1
    Persuasion                         1
    Service Orientation                1
    Social Perceptiveness              1
                              Technical Skills
    Equipment Maintenance                    0
    Equipment Selection                      0
    Installation                             0
    Operation and Control                    0
    Operations Analysis                      1
    Operations Monitoring                    1
    Programming                              0
    Quality Control Analysis                 0
    Repairing                                0
    Technology Design                        0
    Troubleshooting                          0



```python

```
