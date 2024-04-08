import streamlit as st
import plotly.graph_objs as go
import pandas as pd
from utils.crypto_utils import fetch_all_coins_list, fetch_historical_data, unix_to_datetime

def show_app_crypto_comparison():
    # Streamlit App Title
    st.title('Cryptocurrency Comparison App')

    # Fetch the list of all coins using the utility function
    coins_list = fetch_all_coins_list()
    coins_dict = {coin['id']: coin['name'] for coin in coins_list}

    # Selection boxes for cryptocurrencies
    coin1_id = st.selectbox('Select the first cryptocurrency:', options=list(coins_dict.keys()), format_func=lambda x: coins_dict[x])
    coin2_id = st.selectbox('Select the second cryptocurrency:', options=list(coins_dict.keys()), format_func=lambda x: coins_dict[x], index=1 if coin1_id == list(coins_dict.keys())[0] else 0)

    # Check if the user has selected the same cryptocurrency for both selections
    if coin1_id == coin2_id:
        st.error('Please select two different cryptocurrencies for comparison.')
    else:
        time_frames = {
            '1 week': 7,
            '1 month': 30,
            '1 year': 365
        }
        selected_time_frame = st.selectbox('Select time frame:', options=list(time_frames.keys()))
        days = time_frames[selected_time_frame]

        # Fetching the historical data for both coins
        coin1_data = fetch_historical_data(coin1_id, days)
        coin2_data = fetch_historical_data(coin2_id, days)

        # Check if data is available and not empty for both coins
        if coin1_data and coin2_data:
            # Convert the data to DataFrames
            coin1_df = pd.DataFrame(coin1_data, columns=['timestamp', 'price'])
            coin2_df = pd.DataFrame(coin2_data, columns=['timestamp', 'price'])

            # Convert UNIX timestamps to datetime
            coin1_df['date'] = coin1_df['timestamp'].apply(unix_to_datetime)
            coin2_df['date'] = coin2_df['timestamp'].apply(unix_to_datetime)

            # Plotting with Plotly
            fig = go.Figure()
            # First cryptocurrency trace
            fig.add_trace(go.Scatter(x=coin1_df['date'], y=coin1_df['price'], mode='lines', name=coins_dict[coin1_id], yaxis='y1'))

            # Second cryptocurrency trace
            fig.add_trace(go.Scatter(x=coin2_df['date'], y=coin2_df['price'], mode='lines', name=coins_dict[coin2_id], yaxis='y2'))

            # Layout for separate Y-axes
            fig.update_layout(
                title=f'Price Comparison: {coins_dict[coin1_id]} vs {coins_dict[coin2_id]} over {selected_time_frame}',
                xaxis_title='Date',
                yaxis=dict(title=f'{coins_dict[coin1_id]} Price in USD', side='left'),
                yaxis2=dict(title=f'{coins_dict[coin2_id]} Price in USD', side='right', overlaying='y', showgrid=False),
                legend=dict(x=0.05, y=1.1, orientation='h')
            )

            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error('Could not fetch data for the selected cryptocurrencies.')

