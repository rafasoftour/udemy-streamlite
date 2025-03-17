import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def charts():
    st.title("Charts")
    file = st.file_uploader("Load csv", type=["csv"])
    if file is not None:
        df = pd.read_csv(file)
        st.subheader("Car count by color")
        plt.figure()
        color_count = df["color"].value_counts()
        color_count.plot(kind="bar", color="green")
       
        plt.title("Card count by color")
        plt.xlabel("Color")
        plt.xticks(rotation=70)
        plt.ylabel("Number of cars")
        st.pyplot(plt)

        st.subheader("Count by models")
        plt.figure()
        df_filtered = df[(df["year"] >= 2000) & (df["year"] <= 2013)]
        year_counts = df_filtered["year"].value_counts().sort_index()
        year_counts.plot(kind="bar", color="lightblue")
        plt.title("Count of cars models by year (2000 - 2013)")
        plt.xlabel("Year")
        plt.ylabel("Number of cars")
        plt.xticks(rotation=45)
        st.pyplot(plt)

        st.subheader("Pie")
        plt.figure()
        car = st.selectbox("Choose a car", sorted(df["car"].unique()))
        df_filter = df[df["car"] == car]
        model_counts = df_filter["model"].value_counts()
        model_counts.plot(kind="pie", autopct="%d%%", startangle= 80, colors=plt.cm.Paired.colors)
        plt.title(f"Distribution of models for the Brand {car}")
        plt.ylabel("")
        st.pyplot(plt)