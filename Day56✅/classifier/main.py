import numpy as np
from sklearn.linear_model import LogisticRegression

X = np.array([[20],[35],[36],[45],[64],[99]])
y = np.array([0,0,1,1,1,1])

model = LogisticRegression()
model.fit(X,y)

while True:
    user_say = input("\n Enter the marks: ")
    
    if user_say.lower() == 'quit':
        break
    try:
        marks = int(user_say)
        new_data = np.array([[marks]])
        result = model.predict(new_data)
        if result[0] == 1:
            print(f"{marks} marks → ✅ Pass\n")
        else:
            print(f"{marks} marks → ❌ Fail\n")      
    except ValueError:
        print("⚠️ Please enter a valid number or 'quit' to exit.\n")