dic =  {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}
cred_sum = 0
grade_sum = 0
for i in range(20):
    sub,cred,grade = input().split()
    cred = float(cred)
    if grade != 'P':
        if grade in dic:
            cred_sum +=cred
            grade_sum += dic[grade]*cred
if cred_sum == 0:
    print(f"{0:.6f}")
else:
    print(f"{grade_sum / cred_sum:.6f}")