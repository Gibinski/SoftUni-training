# Not 
data_array = input().split()
command = input()

while command != "3:1":
    command = command.split()
    start_index = int(command[1])
    end_index = int(command[2])
    command = command[0]
    new_data = []
    new_element = ""
    if end_index >= len(data_array):
        end_index = len(data_array) - 1
    if command == 'merge':
        for i in range(len(data_array)):
            if i < start_index or i > end_index:
                new_data.append(data_array[i])
            else:
                new_element += data_array[i]
                if i == end_index:
                    new_data.append(new_element)
        else:
            data_array = new_data.copy() 
    else:
        if start_index >= len(data_array):
            start_index = len(data_array) - 1
        if end_index >= len(data_array[start_index]):
            end_index = len(data_array[start_index]) - 1
        for i in range(len(data_array)):
            if i < start_index or i > end_index:
                new_data.append(data_array[i])
            else:
                count = len(data_array[start_index]) // end_index
                extra_ch = count + (len(data_array[start_index]) % end_index) 
                for ch in range(len(data_array[start_index])):
                    new_element += data_array[start_index][ch]
                    if len(data_array[start_index]) - ch < extra_ch:
                        continue    
                    if (ch + 1) % count == 0:
                        new_data.append(new_element)
                        new_element = ""
                else:
                    new_data.append(new_element)
        else:
            data_array = new_data.copy() 
    command = input()                       
print(" ".join(data_array))