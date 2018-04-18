import sqlite3

DBNAME = 'Spotify.db'

def init_db():
    conn =sqlite3.connect(DBNAME)
    cur=conn.cursor()

    statement='''
        DROP TABLE IF EXISTS 'Albums';
        '''
    cur.execute(statement)
    statement='''
        CREATE TABLE 'Albums'(
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'AlbumName' TEXT NOT NULL,
            'ArtistName' TEXT NOT NULL,
            'TrackCount' INTEGER NOT NULL,
            'ReleaseDate' TEXT NOT NULL,
            'Popularity' INTEGER NOT NULL

        );
    '''
    cur.execute(statement)

    statement='''
        DROP TABLE IF EXISTS 'Artists';
        '''
    cur.execute(statement)
    statement='''
        CREATE TABLE 'Artists'(
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'ArtistName' TEXT NOT NULL,
            'FollowerCount' INTEGER NOT NULL,
            'PopularityCount' INTEGER NOT NULL,
            'Genres' TEXT NOT NULL
        );
    '''
    cur.execute(statement)
    conn.commit()
    conn.close()

def write_artist(artist_info_list):
    conn=sqlite3.connect(DBNAME)
    cur=conn.cursor()
    insertion = artist_info_list
    sql_insert = '''
        INSERT INTO "Artists"
        VALUES(?,?,?,?,?)'''
    cur.execute(sql_insert, insertion)
    conn.commit()
    conn.close()

def write_album(album_info_list):
    conn=sqlite3.connect(DBNAME)
    cur=conn.cursor()
    insertion = album_info_list
    sql_insert = '''
        INSERT INTO "Albums"
        VALUES(?,?,?,?,?,?)'''
    cur.execute(sql_insert, insertion)
    conn.commit()
    conn.close()

def connect_db_album():
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    cur.execute('SELECT Id, AlbumName FROM Albums')
    print('Your history:')
    for row in cur:
        print(row[0], row[1])

def connect_db_artist():
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    cur.execute('SELECT Id, ArtistName FROM Artists')
    print('Your history:')
    for row in cur:
        print(row[0], row[1])


init_db()
