import csv
def main():
    with open('movie_features.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            #print("\""+row["Movie"]+"\"", end=", ")
            print("{\""+row['Movie']+"\", ", end = "")
            data = []
            
            count = -1
            for i in row:
                if row[i]=="1":
                    data.append(count*1)
                count += 1
            a = str(data)
            print((a.replace('[','{')).replace(']','}'),"}, ")
            

if __name__ == "__main__":
    main()