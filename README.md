# Bitcoin Price Forecasting

**Welcome to Bitcoin Price Forecasting!**

In this repository, we explore techniques to forecast Bitcoin prices. This is mostly an exercise in time series prediction.

In our example, we use [Facebook's Prophet ](https://facebook.github.io/prophet/) to forecast Bitcoin's future price. Along the way, we use additional information about the Bitcoin network to improve our predictions. As a bonus, we also predict Ethereum's price.

## Data

Price data for Bitcoin and Ethereum were obtained from [Yahoo! Finance](https://finance.yahoo.com/).

For the regressors, we use a variety of additional data provided in this repository for convenience. We include
* the number of unique addresses
* the difficulty of mining as time progresses
* the hash rate
* the total number of Bitcoins in circulation
* the S&P 500 index value
* the US 13 week Treasury Bill rate
* the number of transactions excluding popular addresses
* the average block size in MB
* search trend sentiment from [Google Trends](https://trends.google.com/trends)

Bitcoin and Ethereum network data were obtained from [Quandl](https://www.quandl.com/data/BCHAIN-Blockchain).

**Disclaimer**: the work in this notebook should not be be used in making financial decisions. Please understand the risks involve when trading cryptocurrencies or any financial instrument.
