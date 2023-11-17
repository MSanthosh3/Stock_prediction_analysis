import tkinter as Tkinter
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor


dataset_name = "Stock_Data"

def predict_stock():
    dataset = pd.read_csv("C:/Users/LENOVO/Downloads/Stock_Data.csv")
    
    x = dataset[['Open', 'High', 'Low']].values
    y = dataset['Close'].values
    
    regressor = RandomForestRegressor(n_estimators=10, random_state=0)
    regressor.fit(x, y)
    
    x_value = float(S_open.get())
    y_value = float(S_High.get())
    z_value = float(S_Low.get())

    
    input_data = np.array([[x_value, y_value, z_value]])
    
    y_pred = regressor.predict(input_data)
    
    prediction.config(text=f"Predicted Closing Price: {y_pred[0]:.2f}")

window = Tkinter.Tk()
window.title("Stock Predictive Analysis")
window.geometry("800x500")
window.configure(bg="black")

label1 = Tkinter.Label(window, text="Stock Predictive Analysis", font=("times new roman", 22, "bold"),bg="black", fg="white")
label1.place(x=240, y=30)

dataset_label = Tkinter.Label(window, text="Dataset: ", font=("times new roman", 18, "italic"),bg="black", fg="white")
dataset_label.place(x=290, y=80)

dataset_label.config(text=f"Dataset: {dataset_name}")

S_open_label = Tkinter.Label(window, text="Open: ", font=("times new roman", 22, "italic"),bg="black", fg="white")
S_open_label.place(x=80, y=190)
S_High_label = Tkinter.Label(window, text="High: ", font=("times new roman", 22, "italic"),bg="black", fg="white")
S_High_label.place(x=280, y=190)
S_Low_label = Tkinter.Label(window, text="Low: ", font=("times new roman", 22, "italic"),bg="black", fg="white")
S_Low_label.place(x=500, y=190)


S_open = Tkinter.Entry(window, width=10)
S_open.place(x=180, y=200)
S_High = Tkinter.Entry(window, width=10)
S_High.place(x=380, y=200)
S_Low = Tkinter.Entry(window, width=10)
S_Low.place(x=580, y=200)


predict_button = Tkinter.Button(window, text="Predict", command=predict_stock, font=("times new roman", 20, "italic"), bg="black", fg="white")
predict_button.place(x=320, y=400)


prediction = Tkinter.Label(window, text="Predicted Closing Price: ", font=("times new roman", 18, "italic"),bg="black", fg="white")
prediction.place(x=150, y=300)

window.mainloop()
