import menu
import api
import db
def interactive():
    #Give the main menu (artist, album, )
    print(menu.main_menu)
    term = input("> ")
    return term


def album_menu(information):
    #Give album album
    print(menu.album_menu.format(*information[1:]))
    answer = input('> ')
    if answer =='yes':
        more_info_album()
    if answer=='no':
        return
    else:
        print('Not a valid input')
def artist_menu(information):
    #artist artist menu
    print(menu.artist_menu.format(*information[1:]))
    answer=input('> ')
    if answer =='yes':
        more_info_artist()
    if answer=='no':
        return
    else:
        print('Not a valid input')
def more_info_album():
    #graphs, image option
    print(menu.detailed_album_menu)
    answer=input('>')
    if answer=='1':
        pass
    elif answer=='2':
        pass
    elif answer=='3':
        pass
    elif answer=='4':
        album_menu(information)
    else:
        print('Not a valid input')

def more_info_artist():
    #graphs, image option
    print(menu.detailed_artist_menu)
    answer=input('>')
    if answer=='1':
        pass
    elif answer=='2':
        pass
    elif answer=='3':
        pass
    elif answer=='4':
        artist_menu(information)
    else:
        print('Not a valid input')

while True:
    answer=interactive()
    number=answer[0]
    search_term=answer[1:]
    if answer=='4' or answer =='quit':
        print('Goodbye. Have a nice day :)')
        break
    elif number=='1':
        information=api.get_artist_info(search_term)
        db.write_artist(information)
        artist_menu(information)

    elif number =='2':
        information=api.get_album_info(search_term)
        db.write_album(information)
        album_menu(information)


    elif number=='3':
        answer=input('Do you want your album history or artist history?\n')
        if answer=='album':
            db.connect_db_album()
            print('\n \n \n \n We will now reconnect you back to the main menu... \n .. \n .. \n .. \n')
        if answer=='artist':
            db.connect_db_artist()
            print('\n \n \n \n We will now reconnect you back to the main menu... \n .. \n .. \n .. \n')
        else:
            print('Not a valid search term')
    else:
        print('Not a valid input')
