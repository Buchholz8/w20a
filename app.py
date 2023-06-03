#i imported the dbhelpers
import dbhelpers
#this first function will call the client_post in the database and check the username and password that 
#we will later run into when logging in
def check_user(username, password):
    sql = "CALL client_post(? , ?)"
    args = (username, password)
    results = dbhelpers.run_procedures(sql , args)
    if results:
        return results[0][0]
    else:
        return None
#this function will take inputs from the user and send them to the data base to be used to insert a post
def make_post(client_id):
    title = input('enter title here:')
    content = input('enter content here:')
    sql = 'CALL insert_post(? , ? , ?)'
    args = (client_id, title, content)
    print('Post Successful')
#get posts will call the get_post and that will return all of the posts and print them with their repected row
def get_posts():
    sql = 'CALL get_posts()'
    results = dbhelpers.run_procedures(sql, None)
    for row in results:
        print('Title:' , row[0])
        print('Content:' , row[1])
        print()
#login loop will ask for a input of 1 of 3 things and use that to call the specific function the user is wanting
#this will return the choice set
def login_loop():
    while True:
        choice = input("Select an option: \n1. Insert a new post\n2. Read all posts\n3. Quit\n")

        if choice == '1':
            client_id = input("Enter your client id: ")
            make_post(client_id)
        elif choice == '2':
            get_posts()
        elif choice == '3':
            return
        else:
            print("Please, enter a choice")
#this is the main function that will take the username and password entered by a user and check them with
#the check_user function and eithe rprint login successful if they match or invalid username or password if it fails
def main():
    username = input('enter your username :')
    password = input('enter your password :')
    client_id = check_user(username, password)
    if client_id:
        print('login successful. client_id')
        login_loop()
    else:
        print('Invalid username or password')
#i found this on dev docs and this from my understanding checks to see if this is the main file being ran
#i thought this would be not needed but cetainly helpful especially when importing information from another
#i would like ur take on this
if __name__ == '__main__':
    main()
    