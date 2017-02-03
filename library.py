def generate_name_invite(invite):
	final_position = len(invite)
	initial_position = final_position - 4
	part1 = invite[0:4]
	part2 = invite[initial_position:final_position]
	print('Enviando convite para %s %s' % (part1, part2))
