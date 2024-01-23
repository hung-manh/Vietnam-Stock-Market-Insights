from .config import *
# Đây là nơi để lưu trữ các hàm liên quan đến phân tích kỹ thuật chứng khoán (vẽ biểu đồ)
def candlestick_chart(df, title='Candlestick Chart with MA and Volume', x_label='Date', y_label='Price', ma_periods=None, show_volume=True, figure_size=(10, 8), reference_period=None, colors=('#00F4B0', '#FF3747'), reference_colors=('blue', 'black')):
    """
    Generate a candlestick chart with optional Moving Averages (MA) lines, volume data, and reference lines.

    Parameters:
    - df: DataFrame with candlestick data ('time', 'open', 'high', 'low', 'close', 'volume', 'ticker').
    - title: Title of the chart.
    - x_label: Label for the x-axis.
    - y_label: Label for the y-axis.
    - ma_periods: List of MA periods to calculate and plot (e.g., [10, 50, 200]).
    - show_volume: Boolean to indicate whether to display volume data.
    - figure_size: Tuple specifying the figure size (width, height).
    - reference_period: Number of days to consider for reference lines (e.g., 90).
    - colors: Tuple of color codes for up and down candles (e.g., ('#00F4B0', '#FF3747')).
    - reference_colors: Tuple of color codes for reference lines (e.g., ('black', 'blue')).

    Returns:
    - Plotly figure object.
    """
    # Create the base candlestick chart
    candlestick_trace = go.Candlestick(
        x=df['TradingDate'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name='Candlestick',
    )

    # Create a figure
    fig = go.Figure(data=[candlestick_trace])

    # Add volume data if specified
    if show_volume:
        df['Volume']=df['Volume'].astype(float)
        volume_trace = go.Bar(
            x=df['TradingDate'],
            y=df['Volume'],
            name='Volume',
            yaxis='y2',  # Use the secondary y-axis for volume
            marker=dict(color=[colors[0] if close >= open else colors[1] for close, open in zip(df['Close'], df['Open'])]),  # Match volume color to candle color
        )

        fig.add_trace(volume_trace)

    # Add Moving Averages (MA) lines if specified
    if ma_periods:
        for period in ma_periods:
            ma_name = f'{period}-day MA'
            df[ma_name] = df['Close'].rolling(period).mean()

            ma_trace = go.Scatter(
                x=df['TradingDate'],
                y=df[ma_name],
                mode='lines',
                name=ma_name,
            )

            fig.add_trace(ma_trace)

    # Add straight reference lines for the highest high and lowest low
    if reference_period:
        df['lowest_low'] = df['Low'].rolling(reference_period).min()
        df['highest_high'] = df['High'].rolling(reference_period).max()

        lowest_low_trace = go.Scatter(
            x=df['TradingDate'],
            y=[df['lowest_low'].iloc[-1]] * len(df),  # Create a straight line for lowest low
            mode='lines',
            name=f'Lowest Low ({reference_period} days)',
            line=dict(color=reference_colors[0], dash='dot'),
        )

        highest_high_trace = go.Scatter(
            x=df['TradingDate'],
            y=[df['highest_high'].iloc[-1]] * len(df),  # Create a straight line for highest high
            mode='lines',
            name=f'Highest High ({reference_period} days)',
            line=dict(color=reference_colors[1], dash='dot'),
        )

        fig.add_trace(lowest_low_trace)
        fig.add_trace(highest_high_trace)

    # Customize the chart appearance
    fig.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
        xaxis_rangeslider_visible=True,
        yaxis2=dict(
            title='Volume',
            overlaying='y',
            side='right',
        ),
        width=figure_size[0] * 100,  # Convert short form to a larger size for better readability
        height=figure_size[1] * 100,
        margin=dict(l=50, r=50, t=70, b=50),  # Adjust margins for space between title and legend
    )

    return fig