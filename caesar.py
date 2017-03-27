

def encrypt(text,rot):
	encrypted = ''

	for char in text:
		encrypted+= rotate_character(char,rot)
	return encrypted


def rotate_character(char,rot):
	alphabet1='abcdefghijklmnopqrstuvwxyz'
	alphabet2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	if char in alphabet1:
		char_idx = alphabet1.find(char)
		char_idx=int(char_idx)

		rot_idx=(char_idx+rot) % 26

		return alphabet1[rot_idx]

	if char in alphabet2:
		char_idx = alphabet2.find(char)
		char_idx=int(char_idx)

		rot_idx=(char_idx+rot) % 26

		return alphabet2[rot_idx]
	else:
		return char
