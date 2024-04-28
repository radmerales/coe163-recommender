import csv

def generate_users():
    with open('user_features.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #print("\""+row["Movie"]+"\"", end=", ")
            print("{\""+row['User ID']+"\", ", end = "")
            data = []
            
            count = -1
            for i in row:
                if i!="User" and i!="User ID":
                    data.append(int(row[i][2::]))
                count += 1
            a = str(data)
            print((a.replace('[','{')).replace(']','}'),"}, ")

def generate_movies_index_list():

    with open('movie_features.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #print("\""+row["Movie"]+"\"", end=", ")
            print("{\""+row['Movie']+"\", ", end = "")
            data = []
            
            count = -1
            for i in row:
                if i!="Movie" and row[i]=="1":
                    data.append(int(count)+1)
                count += 1
            while len(data) != 4:
                data.append(0)
            a = str(data)
            print((a.replace('[','{')).replace(']','}'),"}, ")
    
def main():
    b = list()
    with open('movie_features.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #print("\""+row["Movie"]+"\"", end=", ")
            print("{\""+row['Movie']+"\", ", end = "")
            data = []
            
            count = -1
            for i in row:
                if i!="Movie":
                    data.append(int(row[i]))
                count += 1
            a = str(data)
            print((a.replace('[','{')).replace(']','}'),"}, ")
    print(set(b))        

if __name__ == "__main__":
    generate_users()