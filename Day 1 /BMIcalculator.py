height = float(input('enter height in meters'))
weight = float(input('enter height in kg'))
BMI = weight/(height**2)
print('BMI = ',round(BMI,2))
if BMI < 18.5:
    print('category : underweight')
elif  BMI<25:
    print('category: normal weight')
elif BMI<30:
    print('category : overweight')
else:
    print('category : obese')        
