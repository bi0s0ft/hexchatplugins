import hexchat

__module_name__ = ">greentext"
__module_version__ = "1.0.0.0"
__module_description__ = "adds 4chan style greentext to hexchat"



def greentext(word, word_eol, userdata):
	text = word_eol[0]

	if text.find(">") > -1:
		if word_eol[0].index(">") == 0:
			text = word_eol[0].replace(">", "\00303>")
	
	hexchat.command(" ".join(["msg", hexchat.get_info("channel"), text]))
	return hexchat.EAT_ALL


hexchat.hook_command("", greentext)
