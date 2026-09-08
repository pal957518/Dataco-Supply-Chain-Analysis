import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import joblib
from pathlib import Path

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Dataco-Smart-Supply-Chain",
    page_icon="🚚",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.block-container {
    padding-top: 3rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

[data-testid="stAppViewContainer"] {
    overflow: visible;
}

[data-testid="stHeader"] {
    background: transparent;
}

.dashboard-title {
    font-size: 32px;
    font-weight: 800;
    line-height: 1.3;
    margin-top: 0px;
    margin-bottom: 5px;
    padding-top: 5px;
    overflow: visible;
    color: white;
}

.dashboard-subtitle {
    color: #9ca3af;
    font-size: 15px;
    line-height: 1.5;
    margin-bottom: 25px;
}

.kpi-card {
    background: #ffffff;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.05);
}

.kpi-title {
    color: #6b7280;
    font-size: 14px;
    font-weight: 600;
}

.kpi-value {
    color: #111827 !important;
    font-size: 28px;
    font-weight: 800;
    margin-top: 8px;
}

.prediction-box {
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #e5e7eb;
    background: white;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# FILE PATHS
# =========================================================
BASE_DIR = Path(__file__).resolve().parent

CSV_PATH = BASE_DIR / "Supply_Chain_Clean.csv"
MODEL_PATH = BASE_DIR / "Supply_Chain_Model.pkl"

# =========================================================
# LOAD DATA
# =========================================================
@st.cache_data
def load_data():
    if not CSV_PATH.exists():
        st.error(f"CSV file not found: {CSV_PATH}")
        st.stop()

    df = pd.read_csv(CSV_PATH)

    df["order date (DateOrders)"] = pd.to_datetime(
        df["order date (DateOrders)"],
        errors="coerce"
    )

    df["shipping date (DateOrders)"] = pd.to_datetime(
        df["shipping date (DateOrders)"],
        errors="coerce"
    )

    return df

df = load_data()

# =========================================================
# LOAD ML MODEL
# =========================================================
model = None

if MODEL_PATH.exists():
    try:
        model = joblib.load(MODEL_PATH)
    except Exception as e:
        st.error(
            "❌ Supply_Chain_Model.pkl was found, but it could not be loaded.\n\n"
            f"Error: {e}"
        )
else:
    st.error(
        "❌ Supply_Chain_Model.pkl was not found.\n\n"
        f"Put this file in the same folder as app.py:\n{MODEL_PATH}"
    )

# =========================================================
# HEADER
# =========================================================
st.markdown(
    """
    <div class="dashboard-title">
        🚚 DATACO-SMART-SUPPLY-CHAIN
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="dashboard-subtitle">
        Interactive Supply Chain Performance Dashboard
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SIDEBAR FILTERS
# =========================================================
st.sidebar.title("🔎 Dashboard Filters")

years = sorted(df["Order_Year"].dropna().unique())
selected_year = st.sidebar.multiselect(
    "Order Year",
    years,
    default=years
)

markets = sorted(df["Market"].dropna().unique())
selected_market = st.sidebar.multiselect(
    "Market",
    markets,
    default=markets
)

segments = sorted(df["Customer Segment"].dropna().unique())
selected_segment = st.sidebar.multiselect(
    "Customer Segment",
    segments,
    default=segments
)

categories = sorted(df["Category Name"].dropna().unique())
selected_category = st.sidebar.multiselect(
    "Category",
    categories,
    default=categories
)

shipping_modes = sorted(df["Shipping Mode"].dropna().unique())
selected_shipping = st.sidebar.multiselect(
    "Shipping Mode",
    shipping_modes,
    default=shipping_modes
)

# =========================================================
# APPLY FILTERS
# =========================================================
filtered_df = df[
    df["Order_Year"].isin(selected_year) &
    df["Market"].isin(selected_market) &
    df["Customer Segment"].isin(selected_segment) &
    df["Category Name"].isin(selected_category) &
    df["Shipping Mode"].isin(selected_shipping)
].copy()

# =========================================================
# KPI CALCULATIONS
# =========================================================
total_sales = filtered_df["Sales"].sum()
total_orders = len(filtered_df)
total_profit = filtered_df["Order Profit Per Order"].sum()
total_quantity = filtered_df["Order Item Quantity"].sum()

if len(filtered_df) > 0:
    late_delivery = filtered_df["Late_delivery_risk"].mean() * 100
else:
    late_delivery = 0

# =========================================================
# KPI CARDS
# =========================================================
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">💰 TOTAL SALES</div>
            <div class="kpi-value">₹{total_sales:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">📦 TOTAL ORDERS</div>
            <div class="kpi-value">{total_orders:,}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">💵 TOTAL PROFIT</div>
            <div class="kpi-value">₹{total_profit:,.0f}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">📊 TOTAL QUANTITY</div>
            <div class="kpi-value">{total_quantity:,}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col5:
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-title">🚚 LATE DELIVERY</div>
            <div class="kpi-value">{late_delivery:.2f}%</div>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# LATE DELIVERY PREDICTION
# =========================================================
st.markdown("---")
st.header("🤖 Late Delivery Prediction")

st.write(
    "Enter the 16 model input values and click the button to predict "
    "whether the order will be late."
)

if model is not None:

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        input_1 = st.number_input("Shipping Mode", value=3.0)
        input_2 = st.number_input("Customer Segment", value=0.0)
        input_3 = st.number_input("Market", value=3.0)
        input_4 = st.number_input("Order Region", value=13.0)

    with col2:
        input_5 = st.number_input("Category Name", value=17.0)
        input_6 = st.number_input("Department Name", value=3.0)
        input_7 = st.number_input("Order Item Quantity", value=1.0)
        input_8 = st.number_input("Sales", value=399.980011)

    with col3:
        input_9 = st.number_input("Order Item Discount", value=16.0)
        input_10 = st.number_input("Order Item Discount Rate", value=0.04)
        input_11 = st.number_input("Product Price", value=399.980011)
        input_12 = st.number_input("Order Profit Per Order", value=168.949997)

    with col4:
        input_13 = st.number_input("Days for shipment (scheduled)", value=4.0)
        input_14 = st.number_input("Order_Year", value=2016.0)
        input_15 = st.number_input("Order_Month", value=1.0)
        input_16 = st.number_input("Order_Weekday", value=5.0)

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🔮 PREDICT LATE DELIVERY", type="primary"):

        try:
            # EXACT 16 INPUT VALUES
            a = np.array([
                input_1,
                input_2,
                input_3,
                input_4,
                input_5,
                input_6,
                input_7,
                input_8,
                input_9,
                input_10,
                input_11,
                input_12,
                input_13,
                input_14,
                input_15,
                input_16
            ])

            # Convert to 2D array
            a = a.reshape(1, -1)

            # Prediction
            pred = model.predict(a)

            prediction = int(pred[0])

            if prediction == 1:
                st.error("🚚 LATE DELIVERY")
                st.warning(
                    "The model predicts that this order is likely to have "
                    "a late delivery."
                )

            elif prediction == 0:
                st.success("✅ NOT LATE DELIVERY")
                st.info(
                    "The model predicts that this order is not likely to "
                    "have a late delivery."
                )

            else:
                st.warning(f"Model returned an unexpected value: {prediction}")

        except Exception as e:
            st.error(
                "❌ Prediction failed.\n\n"
                f"Error: {e}"
            )

else:
    st.warning(
        "⚠️ Prediction is disabled because Supply_Chain_Model.pkl "
        "could not be loaded."
    )

# =========================================================
# ROW 1 — SALES TREND + MARKET
# =========================================================
col1, col2 = st.columns(2)

with col1:
    monthly_sales = (
        filtered_df
        .groupby(["Order_Year", "Order_Month"])["Sales"]
        .sum()
        .reset_index()
    )

    if not monthly_sales.empty:
        monthly_sales["Date"] = pd.to_datetime(
            monthly_sales["Order_Year"].astype(str)
            + "-"
            + monthly_sales["Order_Month"].astype(str)
            + "-01"
        )

        fig_sales = px.line(
            monthly_sales,
            x="Date",
            y="Sales",
            markers=True,
            title="📈 Sales Trend"
        )

        fig_sales.update_layout(
            template="plotly_white",
            height=380,
            xaxis_title="",
            yaxis_title="Sales"
        )

        st.plotly_chart(
            fig_sales,
            use_container_width=True
        )

with col2:
    market_sales = (
        filtered_df
        .groupby("Market")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
    )

    fig_market = px.bar(
        market_sales,
        x="Market",
        y="Sales",
        title="🌎 Sales by Market",
        text_auto=".2s"
    )

    fig_market.update_layout(
        template="plotly_white",
        height=380,
        xaxis_title="",
        yaxis_title="Sales"
    )

    st.plotly_chart(
        fig_market,
        use_container_width=True
    )

# =========================================================
# ROW 2 — PROFIT + ORDER STATUS
# =========================================================
col1, col2 = st.columns(2)

with col1:
    category_profit = (
        filtered_df
        .groupby("Category Name")["Order Profit Per Order"]
        .sum()
        .reset_index()
        .sort_values(
            "Order Profit Per Order",
            ascending=False
        )
        .head(10)
    )

    fig_profit = px.bar(
        category_profit,
        x="Order Profit Per Order",
        y="Category Name",
        orientation="h",
        title="💵 Top 10 Categories by Profit",
        text_auto=".2s"
    )

    fig_profit.update_layout(
        template="plotly_white",
        height=420,
        xaxis_title="Profit",
        yaxis_title=""
    )

    st.plotly_chart(
        fig_profit,
        use_container_width=True
    )

with col2:
    status_count = (
        filtered_df["Order Status"]
        .value_counts()
        .reset_index()
    )

    status_count.columns = [
        "Order Status",
        "Orders"
    ]

    fig_status = px.pie(
        status_count,
        names="Order Status",
        values="Orders",
        hole=0.45,
        title="📦 Order Status"
    )

    fig_status.update_layout(
        template="plotly_white",
        height=420
    )

    st.plotly_chart(
        fig_status,
        use_container_width=True
    )

# =========================================================
# ROW 3 — SHIPPING + SEGMENT
# =========================================================
col1, col2 = st.columns(2)

with col1:
    shipping_data = (
        filtered_df
        .groupby("Shipping Mode")
        .agg(
            Orders=("Shipping Mode", "size"),
            Sales=("Sales", "sum")
        )
        .reset_index()
    )

    fig_shipping = px.bar(
        shipping_data,
        x="Shipping Mode",
        y="Orders",
        title="🚚 Orders by Shipping Mode",
        text_auto=True
    )

    fig_shipping.update_layout(
        template="plotly_white",
        height=380
    )

    st.plotly_chart(
        fig_shipping,
        use_container_width=True
    )

with col2:
    segment_data = (
        filtered_df
        .groupby("Customer Segment")["Sales"]
        .sum()
        .reset_index()
    )

    fig_segment = px.pie(
        segment_data,
        names="Customer Segment",
        values="Sales",
        hole=0.45,
        title="👥 Sales by Customer Segment"
    )

    fig_segment.update_layout(
        template="plotly_white",
        height=380
    )

    st.plotly_chart(
        fig_segment,
        use_container_width=True
    )

# =========================================================
# TOP PRODUCTS
# =========================================================
st.subheader("🏆 Top 10 Products")

top_products = (
    filtered_df
    .groupby("Product Name")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Order Profit Per Order", "sum"),
        Quantity=("Order Item Quantity", "sum")
    )
    .reset_index()
    .sort_values("Sales", ascending=False)
    .head(10)
)

st.dataframe(
    top_products,
    use_container_width=True,
    hide_index=True
)

# =========================================================
# DATA TABLE
# =========================================================
st.subheader("📋 Detailed Supply Chain Data")

show_columns = [
    "Order_Year",
    "Market",
    "Customer Segment",
    "Category Name",
    "Product Name",
    "Sales",
    "Order Item Quantity",
    "Order Profit Per Order",
    "Order Status",
    "Shipping Mode",
    "Late_delivery_risk"
]

st.dataframe(
    filtered_df[show_columns].head(1000),
    use_container_width=True,
    hide_index=True
)

# =========================================================
# FOOTER
# =========================================================
st.markdown("---")

st.caption(
    f"Showing {len(filtered_df):,} records from "
    f"{len(df):,} total records"
)
