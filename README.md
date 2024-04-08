# Assignment on Cryptocurrency Analysis and Image Classification

## Submitted by : A00463237

This repository hosts the Python assignment for creating interactive Streamlit applications focused on cryptocurrency analysis and an image classifier for digit recognition. The assignment is divided into three parts:

## Part 1: Stock Details App

This Streamlit application leverages the CoinGecko API to present an interactive analysis of cryptocurrency data. Users can input a cryptocurrency name (e.g., Bitcoin, Ethereum), and the app will display:

- A plot of the coin's price over the last year (52 weeks).
- Maximum and minimum prices during that timeframe.
- Dates when the coin traded at its highest and lowest.

### API Used

- Coin List: `https://api.coingecko.com/api/v3/coins/list`

## Part 2: Coin Comparison App

Building on the first app, this Streamlit application allows users to compare the price performance of two cryptocurrencies. Features include:

- Overlaid price performance graphs of two selected coins.
- Interactive time frame selection (1 week, 1 month, 1 year, 5 years).

## Part 3: Image Classifier

An image classification Streamlit app that identifies digits (0-9) in uploaded images. The model demonstrates a test accuracy of 0.9919. Key features:

- Users can upload square images of digits for classification.
- The model automatically resizes uploaded images for processing.
- Built using the model from class sessions.

### Test Accuracy of the Image Classifier Model

- Test accuracy: 0.9919000267982483

## Streamlit Cloud Deployment

Please visit the following URL to interact with the deployed application:

- [Streamlit Application](https://streamlit.io/cloud)


## How to Use

Instructions on how to run the applications locally and interact with the deployed versions can be found in the corresponding application directories within this repository.

## Requirements

All required Python packages and dependencies are listed in the `requirements.txt` file. Install them using:

```sh
pip install -r requirements.txt
