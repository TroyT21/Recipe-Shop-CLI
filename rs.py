import cmd
import os
import http.client
import json
from ascii_magic import AsciiArt, Back

#print(dir(cmd.Cmd))

class RecipeShopCLI(cmd.Cmd):
    intro = "\n----------Recipe-Shop-CLI----------\nType \"help\" or \"?\" to view commands\n"
    prompt = "\n(Enter Command): "
    
    #Commands
    def do_quit(self, arg):
        "Quit Recipe-Shop-CLI"
        return True
    
    def do_exit(self, arg):
        "Exit Recipe-Shop-CLI"
        return True
    
    def do_close(self, arg):
        "Close Recipe-Shop-CLI"
        return True
    
    def do_connect(self, arg):
        "Set the ip address to connect to: \"connect [ip]\"\nSet the ip address and port to connect to: \"connect [ip] [port]\""
        try:
            connect(*parse(arg))
        except:
            print("Command failed.\nRun \"help [command]\" to check how to run it.")

    def do_check(self,arg):
        "Check the ip address and port used for connection: \"check\""
        try:
            checkConnect()
        except:
            print("Command failed.\nRun \"help [command]\" to check how to run it.")
    
    def do_login(self, arg):
        "Login to Recipe-Shop: \"login [username] [password]\""
        try:
            login(*parse(arg))
        except:
            print("Command failed.\nRun \"help [command]\" to check how to run it.")
    
    def do_logout(self, arg):
        "Logout of Recipe-Shop: \"logout\""
        try:
            logout()
        except:
            print("Command failed.\nRun \"help [command]\" to check how to run it.")
    
    def do_user(self, arg):
        "Check if a username already exists: \"user [username]\""
        try:
            user(arg)
        except:
            print("Command failed.\nRun \"help [command]\" to check how to run it.")
    
    def do_register(self, arg):
        "Register new user: \"register [username] [password] [confirmPassword]"
        try:
            register(*parse(arg))
        except:
            print("Command failed.\nRun \"help [command]\" to check how to run it.")

    def do_search(self, arg):
        "Search for recipes: \n\"search [keywords] [min Time] [max Time] [meal type]\"\n\"search [keywords] [min Time] [max Time]\"\n\"search [keywords] [meal type]\"\n\"search [keywords]\"\nSeparate multiple keywords with \"/\""
        try:
            search(*parse(arg))
        except:
            print("Command failed.\nRun \"help [command]\" to check how to run it.")
    
    def do_recipe(self, arg):
        "View more details about a recipe: \"recipe [recipe #]\"\nMust use search command first to get recipe #"
        try:
            recipe(arg)
        except:
            print("Command failed.\nRun \"help [command]\" to check how to run it.")

    def do_last(self, arg):
        "View the results from the last search command: \"last\""
        try:
            printRecipeList()
        except:
            print("Command failed.\nRun \"help [command]\" to check how to run it.")


# RecipeShopCLI class
#=============================================================================================


#Global Variables
ip = "localhost"
port = 80
username = ""
recipes = []


#Functions
def parse(args):
    return tuple(map(str, args.split()))

def connect(*args):
    if(len(args) == 2):
        connect2(args[0], args[1])
    elif(len(args) == 1):
        connect1(args[0])
    else:
        print("Invalid number of arguments.\nRun \"help [command]\" to check how to run it.")

def connect2(serverIP, serverPort):
    global ip
    ip = serverIP
    global port
    port = serverPort
    checkConnect()

def connect1(serverIP):
    global ip
    ip = serverIP
    global port
    port = 80
    checkConnect()

def checkConnect():
    print("ip: ", ip)
    print("port: ", port)

def login(user, password):
    global username
    if(username == ""):
        try:
            url = ip + ":" + str(port)
            params = "/api/login?username=" + user + "&password=" + password
            conn = http.client.HTTPConnection(url)
            conn.request("GET", params)
            res = conn.getresponse()
            print(res.status, res.reason)
            data = json.loads(res.read().decode("utf-8"))
            if(res.status == 200):
                print(data["message"])
                username = user
            else:
                print(data["error"])
        except:
            print("Failed to connect.\nRun \"check\" command to see ip\nRun \"connect\" command to change ip")
    else:
        print("Already logged in as", username)

def logout():
    global username
    if(username == ""):
        print("Not logged in.")
    else:
        print(username, "logged out.")
        username = ""

def user(user):
    try:
        url = ip + ":" + str(port)
        params = "/api/user-exist?username=" + user
        conn = http.client.HTTPConnection(url)
        conn.request("GET", params)
        res = conn.getresponse()
        print(res.status, res.reason)
        data = json.loads(res.read().decode("utf-8"))
        if(res.status == 200):
            if(data["exists"]):
                print("Username", user, "already in use")
            else:
                print("Username", user, "is available")
        else:
            print(data["error"])
    except:
        print("Failed to connect.\nRun \"check\" command to see ip\nRun \"connect\" command to change ip")

def register(user, password, confirm):
    global username
    if(username == ""):
        try:
            url = ip + ":" + str(port)
            params = "/api/register"
            body = json.dumps({
                "username": user,
                "password": password,
                "confirmPassword": confirm
            })
            #print(body)
            headers = {
                "Content-Type": "application/json",
                "Content-Length": len(body)
            }
            #print(headers)
            conn = http.client.HTTPConnection(url)
            conn.request("POST", params, body, headers)
            res = conn.getresponse()
            print(res.status, res.reason)
            data = json.loads(res.read().decode("utf-8"))
            if(res.status == 201):
                print(data["message"])
            else:
                print(data["error"])
        except:
            print("Failed to connect.\nRun \"check\" command to see ip\nRun \"connect\" command to change ip")
    else:
        print("Already logged in as", username)
        print("Please logout before registering a new user.")

def search(*args):
    if(len(args) == 4):
        search4(args[0], args[1], args[2], args[3])
    elif(len(args) == 3):
        search3(args[0], args[1], args[2])
    elif(len(args) == 2):
        search2(args[0], args[1])
    elif(len(args) == 1):
        search1(args[0])
    else:
        print("Invalid number of arguments.\nRun \"help [command]\" to check how to run it.")

def search4(keywords, minTime, maxTime, mealType):
    if(keywords != ""):
        if(minTime < maxTime):
            try:
                url = ip + ":" + str(port)
                params = "/api/recipe/search?keyword=" + str(keywords).replace("/","+") + "&mealType=" + mealType + "&time=" + minTime + "-" + maxTime
                #print(params)
                conn = http.client.HTTPConnection(url)
                conn.request("GET", params)
                res = conn.getresponse()
                print(res.status, res.reason)
                data = res.read()
                if(res.status == 200):
                    #print(data[:250], "...")
                    getRecipeList(json.loads(data))
                else:
                    print(data)
            except:
                print("Failed to connect.\nRun \"check\" command to see ip\nRun \"connect\" command to change ip")
        else:
            search2(keywords, mealType)
    else:
        print("Please enter keywords and try again.")

def search3(keywords, minTime, maxTime):
    if(keywords != ""):
        if(minTime < maxTime):
            try:
                url = ip + ":" + str(port)
                params = "/api/recipe/search?keyword=" + keywords + "&time=" + minTime + "-" + maxTime
                #print(params)
                conn = http.client.HTTPConnection(url)
                conn.request("GET", params)
                res = conn.getresponse()
                print(res.status, res.reason)
                data = res.read()
                if(res.status == 200):
                    #print(data[:250], "...")
                    getRecipeList(json.loads(data))
                else:
                    print(data)
            except:
                print("Failed to connect.\nRun \"check\" command to see ip\nRun \"connect\" command to change ip")
        else:
            search1(keywords)
    else:
        print("Please enter keywords and try again.")

def search2(keywords, mealType):
    if(keywords != ""):
        try:
            url = ip + ":" + str(port)
            params = "/api/recipe/search?keyword=" + keywords + "&mealType=" + mealType
            #print(params)
            conn = http.client.HTTPConnection(url)
            conn.request("GET", params)
            res = conn.getresponse()
            print(res.status, res.reason)
            data = res.read()
            if(res.status == 200):
                #print(data[:250], "...")
                getRecipeList(json.loads(data))
            else:
                print(data)
        except:
            print("Failed to connect.\nRun \"check\" command to see ip\nRun \"connect\" command to change ip")
    else:
        print("Please enter keywords and try again.")

def search1(keywords):
    if(keywords != ""):
        try:
            url = ip + ":" + str(port)
            params = "/api/recipe/search?keyword=" + keywords
            #print(params)
            conn = http.client.HTTPConnection(url)
            conn.request("GET", params)
            res = conn.getresponse()
            print(res.status, res.reason)
            data = res.read()
            if(res.status == 200):
                #print(data[:250], "...")
                getRecipeList(json.loads(data))
            else:
                print(data)
        except:
            print("Failed to connect.\nRun \"check\" command to see ip\nRun \"connect\" command to change ip")
    else:
        print("Please enter keywords and try again.")

def getRecipeList(data):
    fro = data["from"]
    to = data["to"]
    if(fro <= to):
        global recipes
        recipes = []
        for i in range(to - fro + 1):
            recipes.append(data["hits"][i])
        printRecipeList()
    else:
        print("No recipes found.")

def printRecipeList():
    if(len(recipes) > 0):
        iMax = len(str(len(recipes)))
        for i in range(iMax):
            print(" ", end="")
        print("# | Recipe Name")
        print("=========================================================")
        index = 0
        for recipe in recipes:
            iNum = str(index)
            for i in range(iMax + 1 - len(iNum)):
                print(" ", end="")
            print(index, " | ", recipe["recipe"]["label"], sep="")
            index += 1
    else:
        print("No recipes found. Please use search first.")

def recipe(arg):
    index = int(arg)
    if(index >= 0 and index < len(recipes)):
        print("\n", recipes[index]["recipe"]["label"], sep="")
        print("Recipe from", recipes[index]["recipe"]["source"], "\n")
        try:
            print("Image:")
            image = AsciiArt.from_url(recipes[index]["recipe"]["image"])
            image.to_terminal(min(os.get_terminal_size().columns,os.get_terminal_size().lines*2))

            #image.to_html_file('image.html', columns=200)
            #filePath = "file:///Recipe-Shop-CLI/image.html"
            #print("\n", "Better Image (opens in browser):\n", filePath, sep="")
        except OSError as e:
            print("\nFailed to load image.")
        print("\nIngredients:")
        for i in range(len(recipes[index]["recipe"]["ingredientLines"])):
            print("  \u2022", recipes[index]["recipe"]["ingredientLines"][i])
        print("\nInstructions:")
        print(recipes[index]["recipe"]["url"])
    else:
        print("Invalid recipe #.\nCheck last search with \"last\" command, or make a new search with \"search\" command.")


    


#start cli
RecipeShopCLI().cmdloop()