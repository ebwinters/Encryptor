switched_int_list = [102, 232, 133, 91, 93, 146]
random_number_list = [3, 7, 2, 9, 2, 1, 0, 4]

final_string = ''
tracker = 0
real_value = None
	# messages = Message.select()
	# instance = messages.where(Message.content.contains(message))
while tracker < len(switched_int_list):
	temp_rand = random_number_list[tracker]
	temp_switched = switched_int_list[tracker]
	real_value = None

	if temp_rand == 0:
		temp_switched = temp_switched + 2
	if temp_rand == 1:
		temp_switched = temp_switched - 3
	if temp_rand == 2:
		temp_switched = int(temp_switched / 10)
	if temp_rand == 3:
		temp_switched = int(temp_switched / 6)
	if temp_rand == 4:
		temp_switched = temp_switched - 9
	if temp_rand == 5:
		temp_switched = temp_switched + 5
	if temp_rand == 6:
		temp_switched = int(temp_switched / 3)
	if temp_rand == 7:
		temp_switched = temp_switched - 8
	if temp_rand == 8:
		temp_switched = temp_switched + 0
	if temp_rand == 9:
		temp_switched = temp_switched + 10


	real_value = chr(temp_switched)
	final_string = final_string + real_value

	tracker = tracker + 1

print("The message reads as follows: ")
print(final_string)
	