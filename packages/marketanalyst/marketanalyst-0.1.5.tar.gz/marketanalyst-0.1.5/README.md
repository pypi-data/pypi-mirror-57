## requirement

This library requires greater than 3.6 version of python.

## Installment:
First install marketanalyst package from pip so do
```bash
pip install marketanalyst
python -m pip install marketanalyst
```
This will download the package itself and dependencies that is uses.

## How to use:

```python
import marketanalyst
```
Make a client which can be used to call all the other methods.
```python
client = marketanalyst.client("your api key","your secret key")
```
The client is ready to use, it can be used to call the below methods.

## Methods:

All of these methods will return either a string with error message or a dataframe as a success
1) Getallsecurities:
```python
df = client.Getallsecurities()
```
This will return a dataframe like this:
```bash
          id      title
0      71877  AMEX:AAAU
1      71878  AMEX:AADR
2      67702  AMEX:AAMC
3      48525   AMEX:AAU
4      71880  AMEX:ACIM
...      ...        ...
20631  56925    TSX:YRI
20632  56932    TSX:ZAR
20633  56933    TSX:ZAZ
20634  56934    TSX:ZCL
20635  56935    TSX:ZNC

[20636 rows x 2 columns]
```

Here title is the name of security and id represents the database id that was assigned to this security.

2) getallcategory:
```python
df = client.getallcategory()
```
This will return a dataframe like this:
```bash
   id            title
0   1      Commodities
1   2       Currencies
2   5   Global Indices
3  27    Hong Kong ETF
4  15  Indian Equities
5  28    Singapore ETF
6  29   Singapore REIT
7   4      US Equities
8  26         USA ETF 
```
3) getallsubcategory:
```python
df = client.getallsubcategory("Commodities")
```
This will return a dataframe like this:
```bash
    id  title
0  464  COMEX
1  463  NYMEX
```
4) getallportfolio:
```python
df = client.getallportfolio()
```
This will return a dataframe like this:
```bash
      id                    title
0   8003                   DOW 30
1   8008                    FAANG
2   8004               NASDAQ 100
3   8010                    nmbjk
4   8005             Russell 1000
5   8006             Russell 2000
6   8007             Russell 3000
7   8002                  S&P 400
8   8001                  S&P 500
9   8009    Warren Buffett Stocks
```





5) getallindicator:
```python
df = client.getallindicator()
```
This will return a dataframe like this:

```bash
  id        title
0  1        Price
1  2    Technical
2  3  Fundamental
3  4   Financials
```

6) getallsubindicator:
```python
df = client.getallsubindicator("Price")
```
This will return a dataframe like this:
```bash
  id      title
0  1        EOD
1  2  Analytics
```

7) getdata:
```python
df = client.getdata(["NASDAQ:AAPL"],"01/01/2012","01/01/2019","Price","EOD")
```
This will return a dataframe like this:
```bash
         e      s          i                v         d
0      NASDAQ  AAPL  D_EODCLOSE_EXT_1     58.75  2012-01-03
1      NASDAQ  AAPL  D_EODCLOSE_EXT_1     59.06  2012-01-04
2      NASDAQ  AAPL  D_EODCLOSE_EXT_1     59.72  2012-01-05
3      NASDAQ  AAPL  D_EODCLOSE_EXT_1     60.34  2012-01-06
4      NASDAQ  AAPL  D_EODCLOSE_EXT_1     60.25  2012-01-09
...       ...   ...               ...       ...         ...
17590  NASDAQ  MSFT    D_EODVOL_EXT_1  43935100  2018-12-24
17591  NASDAQ  MSFT    D_EODVOL_EXT_1  51634700  2018-12-26
17592  NASDAQ  MSFT    D_EODVOL_EXT_1  49498500  2018-12-27
17593  NASDAQ  MSFT    D_EODVOL_EXT_1  38169300  2018-12-28
17594  NASDAQ  MSFT    D_EODVOL_EXT_1  33173700  2018-12-31

[17595 rows x 5 columns]
```

8) getOHLCVData:
```python
df = client.getOHLCVData(["NASDAQ:AAPL","NASDAQ:MSFT"],"01/01/2012","01/01/2019")
```
OR 
```python
df = client.getOHLCVData(["NASDAQ:AAPL","NASDAQ:MSFT"],"01/01/2012","01/01/2019","EOD")
```
You can provide sub indicator type like this.
This will return a dataframe like this:
```bash
        datetime   exchange  security open   low     high    close   volume
0     2012-01-03   NASDAQ     AAPL   58.49   58.43   58.93   58.75  75564699
1     2012-01-04   NASDAQ     AAPL   58.57   58.47   59.24   59.06  65061108
2     2012-01-05   NASDAQ     AAPL   59.28   58.95   59.79   59.72  67816805
3     2012-01-06   NASDAQ     AAPL   59.97   59.89   60.39   60.34  79596412
4     2012-01-09   NASDAQ     AAPL   60.79   60.19   61.11   60.25  98505792
...          ...      ...      ...     ...     ...     ...     ...       ...
3514  2018-12-24   NASDAQ     MSFT   97.68   93.98   97.97   94.13  43935100
3515  2018-12-26   NASDAQ     MSFT   95.14   93.96  100.69  100.56  51634700
3516  2018-12-27   NASDAQ     MSFT    99.3    96.4  101.19  101.18  49498500
3517  2018-12-28   NASDAQ     MSFT  102.09   99.52  102.41  100.39  38169300
3518  2018-12-31   NASDAQ     MSFT  101.29  100.44   102.4  101.57  33173700

[3519 rows x 8 columns]
```
9) export_df:
With this method you can export a dataframe to a csv or excel.
```python
client.export_df(df,'excel',r"D:\some_folder\filename")
```
This example is for windows.


