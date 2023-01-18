def grades(grad):
    result = ""
    if 2. <= grad < 3.:
        result = "Fail"
    elif 3. <= grad < 3.5:
        result = "Poor"
    elif 3.5 <= grad < 4.5:
        result = "Good"
    elif 4. <= grad < 5.5:
        result = "Very Good"
    else:
        result = "Excellent"
    return result

score = float(input())
print(grades(score))