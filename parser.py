import csv
def main():
    with open('user_features.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #print("\""+row["Movie"]+"\"", end=", ")
            print("{\""+row['User ID']+"\", ", end = "")
            data = []
            
            for i in row:
                if i != "User ID" and i!= "User":
                    data.append(int(float(row[i])*10000))
            a = str(data)
            print((a.replace('[','{')).replace(']','}'),"}, ")
            

if __name__ == "__main__":
    main()