def binary_search_recursive(numbers_list, number_to_find, left_index, right_index, indexs=[]):
   if right_index < left_index:
       return -1
   
   med_index = (left_index + right_index)//2
   if med_index >= len(numbers_list) or med_index < 0:
       return -1
   
   med_element = numbers_list[med_index]
   
   if number_to_find < med_element:
      right_index = med_index -1
      
    
   elif number_to_find > med_element:
       left_index = med_index + 1
       
   else:
       numbers_list.pop(med_index)
       left_index = 0
       right_index = len(numbers_list) -1
       indexs.append(med_index)
       
   binary_search_recursive(numbers_list, number_to_find, left_index, right_index,indexs)
   return indexs

if __name__ == '__main__':
    numbers_list = [15, 15,17, 17,19, 21,21]
    number_to_find = 19

    index = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list)-1)
    print(f"Number found at index {index} using binary search")