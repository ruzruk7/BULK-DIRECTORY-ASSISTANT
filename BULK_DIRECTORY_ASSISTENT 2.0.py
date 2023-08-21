import shutil, os
file_mode = False
folder_mode = False
#PATH FORMATYER
def path_formatter(path):
    splitted_orig = path.split('\\')
    format = '\\'.join(splitted_orig)
    formatted = format.strip('\"')
    return formatted

while True:
    print('Welcome To BULK FILE/FOLDER ASSISTENT\nEnter: Q to quit\nEnter: M for main menu\n-------------------------------------------MENU-------------------------------------------')
    type_selecter = input('\nWhat would you like to work with?\nFiles enter: FIL\tFolders enter: FOL\n\nYou can always switch by returning to the main menu\nEntered: ').lower()
    if type_selecter == 'q'.lower():
        x = input('\nAre you sure you want to Quit? Y/N ').lower()
        if x not in ['y', 'n', 'm']:
            pass
        else:
            if x == 'y':
                break
            else:
                continue
    if type_selecter == 'm':
        continue
    if type_selecter == 'fil':
        file_mode = True
    if type_selecter == 'fol':
        folder_mode = True
    
    if file_mode:
        while True:
            print('-------------------------------------------FILE MODE-------------------------------------------')
            mode = input('\nWhat would you like to do with your files?\nRename enter: RENAME\tMove enter: M\tCopy enter: C\tDelete enter: DEL\tMain-Menu enter: MM\nEntered: ').lower()
            if mode =='mm':
                print('Returning to the main menu\n-------------------------------------------------------------------------------------------')
                file_mode = False
                break
            elif mode == 'rename':
                pass # BUILD RENAMER using PyQT 
            elif mode == 'del':
                sec_sub_mode = input('\nWould you like to delete all files or specific files only?\nAll files enter: ALL\tSpecific files enter: SPEC\nEntered: ').lower()
                if sec_sub_mode == 'all':
                    tert_sub_mode = input('\nDelete all files from single or multiple folders?\nSingle Folder: SFOL\tMultiple Folder: MFOL\nEntered: ').lower()
                    if tert_sub_mode =='sfol':
                        # origin
                        file_parent_folder_location = input('\nPlease enter the PATH(case-sensitive) of the folder you wish to clear.\nEntered: ')
                        formatted_orig = path_formatter(file_parent_folder_location)
                        all_files_in_orig = os.listdir(formatted_orig)
                        for files in all_files_in_orig:
                            file_path = (f'{formatted_orig}\\{files}')
                            print(f'DELETING---{files}---FROM---{formatted_orig}') 
                            os.remove(file_path)
                        print('-------------------------------------------DELETING FILES COMPLETE-------------------------------------------')
                        continue
                    elif tert_sub_mode == 'mfol':
                        folder_names = []
                        folder_name = input('\nPlease enter the folder names(case-sensitive) you want cleared(seperated with commas, WITHOUT SPACES.)\nEntered: ')
                        splitter = folder_name.split(',')
                        for split in splitter:
                            folder_names.append(split)
                        # destination
                        file_destination_root_folder = input('\nPlease enter the PATH(case-sensitive) of the parent folder where the folders you want cleared are located\ne.g: User/Desktop/Folders_of_interest  |you would enter: User/Desktop\nEntered: ')
                        print('')
                        formatted_dest = path_formatter(file_destination_root_folder)
                        for folder in folder_names:
                            folder_path = (f'{formatted_dest}\\{folder}')
                            all_files_in_orig = os.listdir(folder_path)
                            for files in all_files_in_orig:
                                file_path = (f'{folder_path}\\{files}')
                                print(f'DELETING---{files}---FROM---{folder_path}') 
                                os.remove(file_path)
                                continue
                        print('-------------------------------------------MULTIPLE FOLDERS CLEARED-------------------------------------------')
                        continue
                elif sec_sub_mode == 'spec':
                    tert_sub_mode = input('\nDelete specific files from single/multiple folders?\nSingle Folder: SFOL\tMultiple Folder: MFOL\nEntered: ').lower()
                    if tert_sub_mode == 'sfol':
                        file_name_types = []
                        file_names = input('\nPlese enter the file names(case-sensitive), if there are multiple file names that are numbered differently (e.g: file_1, file_2...file_300).\nEnter only part of the file name(e.g: \'file_\') seperated by commas WITHOUT spaces.\nEntered: ')
                        splitted = file_names.split(',')
                        for split in splitted:
                            file_name_types.append(split)
                        print(f'File names---{file_name_types}---\n')
                        file_parent_folder_location = input('\nPlease enter file(s) folder PATH(case-sensitive).\nEntered: ')
                        print('')
                        formatted_orig = path_formatter(file_parent_folder_location)
                        all_files_in_orig = os.listdir(formatted_orig)
                        for name in file_name_types:
                            for files in all_files_in_orig:
                                if name in files:
                                    file_path = (f'{formatted_orig}\\{files}')
                                    print(f'DELETING----{files}----FROM---{formatted_orig}')
                                    os.remove(file_path)
                        print('-------------------------------------------SPECIFIED FILES DELETED-------------------------------------------')
                        continue
                    elif tert_sub_mode == 'mfol':
                        folder_names = []
                        folder_name = input('\nPlease enter the folder names(case-sensitive)(seperated with commas, WITHOUT SPACES.)\nEntered: ')
                        splitter_folder = folder_name.split(',')
                        for split in splitter_folder:
                            folder_names.append(split)
    
                        file_names = []
                        file_name = input('\nPlese enter the file names(case-sensitive), if there are multiple file names that are numbered differently (e.g: file_1, file_2...file_300).\nEnter only part of the file name(e.g: \'file_\') seperated by commas WITHOUT spaces.\nEntered: ')
                        splitted = file_name.split(',')
                        for split in splitted:
                            file_names.append(split)
                        print(f'Folders specified---{folder_names}---')
                        print(f'File names---{file_names}---\n')
                        file_destination_root_folder = input('\nPlease enter the PATH of the parent folder containing the folders specified\ne.g: User/Desktop/Folder_of_interest  | you would enter: User/Desktop.\nEntered: ')
                        print('')
                        formatted_dest = path_formatter(file_destination_root_folder)
                        for folder in folder_names:
                            folder_path = (f'{formatted_dest}\\{folder}')
                            all_files_in_orig = os.listdir(folder_path)
                            for name in file_names:
                                for files in all_files_in_orig:
                                    if name in files:
                                        file_path = (f'{folder_path}\\{files}')
                                        print(f'DELETING----{files}----FROM---{folder_path}')
                                        os.remove(file_path)
                        print('-------------------------------------------SPECIFIED FILES DELETED-------------------------------------------')
                        continue
            elif mode == 'm':
                sub_mode = input('\nMove all contents? Enter: \'ALL\'\tMove specified Files? Enter: \'SPEC\'\nEntered: ').lower()
                if sub_mode == 'all':
                    sec_sub_mode = input('\nWould you like to move all files to single/multiple folders?\nSINGLE folder enter: SFOL\tMULTIPLE folders enter: MFOL\nEntered: ').lower()
                    if sec_sub_mode == 'sfol':
                        # origin
                        file_parent_folder_location = input('\nPlease enter file(s) origin folder location as a PATH(case-sensitive).\nEntered: ')
                        print('')
                        formatted_orig = path_formatter(file_parent_folder_location)
                        # destination
                        file_destination = input('\nPlease enter the PATH(case-sensitive) you want your FILES moved to.\nEntered: ')
                        print('')
                        formatted_dest = path_formatter(file_destination)
                        all_files_in_orig = os.listdir(formatted_orig)
                        for files in all_files_in_orig:
                            file_path = (f'{formatted_orig}\\{files}')
                            print(f'MOVING---{files}---TO---{formatted_dest}') 
                            shutil.move(file_path, formatted_dest)
                        print('-------------------------------------------FILE TRANSFER COMPLETE-------------------------------------------')
                        continue
                    elif sec_sub_mode == 'mfol':
                        folder_names = []
                        folder_name = input('\nPlease enter the folder names(case-sensitive)(seperated with commas. NO SPACE)\nEntered: ')
                        splitter = folder_name.split(',')
                        for split in splitter:
                            folder_names.append(split)
                        # origin
                        file_parent_folder_location = input('\nPlease enter file(s) origin folder location as a PATH(case-sensitive).\nEntered: ')
                        print('')
                        formatted_orig = path_formatter(file_parent_folder_location)
                        # destination
                        file_destination_root_folder = input('\nPlease enter the PATH(case-sensitive) of the folders where you want your files moved\ne.g: User/Desktop/Folder_of_interest  | you would enter: User/Desktop.\nEntered: ')
                        print('')
                        formatted_dest = path_formatter(file_destination_root_folder)
                        all_files_in_orig = os.listdir(formatted_orig)
                        for folder in folder_names:
                            folder_path = (f'{formatted_dest}\\{folder}')
                            for files in all_files_in_orig:
                                file_path = (f'{formatted_orig}\\{files}')
                                print(f'MOVING----{files}----FROM---{formatted_orig}\nTO---{folder_path}') 
                                shutil.copy2(file_path, folder_path)
                        for file in all_files_in_orig:
                            file_path = (f'{formatted_orig}\\{file}')
                            os.remove(file_path)
                        print('-------------------------------------------FILE TRANSFER COMPLETE-------------------------------------------')
                        continue
                elif sub_mode == 'spec':
                    sec_sub_mode = input('\nWould you like to move specific files to single/multiple folders?\nSINGLE folder enter: SFOL\tMULTIPLE folders enter: MFOL\nEntered: ').lower()
                    if sec_sub_mode == 'sfol':
                        file_name_types = []
                        file_names = input('\nPlese enter the file names(case-sensitive), if there are multiple file names that are numbered differently (e.g: file_1, file_2...file_300).\nEnter only part of the file name(e.g: \'file_\') seperated by commas WITHOUT spaces.\nEntered: ')
                        splitted = file_names.split(',')
                        for split in splitted:
                            file_name_types.append(split)
                        print(f'File names---{file_name_types}---\n')
                        file_parent_folder_location = input('\nPlease enter file(s) origin folder PATH(case-sensitive).\nEntered: ')
                        print('')
                        formatted_orig = path_formatter(file_parent_folder_location)
                        # destination
                        file_destination = input('\nPlease enter the PATH(case-sensitive) you want your FILES moved to.\nEntered: ')
                        print('')
                        formatted_dest = path_formatter(file_destination)
                        
                        all_files_in_orig = os.listdir(formatted_orig)
                        for name in file_name_types:
                            for files in all_files_in_orig:
                                if name in files:
                                    file_path = (f'{formatted_orig}\\{files}')
                                    print(f'MOVING----{files}----FROM---{formatted_orig}\nTO---{formatted_dest}')
                                    shutil.move(file_path, formatted_dest)
                        print('-------------------------------------------SPECIFIED FILES TRANSFER COMPLETE-------------------------------------------')
                        continue
                    elif sec_sub_mode == 'mfol':
                        folder_names = []
                        folder_name = input('\nPlease enter the folder names(case-sensitive)(seperated with commas, WITHOUT SPACES.)\nEntered: ')
                        splitter_folder = folder_name.split(',')
                        for split in splitter_folder:
                            folder_names.append(split)

                        file_name_types = []
                        file_names = input('\nPlese enter the file names(case-sensitive), if there are multiple file names that are numbered differently (e.g: file_1, file_2...file_300).\nEnter only part of the file name(e.g: \'file_\') seperated by commas WITHOUT spaces.\nEntered: ')
                        splitted = file_names.split(',')
                        for split in splitted:
                            file_name_types.append(split)
                        print(f'Folder names---{folder_names}---')
                        print(f'File names---{file_name_types}---\n')

                        #origin
                        file_parent_folder_location = input('\nPlease enter file(s) original folder PATH(case-sensitive).\nEntered: ')
                        print('')
                        formatted_orig = path_formatter(file_parent_folder_location)
                        # destination
                        file_destination_root_folder = input('\nPlease enter the PATH of the folders where you want your files moved to.\ne.g: User/Desktop/Folder_of_interest  | you would enter: User/Desktop.\nEntered: ')
                        print('')
                        formatted_dest = path_formatter(file_destination_root_folder)

                        all_files_in_orig = os.listdir(formatted_orig)
                        for folder in folder_names:
                            folder_path = (f'{formatted_dest}\\{folder}')
                            for name in file_name_types:
                                for files in all_files_in_orig:
                                    if name in files:
                                        file_path = (f'{formatted_orig}\\{files}')
                                        print(f'MOVING----{files}----FROM---{formatted_orig}\nTO---{folder_path}')
                                        shutil.copy2(file_path, folder_path)
                        for name in file_name_types:
                            for files in all_files_in_orig:
                                if name in files:
                                    file_path = (f'{formatted_orig}\\{files}')
                                    os.remove(file_path)
                        print('-------------------------------------------SPECIFIED FILES TRANSFER COMPLETE-------------------------------------------')
                        continue
            elif mode == 'c':
                sub_mode = input('\nCopy all contents? Enter: \'ALL\'\tCopy specified Files? Enter: \'SPEC\'\nEntered: ').lower()
                if sub_mode == 'all':
                    sec_sub_mode = input('\nWould you like to copy all files to single/multiple folders?\nSINGLE folder enter: SFOL\tMULTIPLE folders enter: MFOL\nEntered: ').lower()
                    if sec_sub_mode == 'sfol':
                        # origin
                        file_parent_folder_location = input('\nPlease enter origin file(s) folder location as a PATH.\nEntered: ')
                        print('')
                        formatted_orig = path_formatter(file_parent_folder_location)
                        # destination
                        file_destination = input('\nPlease enter the PATH(case-sensitive) of the folder you want your FILES moved to.\nEntered: ')
                        print('')
                        formatted_dest = path_formatter(file_destination)
                        all_files_in_orig = os.listdir(formatted_orig)
                        for files in all_files_in_orig:
                            file_path = (f'{formatted_orig}\\{files}')
                            print(f'COPYING---{files}---TO---{formatted_dest}') 
                            shutil.copy2(file_path, formatted_dest)
                        print('-------------------------------------------FILE COPYING COMPLETE-------------------------------------------')
                        continue
                    elif sec_sub_mode == 'mfol':
                        folder_names = []
                        folder_name = input('\nPlease enter the folder names(case-sensitive)(seperated with commas, WITHOUT SPACES.)\nEntered: ')
                        splitter = folder_name.split(',')
                        for split in splitter:
                            folder_names.append(split)
                        # origin
                        file_parent_folder_location = input('\nPlease enter the PATH(case-sensitive) of the folder containing the files of interest\nEntered: ')
                        print('')
                        formatted_orig = path_formatter(file_parent_folder_location)
                        # destination
                        file_destination_root_folder = input('\nPlease enter the PATH(case-sensitive) of the parent folder which contains the folders you want your files moved to.\ne.g: User/Desktop/Folder_of_interest  | you would enter: User/Desktop.\nEntered: ')
                        print('')
                        formatted_dest = path_formatter(file_destination_root_folder)
                        all_files_in_orig = os.listdir(formatted_orig)
                        for folder in folder_names:
                            folder_path = (f'{formatted_dest}\\{folder}')
                            for files in all_files_in_orig:
                                file_path = (f'{formatted_orig}\\{files}')
                                print(f'COPYING----{files}----FROM---{formatted_orig}\nTO---{folder_path}') 
                                shutil.copy2(file_path, folder_path)
                        print('-------------------------------------------FILE COPYING COMPLETE-------------------------------------------')
                        continue
                elif sub_mode == 'spec':
                    sec_sub_mode = input('\nWould you like to move specific files to a single or multiple folders?\nSINGLE folder enter: SFOL\tMULTIPLE folders enter: MFOL\nEntered: ').lower()
                    if sec_sub_mode == 'sfol':
                        file_names = []
                        file_name = input('\nPlease enter the file names(case-sensitive)(seperated with commas, WITHOUT SPACES.)\nEntered: ')
                        splitter = file_name.split(',')
                        for split in splitter:
                            file_names.append(split)
                        print(f'File names you have specified for copying: {file_names}')
                        # origin
                        file_parent_folder_location = input('\nPlease enter original file(s) folder PATH(case-sensitive).\nEntered: ')
                        print('')
                        formatted_orig = path_formatter(file_parent_folder_location)
                        # destination
                        file_destination = input('\nPlease enter the PATH(case-sensitive) of the folder you want your FILES moved to.\nEntered: ')
                        print('')

                        formatted_dest = path_formatter(file_destination)
                        all_files_in_orig = os.listdir(formatted_orig)
                        for files in all_files_in_orig:
                            for name in file_names:
                                if name in files:
                                    file_path = (f'{formatted_orig}\\{files}')
                                    print(f'COPYING---{files}---TO---{formatted_dest}\nFROM---{formatted_orig}') 
                                    shutil.copy2(file_path, formatted_dest)
                        print('-------------------------------------------SPECIFIED FILE COPYING COMPLETE-------------------------------------------')
                        continue
                    elif sec_sub_mode == 'mfol':
                        file_names = []
                        file_name = input('\nPlease enter the file names(case-sensitive)(seperated with commas, WITHOUT SPACES.)\nEntered: ')
                        splitter = file_name.split(',')
                        for split in splitter:
                            file_names.append(split)
                        print(f'FILE NAMES you have specified for copying: {file_names}')
                        folder_names = []
                        folder_name = input('\nPlease enter the folder names(case-sensitive)(seperated with commas, WITHOUT SPACES.)\nEntered: ')
                        splitter = folder_name.split(',')
                        for split in splitter:
                            folder_names.append(split)
                        print(f'FOLDER NAMES you will have your specified files moved to: {folder_names}')
                        # origin
                        file_parent_folder_location = input('\nPlease enter the PATH(case-sensitive) of the folder containing the files of interest.\nEntered: ')
                        print('')
                        formatted_orig = path_formatter(file_parent_folder_location)
                        # destination
                        file_destination_root_folder = input('\nPlease enter the PATH(case-sensitive) of the parent folder which contains the folders you want your specified files copied to.\ne.g: User/Desktop/Folder_of_interest  | you would enter: User/Desktop.\nEntered: ')
                        print('')
                        formatted_dest = path_formatter(file_destination_root_folder)
                        all_files_in_orig = os.listdir(formatted_orig)
                        for folder in folder_names:
                            folder_path = (f'{formatted_dest}\\{folder}')
                            for files in all_files_in_orig:
                                for name in file_names:
                                    if name in files:
                                        file_path = (f'{formatted_orig}\\{files}')
                                        print(f'COPYING---{files}---TO---{folder_path}\nFROM---{formatted_orig}') 
                                        shutil.copy2(file_path, folder_path)   
                        print('-------------------------------------------FILE COPYING COMPLETE-------------------------------------------')
                        continue
    if folder_mode:
        while True:
            print('-------------------------------------------FOLDER MODE-------------------------------------------')
            mode = input('\nWhat would you like to do with your folders?\nRename enter: RENAME\tMove enter: M\tCopy enter: C\tDelete enter: DEL\tMain-Menu enter: MM\nEntered: ').lower()
            if mode =='mm':
                print("Returning to main menu\n-------------------------------------------------------------------------------------------")
                file_mode = False
                break
            elif mode == 'rename':
                pass # BUILD RENAMER using PyQT 
            elif mode == 'del':
                sec_sub_mode = input('\nManage a single folder or multiple/specific folders?\nSingle folders enter: SINGLE\tSpecific folders enter: MULTIPLE\nEntered: ').lower()
                if sec_sub_mode == 'single':
                    tert_sub_mode = input('\nDelete a folder or multiple folders from a directory?\nSingle Folder: SFOL\tMultiple Folder: MFOL\nEntered: ').lower()
                    if tert_sub_mode =='sfol':
                        # origin
                        folder_location = input('\nPlease enter the PATH(case-sensitive) of the folder you want to delete.\nEntered: ')
                        print('')
                        formatted_orig = path_formatter(folder_location)
                        shutil.rmtree(formatted_orig)
                        print('-------------------------------------------FOLDER DELETION COMPLETE-------------------------------------------')
                        continue
                    elif tert_sub_mode == 'mfol':
                        folder_names = []
                        folder_name = input('\nPlease enter the folder names(case-sensitive) you want deleted(seperated with commas, WITHOUT SPACES.)\nEntered: ')
                        splitter = folder_name.split(',')
                        for split in splitter:
                            folder_names.append(split)
                        # destination
                        folder_destination_root_folder = input('\nPlease enter the PATH(case-sensitive) of the parent folder where the folders you want deleted are located\ne.g: User/Desktop/Folders_of_interest  |you would enter: User/Desktop\nEntered: ')
                        print('')
                        formatted_orig = path_formatter(folder_destination_root_folder)
                        all_folders_in_parent_folder = os.listdir(formatted_orig)
                        for name in folder_names:
                            for folder in all_folders_in_parent_folder:
                                if name in folder:
                                    folder_path = {f'{formatted_orig}\\{folder}'}
                        shutil.rmtree(folder_path)
                        print('-------------------------------------------MULTIPLE FOLDERS DELETED-------------------------------------------')
                        continue
                elif sec_sub_mode == 'multiple':
                    tert_sub_mode = input('\nDelete specific folders from single/multiple parent directories?\nSingle directory: SFOL\tMultiple directories: MFOL\nEntered: ').lower()
                    if tert_sub_mode == 'sfol':
                        folder_name_types = []
                        folder_names = input('\nPlese enter the folder names(case-sensitive) you want deleted, if there are multiple folder names that are numbered differently (e.g: folder_1, folder_2...folder_300).\nEnter only part of the folder name(e.g: \'folder_\') seperated by commas, WITHOUT spaces.\nEntered: ')
                        splitted = file_names.split(',')
                        for split in splitted:
                            folder_name_types.append(split)
                        print(f'Folder names---{folder_name_types}---\n')

                        parent_folder_location = input('\nPlease enter folder(s) parent folder PATH(case-sensitive).\nEntered: ')
                        print('')
                        formatted_orig = path_formatter(parent_folder_location)
                        all_folder_in_orig = os.listdir(formatted_orig)
                        for name in folder_name_types:
                            for folder in all_folder_in_orig:
                                if name in folder:
                                    folder_path = (f'{formatted_orig}\\{folder}')
                                    shutil.rmtree(folder_path)
                        print('-------------------------------------------SPECIFIED FOLDERS DELETED-------------------------------------------')
                        continue
                    elif tert_sub_mode == 'mfol':
                        parent_folder_name_types = []
                        parent_folder_name = input('\nPlease enter the parent directory names(case-sensitive)(seperated with commas, WITHOUT SPACES.)\nEntered: ')
                        splitter_folder = parent_folder_name.split(',')
                        for split in splitter_folder:
                            folder_names.append(split)
    
                        folder_name_types = []
                        folder_names = input('\nPlese enter the folder names(case-sensitive) you want deleted, if there are multiple folder names that are numbered differently (e.g: folder_1, folder_2...folder_300).\nEnter only part of the folder name(e.g: \'folder_\') seperated by commas, WITHOUT spaces.\nEntered: ')
                        splitted = folder_names.split(',')
                        for split in splitted:
                            folder_name_types.append(split)
                        print(f'Parent folder names---{parent_folder_name_types}---')
                        print(f'folder names---{folder_name_types}---\n')

                        folder_destination_root_folder = input('\nPlease enter the PATH of the parent directory containing the parent folders containing the specified folders\ne.g: User/Desktop/Folders_of_interest  | you would enter: User/Desktop.\nEntered: ')
                        print('')
                        formatted_dest = path_formatter(folder_destination_root_folder)
                        for parent_folder in parent_folder_name_types:
                            parent_folder_path = (f'{formatted_dest}\\{parent_folder}')
                            all_folders_in_orig = os.listdir(parent_folder_path)
                            for name in folder_name_types:
                                for folder in all_folder_in_orig:
                                    if name in folder:
                                        folder_path = (f'{parent_folder_path}\\{folder}')
                                print(f'DELETING----{folder}----FROM----{folder_path}')
                                shutil.rmtree(folder_path)
                        print('-------------------------------------------SPECIFIED FOLDERS DELETED-------------------------------------------')
                        continue
            elif mode == 'm':
                sub_mode = input('\nMove a single folder from parent directories? Enter: \'SINGLE\'\tMove multiple folders? Enter: \'SPEC\'\nEntered: ').lower()
                if sub_mode == 'single':
                    sec_sub_mode = input('\nWould you like to move this single folder to single/multiple directories?\nSINGLE directory enter: SFOL\tMULTIPLE directory enter: MFOL\nEntered: ').lower()
                    if sec_sub_mode == 'sfol':
                        # origin
                        folder_location = input('\nPlease enter folder(s) location as a PATH(case-sensitive).\nEntered: ')
                        print('')
                        formatted_orig = path_formatter(folder_location)
                        # destination
                        folder_destination = input('\nPlease enter the PATH(case-sensitive) you want your folders moved to.\nEntered: ')
                        print('')
                        formatted_dest = path_formatter(folder_destination)
                        print(f'MOVING---{formatted_orig}---TO---{formatted_dest}') 
                        shutil.move(formatted_orig, formatted_dest)
                        print('-------------------------------------------FOLDER TRANSFER COMPLETE-------------------------------------------')
                        continue
                    elif sec_sub_mode == 'mfol':
                        folder_names = []
                        folder_name = input('\nPlease enter the folder names(case-sensitive)(seperated with commas. WITHOUT SPACES)\nWhere you want to move the one folder to\nEntered: ')
                        splitter = folder_name.split(',')
                        for split in splitter:
                            folder_names.append(split)
                        # origin
                        folder_location = input('\nPlease enter the PATH of the folder you want moved\nEntered: ')
                        print('')
                        formatted_orig = path_formatter(folder_location)
                        # destination
                        folder_destination_root_folder = input('\nPlease enter the PATH(case-sensitive) of the root folder where the collection of folders are in which you want to more the one folder to\ne.g: User/Desktop/Folder_of_interest  | you would enter: User/Desktop.\nEntered: ')
                        print('')
                        formatted_dest = path_formatter(folder_destination_root_folder)
                        for name in folder_names:
                            folder_dest = (f"{formatted_dest}\\{name}")
                            print(f'MOVING----{formatted_orig}----TO----{folder_dest}') 
                            shutil.move(formatted_orig, folder_dest)
                        print('-------------------------------------------FOLDER TRANSFERS COMPLETE-------------------------------------------')
                        continue
                elif sub_mode == 'spec':
                    sec_sub_mode = input('\nWould you like to move specific folders to single/multiple parent folders?\nSINGLE folder enter: SFOL\tMULTIPLE folders enter: MFOL\nEntered: ').lower()
                    if sec_sub_mode == 'sfol':
                        folder_name_types = []
                        folder_names = input('\nPlese enter the folder names(case-sensitive) you want moved, if there are multiple folder names that are numbered differently (e.g: file_1, file_2...file_300).\nEnter only part of the file name(e.g: \'file_\') seperated by commas WITHOUT spaces.\nEntered: ')
                        splitted = file_names.split(',')
                        for split in splitted:
                            folder_name_types.append(split)
                        print(f'Folder names---{folder_name_types}---\n')

                        folder_parent_folder_location = input('\nPlease enter folders(s) parent folder PATH(case-sensitive).\nEntered: ')
                        print('')
                        formatted_orig = path_formatter(file_parent_folder_location)
                        # destination
                        file_destination = input('\nPlease enter the PATH(case-sensitive) you want your folders moved to.\nEntered: ')
                        print('')
                        formatted_dest = path_formatter(file_destination)
                        all_folder_in_orig = os.listdir(formatted_orig)
                        for name in folder_name_types:
                            for folder in all_folder_in_orig:
                                if name in folder:
                                    folder_path = (f'{formatted_orig}\\{folder}')
                                    print(f'MOVING----{folder}----FROM---{formatted_orig}\nTO---{formatted_dest}')
                                    shutil.move(folder_path, formatted_dest)
                        print('-------------------------------------------SPECIFIED FOLDER TRANSFERS COMPLETE-------------------------------------------')
                        continue
                    elif sec_sub_mode == 'mfol':
                        parent_folder_name_types = []
                        parent_folder_name = input('\nPlease enter the parent folder names(case-sensitive)(seperated with commas, WITHOUT SPACES.)\nEntered: ')
                        splitter_folder = folder_name.split(',')
                        for split in splitter_folder:
                            folder_names.append(split)

                        folder_name_types = []
                        folder_names = input('\nPlese enter the file names(case-sensitive), if there are multiple file names that are numbered differently (e.g: file_1, file_2...file_300).\nEnter only part of the file name(e.g: \'file_\') seperated by commas WITHOUT spaces.\nEntered: ')
                        splitted = file_names.split(',')
                        for split in splitted:
                            folder_name_types.append(split)
                        print(f'Parent folder names---{parent_folder_name_types}---')
                        print(f'folder names---{folder_name_types}---\n')

                        # origin
                        parent_folder_location = input('\nPlease enter parent folder(s) PATH(case-sensitive).\nEntered: ')
                        print('')
                        formatted_orig = path_formatter(parent_folder_location)
                        # destination
                        file_destination_root_folder = input('\nPlease enter the PATH of the folders where you want your files moved to.\ne.g: User/Desktop/Folder_of_interest  | you would enter: User/Desktop.\nEntered: ')
                        print('')
                        formatted_dest = path_formatter(file_destination_root_folder)

                        for parent_folder in parent_folder_name_types:
                            parent_folder_path = (f'{formatted_dest}\\{parent_folder}')
                            all_folder_in_orig = os.listdir(parent_folder_path)
                            for name in folder_name_types:
                                for folder in all_folder_in_orig:
                                    if name in folder:
                                        folder_path = (f'{formatted_orig}\\{folder}')
                                        print(f'MOVING----{folder}----FROM---{formatted_orig}\nTO---{formatted_dest}')
                                        shutil.move(folder_path, formatted_dest)
                        print('-------------------------------------------SPECIFIED FOLDER TRANSFERS COMPLETE-------------------------------------------')
                        continue
            elif mode == 'c':
                sub_mode = input('\nCopy all folders? Enter: \'ALL\'\tCopy specified folders? Enter: \'SPEC\'\nEntered: ').lower()
                if sub_mode == 'all':
                    sec_sub_mode = input('\nWould you like to copy all folders to single/multiple parent folders?\nSINGLE folder enter: SFOL\tMULTIPLE folders enter: MFOL\nEntered: ').lower()
                    if sec_sub_mode == 'sfol':
                        # origin
                        file_parent_folder_location = input('\nPlease enter folder(s) location as a PATH.\nEntered: ')
                        print('')
                        formatted_orig = path_formatter(file_parent_folder_location)
                        # destination
                        file_destination = input('\nPlease enter the PATH(case-sensitive) of the parent folder you want to copy this folder to.\nEntered: ')
                        print('')
                        formatted_dest = path_formatter(file_destination)
                        print(f'COPYING---{formatted_orig}---TO---{formatted_dest}') 
                        shutil.copy2(formatted_orig, formatted_dest)
                        print('-------------------------------------------FOLDER COPYING COMPLETE-------------------------------------------')
                        continue
                    elif sec_sub_mode == 'mfol':
                        folder_names = []
                        folder_name = input('\nPlease enter the folder names(case-sensitive)(seperated with commas, WITHOUT SPACES.)\nEntered: ')
                        splitter = folder_name.split(',')
                        for split in splitter:
                            folder_names.append(split)
                        # # origin
                        folder_parent_folder_location = input('\nPlease enter the PATH(case-sensitive) of the parent folder containing the folders you want copied.\nEntered: ')
                        print('')
                        formatted_orig = path_formatter(folder_parent_folder_location)
                        #destination
                        folder_destination_folder = input('\nPlease enter the PATH(case-sensitive) of where you want the folders copied to.\ne.g: User/Desktop/Folder_of_interest  | you would enter: User/Desktop.\nEntered: ')
                        print('')
                        
                        formatted_dest = path_formatter(folder_destination_folder)
                        for folder in folder_names:
                            folder_path = (f'{formatted_orig}\\{folder}')
                            print(f'COPYING----{folder}----FROM---{folder_path}\nTO---{formatted_dest}') 
                            shutil.copy2(folder_path, formatted_dest)
                        print('-------------------------------------------FOLDER COPYING COMPLETE-------------------------------------------')
                        continue
                elif sub_mode == 'spec':
                    sec_sub_mode = input('\nWould you like to move specific files to single/multiple folders?\nSINGLE folder enter: SFOL\tMULTIPLE folders enter: MFOL\nEntered: ').lower()
                    if sec_sub_mode == 'sfol':
                        file_names = []
                        file_name = input('\nPlease enter the file names(case-sensitive)(seperated with commas, WITHOUT SPACES.)\nEntered: ')
                        splitter = file_name.split(',')
                        for split in splitter:
                            file_names.append(split)
                        # origin
                        file_parent_folder_location = input('\nPlease enter file(s) folder PATH(case-sensitive).\nEntered: ')
                        print('')
                        formatted_orig = path_formatter(file_parent_folder_location)
                        # destination
                        file_destination = input('\nPlease enter the PATH(case-sensitive) of the folder you want your FILES moved to.\nEntered: ')
                        print('')

                        formatted_dest = path_formatter(file_destination)
                        all_files_in_orig = os.listdir(formatted_orig)
                        for files in all_files_in_orig:
                            file_path = (f'{formatted_orig}\\{files}')
                            print(f'COPYING---{files}---TO---{formatted_dest}\nFROM---{formatted_orig}') 
                            shutil.copy2(file_path, formatted_dest)
                        print('-------------------------------------------SPECIFIED FILE COPYING COMPLETE-------------------------------------------')
                        continue
                    elif sec_sub_mode == 'mfol':
                        folder_names = []
                        folder_name = input('\nPlease enter the folder names(case-sensitive)(seperated with commas, WITHOUT SPACES.)\nEntered: ')
                        splitter  = folder_name.split(',')
                        for split in splitter:
                            folder_names.append(split)
                        # origin
                        file_parent_folder_location = input('\nPlease enter the PATH(case-sensitive) of the folder containing the files of interest.\nEntered: ')
                        print('')
                        formatted_orig = path_formatter(file_parent_folder_location)
                        # destination
                        file_destination_root_folder = input('\nPlease enter the PATH(case-sensitive) of the parent folder which contains the folders you want your files moved to.\ne.g: User/Desktop/Folder_of_interest  | you would enter: User/Desktop.\nEntered: ')
                        print('')
                        formatted_dest = path_formatter(file_destination_root_folder)
                        all_files_in_orig = os.listdir(formatted_orig)
                        for folder in folder_names:
                            folder_path = (f'{formatted_dest}\\{folder}')
                            for files in all_files_in_orig:
                                file_path = (f'{formatted_orig}\\{files}')
                                print(f'COPYING----{files}----FROM---{formatted_orig}\nTO---{folder_path}') 
                                shutil.copy2(file_path, folder_path)   
                        print('-------------------------------------------FILE COPYING COMPLETE-------------------------------------------')
                        continue