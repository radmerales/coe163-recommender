import csv
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
    main()