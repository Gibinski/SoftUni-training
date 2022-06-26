price_ratings =  list(map(int, input().split(", ")))
entry_points = int(input())
left = [price_ratings[i] for i in range(len(price_ratings)) if i < entry_points]
rigtht = [price_ratings[i] for i in range(len(price_ratings)) if i > entry_points]
type_of_items = input()
position = ""
sum_of_price_ratings = 0
sum_left = 0
sum_right = 0
if type_of_items == "cheap":
    sum_left = sum([e for e in left if e < price_ratings[entry_points]]) 
    sum_right = sum([e for e in rigtht if e < price_ratings[entry_points]])        
elif type_of_items == "expensive":
    sum_left = sum([e for e in left if e >= price_ratings[entry_points]]) 
    sum_right = sum([e for e in rigtht if e >= price_ratings[entry_points]])    

if sum_left < sum_right:
    sum_of_price_ratings = sum_right
    position = "Right"
else:
    sum_of_price_ratings = sum_left
    position = "Left"

print(f"{position} - {sum_of_price_ratings}")