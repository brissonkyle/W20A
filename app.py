import dbcreds
import mariadb

conn=None
cursor=None

conn = mariadb.connect(
                        user=dbcreds.user,
                        password=dbcreds.password, 
                        host=dbcreds.host,
                        database=dbcreds.database,
                        port=dbcreds.port
                        )
cursor = conn.cursor()


print('Welcome to the BLOG! ')
username = input('Please enter username! : ')
print('Hows your day {} !! '.format(username))
print('Please select an option: ')
print('1 : Make a post!')
print('2 : See ALL posts')
selection = input('1 or 2 ? ')
selection = int(selection)

while True:
    if selection == 1:
        int(selection) == 1
        print('Make a Post!! ')
        post = input('... : ')
        cursor.execute('INSERT INTO blog_post (username, content) VALUES (?,?)', [username,post])
        conn.commit()
        print('Nice !! Post Completed : {} '.format(post))
        exit = input('Press Enter to Exit Interface')
        if exit:
            break
    elif selection == 2:
        int(selection) == 2
        print('See ALL posts! ')
        cursor.execute('SELECT content FROM blog_post')
        allPosts = cursor.fetchall()
        # print('Here are some POSTS : {}'.format(allPosts))
        # exit()
    else :
        exit()
