import streamlit as st
import pandas as pd

st.set_page_config(page_title="NourishHer AI", page_icon="🍲", layout="wide")
st.title("NourishHer AI")
st.caption("Team HerSphere | Budget-Aware Nutrition for College Women")

meals = [
    ["Moong Dal Khichdi","Veg",40,12,350,20,"Basic","Moong Dal","Masoor Dal Khichdi",35],
    ["Poha","Veg",25,6,250,10,"Basic","Poha","Upma",20],
    ["Sprouts Chat","Vegan",20,9,200,5,"No Cooking","Sprouts","Peanuts",15],
    ["Quinoa Salad","Vegan",150,14,320,20,"Full Kitchen","Quinoa","Dal Salad",40],
    ["Boiled Eggs + Toast","Non-Veg",45,14,300,10,"Basic","Eggs","Soya Toast",30],
    ["Curd Rice","Veg",30,7,300,5,"No Cooking","Curd","Buttermilk Rice",20],
    ["Chicken Bowl","Non-Veg",120,22,500,20,"Basic","Chicken","Egg Bowl",50],
    ["Besan Chilla","Vegan",25,9,220,15,"Basic","Besan","Sooji Chilla",20],
    ["Oats","Vegan",30,8,280,10,"Basic","Oats","Poha",25],
    ["Banana + Milk","Veg",30,8,300,2,"No Cooking","Banana","Apple",25],
]
df = pd.DataFrame(meals, columns=["meal","category","price","protein","cal","time","facility","main","alt","alt_price"])

with st.sidebar:
    budget
