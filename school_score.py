school_score = [
	{'school_class': '4a', 'scores': [3,5,5,5,4]}, 
	{'school_class': '5a', 'scores': [3,4,4,5,2]},
	{'school_class': '6a', 'scores': [3,3,4,5,2]},
	{'school_class': '7a', 'scores': [5,4,4,5,3]},
	{'school_class': '8a', 'scores': [3,4,3,5,2]}
]

s = 0;
length_list = 0;

for list_element in school_score:
	score = list_element.get('scores')
	sum_class = sum(score)
	len_class = len(score)

	s += sum_class
	length_list += len_class 

average_score = s/length_list

print (average_score)