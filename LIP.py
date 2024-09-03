import streamlit as st
import numpy as np

# Custom CSS for styling
st.markdown(
    """
    <style>
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #FF4500; /* Bright orange color */
        text-align: center;
        padding: 10px;
    }
    .result {
        font-size: 30px;
        color: #00FFFF; /* Neon blue color */
        font-weight: bold;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the app
st.markdown("<h1 class='title'>Whole Life Insurance Premium Calculator</h1>", unsafe_allow_html=True)

# Input fields
age = st.number_input("Enter the Age of the Policyholder", min_value=14, max_value=99, value=30)
sum_assured = st.number_input("Enter the Sum Assured (in ₹)", min_value=0, value=1_000_000)
interest_rate = st.number_input("Enter the Market Interest Rate (in %)", min_value=0.0, value=4.0) / 100

# Mortality rates
mortality_rates = {
    14: 0.000713,
    15: 0.000770,
    16: 0.000828,
    17: 0.000885,
    18: 0.000919,
    19: 0.000961,
    20: 0.000999,
    21: 0.001033,
    22: 0.001063,
    23: 0.001090,
    24: 0.001113,
    25: 0.001132,
    26: 0.001147,
    27: 0.001159,
    28: 0.001166,
    29: 0.001170,
    30: 0.001170,
    31: 0.001171,
    32: 0.001201,
    33: 0.001246,
    34: 0.001308,
    35: 0.001387,
    36: 0.001482,
    37: 0.001593,
    38: 0.001721,
    39: 0.001865,
    40: 0.002053,
    41: 0.002247,
    42: 0.002418,
    43: 0.002602,
    44: 0.002832,
    45: 0.003110,
    46: 0.003438,
    47: 0.003816,
    48: 0.004243,
    49: 0.004719,
    50: 0.005244,
    51: 0.005819,
    52: 0.006443,
    53: 0.007116,
    54: 0.007839,
    55: 0.008611,
    56: 0.009433,
    57: 0.010294,
    58: 0.011025,
    59: 0.011951,
    60: 0.013073,
    61: 0.014594,
    62: 0.015904,
    63: 0.017612,
    64: 0.019516,
    65: 0.021615,
    66: 0.022724,
    67: 0.025617,
    68: 0.028823,
    69: 0.032372,
    70: 0.036294,
    71: 0.040623,
    72: 0.045392,
    73: 0.050639,
    74: 0.056404,
    75: 0.062728,
    76: 0.069655,
    77: 0.077231,
    78: 0.085502,
    79: 0.094519,
    80: 0.104331,
    81: 0.114992,
    82: 0.126553,
    83: 0.139067,
    84: 0.151077,
    85: 0.162298,
    86: 0.174149,
    87: 0.186638,
    88: 0.199775,
    89: 0.213560,
    90: 0.227995,
    91: 0.243072,
    92: 0.258782,
    93: 0.275109,
    94: 0.292031,
    95: 0.309522,
    96: 0.327549,
    97: 0.346073,
    98: 0.365052,
    99: 0.384436
}

# Calculate the discount factor
v = 1 / (1 + interest_rate)

# Calculate EPV of Outgo (for whole life policy, sum over all ages until the last age)
epv_outgo = 0
for t in range(99 - age + 1):
    current_age = age + t
    if current_age in mortality_rates:
        qx = mortality_rates[current_age]
        survival_probability = np.prod([1 - mortality_rates[age + j] for j in range(t)])
        epv_outgo += v**(t + 1) * qx * survival_probability * sum_assured

# Calculate EPV of Income (for whole life policy, sum over all ages until the last age)
epv_income = 0
for t in range(99 - age + 1):
    survival_probability = np.prod([1 - mortality_rates[age + j] for j in range(t)])
    epv_income += v**t * survival_probability

# Calculate the annual premium
annual_premium = epv_outgo / epv_income

# Display the result
st.markdown(f"<p class='result'>The calculated annual premium for the whole life policy is: ₹{annual_premium:.2f}</p>", unsafe_allow_html=True)
