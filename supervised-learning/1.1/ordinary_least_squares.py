from sklearn import linear_model

reg = linear_model.LinearRegression()
print("reg.fit([[0,0],[1,1],[2,2]],[0,1,2])): \n",\
      reg.fit([[0,0],[1,1],[2,2]],[0,1,2]))

print("reg.coef_: \n", reg.coef_)

print(f"reg.intercept_: \n {reg.intercept_:.2f}")