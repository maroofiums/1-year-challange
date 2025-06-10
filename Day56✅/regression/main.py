from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[20],[25],[30],[35],[40]])
y = np.array([100,150,200,250,300])

model = LinearRegression()
model.fit(X,y)
while True:
    user_say = input("Enter The temprature in (°C): ")
    if user_say.lower() == "quit":
        break
    try:
        temp = int(user_say)
        new_temp = np.array([[temp]])
        predicted_sale = model.predict(new_temp)
        print(f"{temp}°C par predicted ice-cream sale: {predicted_sale[0]:.2f} thousand")
    except ValueError:
        print("Please Enter a valid input or 'quit' to exit. \n")