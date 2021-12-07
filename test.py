from flask import *
import mysql.connector

app= Flask(__name__)
@app.route('/', methods=['POST','PUT', 'DELETE', 'GET'])
def lib():

    flag=0
    database = mysql.connector.connect(user='root', password='password', host='localhost',database='library') 
    mycursor = database.cursor() 

    if request.method == 'GET':
        query = "select * from books where BookName = " + f" '{request.args['bookname']}'"
        dataFetcher = query
        mycursor.execute(dataFetcher)
        flag=1
        finalData = mycursor.fetchall()
        json_con = json.dumps(finalData)
        print(finalData)

    elif request.method == 'PUT':
         #put the data to the database
         #creates a resource
        print('Got PUT requestS')
        a={request.args.get['BookName']}
        b={request.args.get['Author']}
        c={request.args.get['ReleaseYear']}
        d={request.args.get['Price']}
        e={request.args.get['Availability']}
        query2 = "INSERT INTO books (BookName,Author,ReleaseYear,Price,Availability) VALUES (%s, %s ,%s ,%s ,%s)"
            
        val2=(a,b,c,d,e) 
        mycursor.execute(query2,val2)
        flag=1
        finalData1 = mycursor.fetchall()
        json_con = json.dumps(finalData1)
        print(finalData1)
        
    elif request.method == 'POST':
         #post the data to the database
         #updates a resource
         #print('Got POST request')
        print(request.json)
        #return  jsonify(isError= False,
                   #message= "Success",
                    #statusCode= 200,
        #), 200
        fgh=input("Enter total number of records you want to insert: ")
        for k in fgh:               
                 a1=request.args['BookName']
                 b1=request.args['Author']
                 c1=request.args['ReleaseYear']
                 d1=request.args['Price']
                 e1=request.args['Availability']
                 query1 = "INSERT INTO books (BookName,Author,ReleaseYear,Price,Availability) VALUES (%s, %s ,%s ,%s ,%s)"
                    
                 val1=(a1,b1,c1,d1,e1) 
                 mycursor.execute(query1,val1)
                 flag=1
                 finalData = mycursor.fetchall()
                 json_con = json.dumps(finalData)
                 print(finalData)
    
    elif request.method == 'DELETE':
         #delete a resource from the database
        print('Got delete request')

    else:
         #invalid request method
         #return some err
        print('BAD REQUEST!')


    if flag == 1:
        return json_con

if __name__ == "__main__":
    app.run(debug=True,port=8080)


