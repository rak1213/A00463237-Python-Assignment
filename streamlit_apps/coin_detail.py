import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from utils.crypto_utils import fetch_all_coins_list, fetch_historical_data

def show_app_crypto_detail():
    # Streamlit App Title
    st.title('Cryptocurrency Details App')

    # Fetching all available coins
    def fetch_coins_list():
        response = fetch_all_coins_list()
        return response if response is not None else []

    # Fetching historical data of a coin 
    def fetch_single_coin_historical_data(coin_id):
        response = fetch_historical_data(coin_id, 365)
        return response if response is not None else {}

    coins_list = fetch_coins_list()
    coins_names = [coin['name'] for coin in coins_list]

    # User input for cryptocurrency name with a dropdown menu
    default_index = coins_names.index('Bitcoin') if 'Bitcoin' in coins_names else 0
    user_input = st.selectbox('Select the cryptocurrency:', options=coins_names, index=default_index).lower()
    coin_id = next((coin['id'] for coin in coins_list if coin['name'].lower() == user_input), None)

    if coin_id:
        data = fetch_single_coin_historical_data(coin_id)
        if data:
            prices = pd.DataFrame(data, columns=['timestamp', 'price'])
            prices['date'] = pd.to_datetime(prices['timestamp'], unit='ms')
            
            # Plotting with Plotly  
            if not prices.empty:
                fig = go.Figure()
                fig.add_trace(go.Scatter(x=prices['date'], y=prices['price'], mode='lines', name='Price'))
                fig.update_layout(title=f'{user_input.capitalize()} Price Chart (Last Year)', xaxis_title='Date', yaxis_title='Price in USD')
                st.plotly_chart(fig, use_container_width=True)
                
                # Display max and min prices and dates
                max_price = prices['price'].max()
                min_price = prices['price'].min()
                max_date = prices.loc[prices['price'].idxmax()]['date']
                min_date = prices.loc[prices['price'].idxmin()]['date']

                col1, col2 = st.columns(2)
                col1.metric("Maximum Price", f"${max_price:.3f}", f"On {max_date.strftime('%Y-%m-%d')}")
                col2.metric("Minimum Price", f"${min_price:.3f}", f"On {min_date.strftime('%Y-%m-%d')}", delta_color="inverse")
            else:
                st.error("No price data available for the selected cryptocurrency.")
        else:
            st.error("Failed to fetch historical data.")
    else:
        st.info("Please enter a cryptocurrency name.")
