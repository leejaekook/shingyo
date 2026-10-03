#imple Linear Regression) 기본 개념
#
# Y = beta0 + beta1 * X + epsilon
#
# beta1 : 기울기 계수
#         X가 1단위 증가할 때 Y가 평균적으로 얼마나 변화하는지
#
# beta0 : y절편 계수
#         X가 0일 때의 Y값
#
# epsilon : 오차항(error term)
#
# 실제 데이터에서 추정한 계수는
# beta0_hat, beta1_hat 처럼 모자(hat)를 붙여 표현합니다.
#
# 따라서 예측식은
# Y_hat = beta0_hat + beta1_hat * X
#
# 아래 예제는 공부시간(X)으로 시험점수(Y)를 예측합니다.

import numpy as np
from sklearn.linear_model import LinearRegression

# 예제 데이터
# X = 공부시간, Y = 시험점수
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
Y = np.array([55, 60, 65, 70, 75])

# 선형회귀 모델 생성 및 학습
model = LinearRegression()
model.fit(X, Y)

# 추정된 계수
beta0_hat = model.intercept_
beta1_hat = model.coef_[0]

print("=== 단순 선형 회귀 ===")
print(f"추정된 절편(beta0_hat): {beta0_hat:.2f}")
print(f"추정된 기울기(beta1_hat): {beta1_hat:.2f}")

# 회귀식 출력
print(f"\n회귀식: Y_hat = {beta0_hat:.2f} + {beta1_hat:.2f}X")

# 새로운 공부시간에 대한 예측
study_hours = np.array([[6]])
prediction = model.predict(study_hours)[0]

print(f"\n공부시간 {study_hours[0, 0]}시간일 때 예상 시험점수: {prediction:.2f}점")

# 여러 값 예측
print("\n=== 예측 결과 ===")
for hours in [1, 2, 3, 4, 5, 6]:
    score = model.predict([[hours]])[0]
    print(f"공부시간 {hours}시간 -> 예상 점수 {score:.2f}점")

