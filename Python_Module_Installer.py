import os
from tkinter import *
from tkinter import messagebox, filedialog, ttk
import pyperclip
from pip._internal.utils.misc import get_installed_distributions

BACKGROUND_COLOR ="#3282b8"
TITLE_FONT_COLOR ="#f5f5f5"
BUTTON_COLOR_BG ="#111f4d"
BUTTON_COLOR_FG ="#f2f4f7"
TEXT_BOX_COLOR_BG = "#e4f9f5"
TEXT_BOX_COLOR_FG = "#222831"
FONT = ("Courier", 12, "normal")

installed_libraries = get_installed_distributions()
list_installed_packages = [package.project_name for package in installed_libraries]
package_name = 'pyperclip'
if package_name not in list_installed_packages:
	run_cmd = f"pip install {package_name}"
	os.system(run_cmd)
	messagebox.showinfo(title = f"{Package_name} Installed", message =f"{package_name} was not found and was automatically installed.\nRun the program again.")
else:

	def search():
		not_installed_packages = []
		installed_modules =[]
		search_data =  input_list.get(1.0,"end-1c")
		if len(search_data) == 0:
			messagebox.showinfo(title = "Error", message = "The input field is empty.!\nInput the name of the module you want to search")
		else:	

			singled_data_list =  str(search_data).split(",")
			for data in singled_data_list:
				if data.lower() in list_installed_packages:
					installed_modules.append(data)
					input_list.delete(1.0, END)
				else:
					
					not_installed_packages.append(data)
			str1 = "\n".join(installed_modules)
			str2 = "\n".join(not_installed_packages)
			messagebox.showinfo(title = "Already Installed", message =f"The following modules has already been installed \n{str1}")
			messagebox.showinfo(title = "Not Installed", message =f"The following modules are not installed \n{str2}")
			pack_to_install = ",".join(not_installed_packages)
			input_list.insert(1.0,pack_to_install)
		
	def available_packages():

		data_str =""
		for package in installed_libraries:
			name_ver = f"{package.project_name} :v.{package._version}\n"
			data_str += name_ver 
		with open("installed_modules_log.txt",'a') as log_file:
			log_file.truncate(0)
			log_file.write(data_str)
		messagebox.showinfo(title ="Log file created",message = "The installed modules in system is loged into installed_modules_log.txt")


	def install_package():
		install_data = input_list.get(1.0,"end-1c")

		if len(install_data) == 0:
			messagebox.showinfo(title = "Error", message = "The input field is empty.!\nInput the name of the module you want to install")
		else:

			command = str(install_data).split(",")
			
			for cmd in command:
				commands = f'pip install {cmd}'
				print(commands)
				
				os.system(commands)
			messagebox.showinfo(title = "Installation Completed", message = "The given packages have completed instaling")
			input_list.delete(1.0, END)


	def import_from_file():
		file_dir = filedialog.askopenfilename(initialdir = '.')

		try:
			with open(file_dir) as file_data:
				imported_data = file_data.readlines()

		except FileNotFoundError:
			pass

		else:
			
			stripped_data =[]
			for data in imported_data:
				stripped_data.append(data.strip())
			data_to_input = ",".join(stripped_data)
			input_list.delete(1.0,END)
			input_list.insert(1.0, data_to_input)


	def about():
		messagebox.showinfo(title = "About", message = "v.1.6\nCreated by Sahasil \n github.com/SahasilAK")


	window = Tk()
	
	window.config(padx = 50, pady = 40, bg= BACKGROUND_COLOR)
	window.title("Module Installer for Python")

	about_img = PhotoImage(file ="icons/about.png")
	load_img = PhotoImage(file ="icons/load.png")


	
	label_1 = Label(text ="Input Single Module Name")
	label_1.config(pady = 5, fg = TITLE_FONT_COLOR, bg= BACKGROUND_COLOR, font =FONT)
	label_1.grid(row = 1,column = 3, columnspan = 2)

	label_2 = Label(text ="Or")
	label_2.config(pady = 5, fg = TITLE_FONT_COLOR, bg= BACKGROUND_COLOR, font =FONT)
	label_2.grid(row = 2,column =3 ,columnspan = 2)


	label_3 = Label(text ="Input Multiple Module Names Seperated by commas ( , )")
	label_3.config(pady = 5, fg = TITLE_FONT_COLOR, bg= BACKGROUND_COLOR, font =FONT)
	label_3.grid(row = 3,column = 1, columnspan = 6)


	clip_board = pyperclip.paste()

	input_list = Text(height = 4, width = 50)
	input_list.config(fg = TEXT_BOX_COLOR_FG, bg = TEXT_BOX_COLOR_BG, borderwidth=0)
	input_list.insert(1.0,clip_board)
	input_list.focus()

	input_list.grid(row = 4,column = 2, columnspan = 4,pady = 5)

	install_button = Button(text = "Install", command = install_package)
	install_button.config(fg = BUTTON_COLOR_FG, bg= BUTTON_COLOR_BG,width = 10,font = FONT, highlightthickness = 0, borderwidth=0)
	install_button.grid(row = 5,column = 3,pady = 5)

	about_button = Button(image=about_img, command = about)
	about_button.config(highlightthickness = 0, bg= BACKGROUND_COLOR, borderwidth=0)
	about_button.grid(row = 0,column = 7)

	search_button = Button(text = "Search", command = search)
	search_button.config(fg = BUTTON_COLOR_FG, bg= BUTTON_COLOR_BG,width = 10,font = FONT, highlightthickness = 0, borderwidth=0)
	search_button.grid(row = 5,column = 4,pady = 5)

	import_button = Button(image=load_img, command = import_from_file)
	import_button.config(highlightthickness = 0, bg= BACKGROUND_COLOR, borderwidth=0)
	import_button.grid(row = 0,column = 0)

	installed_package_button =  Button(text = "Installed Modules", command = available_packages)
	installed_package_button.config(fg = BUTTON_COLOR_FG, bg= BUTTON_COLOR_BG,width = 20,font = FONT, highlightthickness = 0, borderwidth=0)
	installed_package_button.grid(row = 6,column = 3, columnspan = 2,pady = 5)

	





	window.mainloop()