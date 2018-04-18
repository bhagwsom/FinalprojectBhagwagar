def init_db_json():
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
            'ReleaseDate' TEXT NOT NULL,
            'TrackCount' TEXT NOT NULL

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
            'ArtistName' TEXT NOT NULL
        );
    '''
    cur.execute(statement)

    statement='''
        DROP TABLE IF EXISTS 'Tracks';
        '''
    cur.execute(statement)
    statement='''
        CREATE TABLE 'Tracks'(
            'Id' INTEGER PRIMARY KEY AUTOINCREMENT,
            'ArtistName' TEXT NOT NULL,
            'AlbumName' TEXT NOT NULL,
            'TrackLength' INTEGER NOT NULL
        );
            '''
    cur.execute(statement)

    conn.commit()
    conn.close()
