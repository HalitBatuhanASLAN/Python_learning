def func_direct():
	print("Function direct")
def func_imported():
	print("Function imported")


#by following when we run directly this file it does whatecer in if scope
#if it is called from another file as a module it does whatever in else scope
if __name__ == '__main__':
	func_direct()
else:
	func_imported()
