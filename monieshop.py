import os

def highestSalesValueForaDay(transactionFolder, transactionDay):
    saleAmounts = []
    for fileName in os.listdir(transactionFolder):
        if fileName.endswith(".txt"):
            
            # Prints only text file present in My Folder
            # print(x)
            formattedFileName = fileName[:10]
            if formattedFileName == transactionDay:
                print(f"File for day {transactionDay} found:{fileName}")
                f = os.path.join(transactionFolder, fileName)
                if os.path.isfile(f):
                    with open(f, 'r') as file:
                        for line in file:
                            lineData = [data.strip() for data in line.split(',')]
                            dataIndex = 0
                            while dataIndex < len(lineData):
                                if dataIndex == 3:
                                    saleAmounts.append(float(lineData[dataIndex]))
                                dataIndex += 1
                    break
    maxSalesValuePerDay = max(saleAmounts)
    return(maxSalesValuePerDay)

def mostSoldProductIdByVolume():
    return

def highestSalesStaffIdPerMonth(transactionFolder):
    jan = []
    feb = []
    mar = []
    apr = []
    may = []
    jun = []
    jul = []
    aug = []
    sep = []
    oct = []
    nov = []
    dec = []
    
    months = [jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec]
    # Array to store the highest staff id for each month
    monthsHighestStaffIds = []
    # Go through all the files
    for fileName in os.listdir(transactionFolder):
        if fileName.endswith(".txt"):
            f = os.path.join(transactionFolder, fileName)
            # Get the month of the file and
            if "-01-" in fileName:
                jan.append(f)
            if "-02-" in fileName:
                feb.append(f)
            if "-03-" in fileName:
                mar.append(f)
            if "-04-" in fileName:
                apr.append(f)
            if "-05-" in fileName:
                may.append(f)
            if "-06-" in fileName:
                jun.append(f)
            if "-07-" in fileName:
                jul.append(f)
            if "-08-" in fileName:
                aug.append(f)
            if "-09-" in fileName:
                sep.append(f)
            if "-10-" in fileName:
                oct.append(f)
            if "-11-" in fileName:
                nov.append(f)
            if "-12-" in fileName:
                dec.append(f)  
    
    for month in months:
        highestStaffId = highestStaffIdForOneMonth(month)
        monthsHighestStaffIds.append(highestStaffId)
        
    return(monthsHighestStaffIds)
    
    # return jan
# print(printNumber())

def highestStaffIdForOneMonth(month):
    staffIds = []
    for f in month:
        staffIds = []
        lineCount = 0
        # Open a partifcular file
        with open(f, 'r') as file:
            # For each line in that file
            for line in file:
                lineData = [data.strip() for data in line.split(',')]
                dataIndex = 0
                while dataIndex < len(lineData):
                    if dataIndex == 0:
                        staffIds.append(int(lineData[dataIndex]))
                        staffIds.append(int(lineData[dataIndex]))
                    dataIndex += 1
    
    highestStaffId = max(set(staffIds), key=staffIds.count)
    return(highestStaffId)

def highestHourOfTheDayByAverageTransactionVolume():
    return

def analyticsSoftware():
    print("Welcome to MonieShop Analytics Software!")
    print("To analyse your transaction files, please provide the path to the transaction folder")
    
    print("This software can get you the following metrics\n:1.Highest Sales Volume in a Day\n2.Highest Sales value in a day\n3.Most Sold Product ID by Volume\n4.Highest Sales Staff ID For Each Month\n5.Highest Hour of the Day By Average Transaction Volume")
    
    print("To get any of this metrics using this software, just input the number attached to the metric/nFor example: If you want to get the Most Sold Product ID by volume of your trasaction dat, input 3")
    
    print("To go back to the main menu after getting a metric, input 'Main Menu")
    
    path = input("Input path to your transactions folders: ").strip()
    
    metric = input("What metric do you want to get?: ")
    
    if metric == "2":
        transactionDay = input("Please enter the transaction day in the format '2025-11-08: ")
        result = highestSalesValueForaDay(path, transactionDay)
        print (f"The highest sales value for the transaction day '{transactionDay}' is: {result}")
    if metric == "4":
        result = highestSalesStaffIdPerMonth(path)
        print(f"The Highest sales staff ID for each month is: {result}")

analyticsSoftware()