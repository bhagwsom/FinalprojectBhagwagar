import menu
import api
import db
import scraping
import plotlygraphs

def interactive():
    #Give the main menu (artist, album, )
    print(menu.main_menu)
    term = input("> ")
    return term


def album_menu(information):
    #Give album album
    menu.refresh()
    print(menu.album_menu.format(*information[1:]))
    answer = input('> ')
    if answer =='yes':
        more_info_album(information)
    elif answer=='no':
        return
    else:
        print('Not a valid input')
        menu.pressenter()
def artist_menu(information):
    #artist artist menu
    menu.refresh()
    print(menu.artist_menu.format(*information[1:]))
    answer=input('> ')
    if answer =='yes':
        more_info_artist(information)
    elif answer=='no':
        return
    else:
        print('Not a valid input')
        menu.pressenter()
def more_info_album(information):
    #graphs, image option
    menu.refresh()
    print(menu.detailed_album_menu)
    information2=api.get_album_info('beyonce')
    answer=input('>')
    if answer=='1':
        #trackcount
        trace1=[information[3], information2[3]]
        #albumname
        trace2=[information[1], information2[1]]
        plotlygraphs.plot_graph1(trace1, trace2)

    elif answer=='2':
        #popularitycount
        trace1=[information[5], information2[5]]
        #albumname
        trace2=[information[1], information2[1]]
        plotlygraphs.plot_graph2(trace1, trace2)
    elif answer=='3':
        scraping.get_image(information[-1], mtype='album')
        return
    elif answer=='4':
        album_menu(information)

    else:
        print('Not a valid input')
        menu.pressenter()

def more_info_artist(information):
    #graphs, image option
    menu.refresh()
    print(menu.detailed_artist_menu)
    information2=api.get_artist_info('beyonce')
    answer=input('>')

    if answer=='1':
        #followercount
        trace1=[information[2], information2[2]]
        #artistname
        trace2=[information[1], information2[1]]
        plotlygraphs.plot_graph1(trace1, trace2)
    elif answer=='2':
        #popularity
        trace1=[information[3], information2[3]]
        #artistname
        trace2=[information[1], information2[1]]
        plotlygraphs.plot_graph1(trace1, trace2)
    elif answer=='3':
        scraping.get_image(information[-1], mtype='artist')
        return
    elif answer=='4':
        artist_menu(information)
    else:
        print('Not a valid input')
        menu.pressenter()

while True:
    try:
        menu.refresh()
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
                menu.pressenter()
                (menu.refresh())
            elif answer=='artist':
                db.connect_db_artist()
                menu.pressenter()
                menu.refresh()
            else:
                print('Please insert a new term')
                menu.pressenter()
        else:
            print('Not a valid input')
            menu.pressenter()
    except Exception as e:
        print(e)
        #print('error, try again')
        menu.pressenter()
