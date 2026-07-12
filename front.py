from cProfile import label
from re import sub

import streamlit as st
import requests
st.set_page_config(page_title="Car Insurance Fraud Dectector",layout="wide")
st.title("Insurance Fraud Prediction System")
st.write("Enter the claim details below to check the probability of fraud")
with st.form("Prediction form"):
    st.subheader("Claim details:")
    col1,col2,col3=st.columns(3)
    with col1:
        month=st.selectbox("Month",["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
        week_of_month = st.number_input("Week Of Month", min_value=1, max_value=5, value=1)
        day_of_week = st.selectbox("Day Of Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        make = st.selectbox("Make", ["Honda", "Toyota", "Ford", "Chevrolet", "Pontiac", "Accura", "Dodge", "Mercury", "Jaguar", "Nisson", "VW", "Saab", "Saturn", "Porche", "BMW", "Mecedes", "Ferrari", "Lexus"])
        accident_area = st.selectbox("Accident Area", ["Urban", "Rural"])
        day_of_week_claimed = st.selectbox("Day Of Week Claimed", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        month_claimed = st.selectbox("Month Claimed", ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
        week_of_month_claimed = st.number_input("Week Of Month Claimed", min_value=1, max_value=5, value=1)
        sex = st.selectbox("Sex", ["Male", "Female"])
        marital_status = st.selectbox("Marital Status", ["Single", "Married", "Widow", "Divorced"])

    with col2:
        age = st.number_input("Age", min_value=0, max_value=100, value=35)
        fault = st.selectbox("Fault", ["Policy Holder", "Third Party"])
        policy_type = st.selectbox("Policy Type", ["Sedan - All Perils", "Sedan - Collision", "Sedan - Liability", "Sport - Collision", "Sport - All Perils", "Sport - Liability", "Utility - All Perils", "Utility - Collision", "Utility - Liability"])
        vehicle_category = st.selectbox("Vehicle Category", ["Sedan", "Sport", "Utility"])
        vehicle_price = st.selectbox("Vehicle Price", ["less than 20000", "20000 to 29000", "30000 to 39000", "40000 to 59000", "60000 to 69000", "more than 69000"])
        rep_number = st.number_input("Rep Number", min_value=1, max_value=16, value=1)
        deductible = st.number_input("Deductible", min_value=300, step=100, value=400)
        driver_rating = st.number_input("Driver Rating", min_value=1, max_value=4, value=1)
        days_policy_accident = st.selectbox("Days Policy Accident", ["none", "1 to 7", "8 to 15", "16 to 30", "more than 30"])
        days_policy_claim = st.selectbox("Days Policy Claim", ["8 to 15", "16 to 30", "more than 30"])

    with col3:
        past_number_of_claims = st.selectbox("Past Number Of Claims", ["none", "1", "2 to 4", "more than 4"])
        age_of_vehicle = st.selectbox("Age Of Vehicle", ["new", "2 years", "3 years", "4 years", "5 years", "6 years", "7 years", "more than 7"])
        age_of_policy_holder = st.selectbox("Age Of Policy Holder", ["16 to 17", "18 to 20", "21 to 25", "26 to 30", "31 to 35", "36 to 40", "41 to 50", "51 to 65", "over 65"])
        police_report_filed = st.selectbox("Police Report Filed", ["No", "Yes"])
        witness_present = st.selectbox("Witness Present", ["No", "Yes"])
        agent_type = st.selectbox("Agent Type", ["External", "Internal"])
        number_of_suppliments = st.selectbox("Number Of Suppliments", ["none", "1 to 2", "3 to 5", "more than 5"])
        address_change_claim = st.selectbox("Address Change Claim", ["no change", "under 6 months", "1 year", "2 to 3 years", "4 to 8 years"])
        number_of_cars = st.selectbox("Number Of Cars", ["1 vehicle", "2 vehicles", "3 to 4", "5 to 8", "more than 8"])
        year = st.number_input("Year", min_value=1990, max_value=2026, value=1994)
        base_policy = st.selectbox("Base Policy", ["All Perils", "Collision", "Liability"])
    submitted=st.form_submit_button("Predict Fraud")

if submitted:
    payload={
        "Month": month, "WeekOfMonth": week_of_month, "DayOfWeek": day_of_week, "Make": make,
        "AccidentArea": accident_area, "DayOfWeekClaimed": day_of_week_claimed, "MonthClaimed": month_claimed,
        "WeekOfMonthClaimed": week_of_month_claimed, "Sex": sex, "MaritalStatus": marital_status,
        "Age": age, "Fault": fault, "PolicyType": policy_type, "VehicleCategory": vehicle_category,
        "VehiclePrice": vehicle_price, "RepNumber": rep_number, "Deductible": deductible,
        "DriverRating": driver_rating, "Days_Policy_Accident": days_policy_accident,
        "Days_Policy_Claim": days_policy_claim, "PastNumberOfClaims": past_number_of_claims,
        "AgeOfVehicle": age_of_vehicle, "AgeOfPolicyHolder": age_of_policy_holder,
        "PoliceReportFiled": police_report_filed, "WitnessPresent": witness_present,
        "AgentType": agent_type, "NumberOfSuppliments": number_of_suppliments,
        "AddressChange_Claim": address_change_claim, "NumberOfCars": number_of_cars,
        "Year": year, "BasePolicy": base_policy
    }
    try:
        response=requests.post("http://127.0.0.1:8000/predict",json=payload)
        if response.status_code==200:
            result=response.json()
            st.markdown("---")
            if result["prediction"]=="Fraud":
                st.error("ALERT:High Fraud probability dectected")
            else:
                st.success("Claim looks legitimate")

            st.metric(label="Fraud Probability",value=f"{result['fraud_probability']}")
        else:
            st.error(f"Error from API:{response.text}")
    except requests.exceptions.ConnectionError:
        st.error("Couldn't connect to backend API.Make sure you are connected to internet")

