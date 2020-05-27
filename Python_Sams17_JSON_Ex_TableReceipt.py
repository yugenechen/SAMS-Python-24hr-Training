# -*- coding: utf-8 -*-

'''# Python_Sams17_waiterReceipt.py a.k.a. TableReceipt.py
    The restaruant owner wants to track cashflow (receipts):
         a) Track daily grand totals (of receipts)
         b) Check grand totals from prior days

    Added:
        get_receiptDailyTotal() - gets a day's recept total from user provided
                                  date.
        calc_dailyTotal(filename) - calculates day's receipt total receipts in
                                    a file.
        get_receipt_total(seats) - calculates a table receipt total for a given
                                   list of seats
    Excercise Description:
    The restarurant manager had been asking for a grand total for receipts
    every day. This functnion:\n
        a) Provides the total for a given day.\n
        b) Accepts a date item object for the given day and then returns
           a float containing the grand total for that day.\n
        c) This function determines the name of the file to pull data from.\n
        d) Extra Credit, reformat the JSON file so that the Daily GrandTotal
               is stored in the 'receipt' JSON file.\n
          [Chen]:  Architectural decision.  First thought to make a new JSON 
                   structure as receipts = {"Total":0,
                                            "receipts":{"hh:mm:ss":<receipt vale>}
                                            }
                   The above structure seems to overcomplicate the code.
                   Since receipts is already a single level <dict>, it is 
                   simpler to just add a new key with assocatied value:
                   "Total":<total for the day value>, where this item is
                   updated everytime a new table receipt is entered (and
                   printed).

                   This approach requires the least change in the existing code
                   and it still efficiently handles the quick access of Total.

Created on Mon May 11 18:33:59 2020

@author: Lifygen
'''


from datetime import datetime
import json
import os


def print_seat(seat):
    for item in seat:
        print("             ${}".format("{:.2f}".format(item).rjust(9, " ")))
    print("_"*23)
    total = get_seat_total(seat)
    print("      Total: ${}\n".format("{:.2f}".format(total).rjust(9, " ")))
    


def get_seat_total(seat):
    total = 0
    for dish in seat:
        total = total + dish
    return total


def get_seat():
    seat = []
    while True:
        item = input("Enter an item amount [ [0] to go to the next seat]: ")
        if (item != '0'):
            try:
                seat.append(float(item))
            except ValueError:
                print("\nInvalid entry, please try again.")
        else:
            return seat


def get_seats():
    seats = []
    seat_num = input("How many seats? ")
    for i in range(int(seat_num)):
        print("Seat", i+1)
        seat = get_seat()
        seats.append(seat)
    return seats


def print_time():
    time = datetime.now()
    time_template = "Date/Time: {mm}/{dd}/{yyyy} {HH}:{MM}\n"
    # commented out original code and replaced with double letter format
    # print(time_template.format(M=time.month, D=time.day, Y=time.year,
    #                            H=time.hour, Min=time.minute))
    print(time_template.format(mm=time.strftime("%m"),
                               dd=time.strftime("%d"),
                               yyyy=time.strftime("%Y"),
                               HH=time.strftime("%HH"),
                               MM=time.strftime("%MM")
                               ))


def print_receipt(seats):
    print_time()
    for seat in seats:
        print_seat(seat)
    # Moved grand_total calc to a function so it's callable without printing
    grand_total = get_receipt_total(seats)
    print("\n" + "="*23 + "\n" + "Grand Total: ${}".
          format("{:.2f}".format(grand_total).rjust(9, " ")))


def get_receipt_total(seats):
    # Calcualte and return the Table Total (seat receipts sum for a table.
    # Implemented as a separate function instead of altering print_receipt()
    # to optionally turn on/off a return and turn on/off the print.
    tableTotal = 0
    for seat in seats:
        tableTotal += get_seat_total(seat)
    return tableTotal


def calc_dailyTotal(filename):
    # Calcualte and return the Grand Total of all the receipts in a JSON file.
    # This was implemented as part of "d) Extra Credit poriton of the excercise
    daysReceipts = get_receipts(filename)
    dailyTotal = 0
    for receipt in daysReceipts:
        if receipt == "Total":
            continue
        else:
            dailyTotal += daysReceipts[receipt]
    return dailyTotal


def get_receipts(filename):
    ''' The restaruant owner wants to track cashflow (receipts):
            a) Track daily grand totals (of receipts)
            b) Check grand totals from prior days
        This program gets all receipts from a file that is in JSON format.
        The goal is to then take the current table receipt and add it to
        the JSON file [see save_receipt()].
    '''
    try:
        # Try opening the receipt json file:
        f = open('data/receipts/' + filename)
        receipts = json.load(f)
        f.close()
    except FileNotFoundError as e:
        # If the json file does not exist then create an empty <dict>.
        # So save_receipt() will save a new blank file or use
        # a blank <dict> to add a new receipt before saving it as a json.

        #receipts={}    # old initialization if file did not already exist.

        # New file intialization includes a "0" "Total" key item in the <dict>.
        receipts = {"Total": 0}
        print("\nAn Error occurred in 'get_receipts':\n{}".format(filename))
        print("e.strerror:  ", e.strerror)
        print("e.filename:  ", e.filename)
        print("Creating a new receipt file....")
    return receipts


def save_receipt(total):
    ''' Opens a receipt file, saves the current receipt total to the file
        with the datetime as the key and the value as the recept total.
    '''
    try:
        # Make a 'receipts' directory if it does not already exist:
        os.mkdir('data/receipts/')
    except FileExistsError:
        pass
    # Generate a new key for the receipt, get the receipt file (generate
    # the receipt file if it does not already exist), and store the
    # receipt total associated with its unique key as an additional receipt
    # in the receipt#.json file and in a <dict> as the value of the new key.
    date = datetime.now()
    filename = "receipt {Y}{M}{D}.json".format(
            Y=date.strftime('%Y'), M=date.strftime('%m'),
            D=date.strftime('%d'))
    # Note: key construction changes:
    #       1. changed to 2-character month, day, and 4-character year
    #       2. added 'h', 'm', 's' suffixes and ':' separator to the key
    receipts = get_receipts(filename)
    key = (str(date.strftime('%Hh')) + ":" + str(date.strftime('%Mm')) + ":" +
           str(date.strftime('%Ss')))
    receipts[key] = total
    # Excercise extra credit (item d changes):
    # Get the old daily total before the new table total has been added and add
    # the new table total to calculate a new daily total and then store it.
    dailyTotal = float(calc_dailyTotal(filename))
    dailyTotal += float(total)
    receipts["Total"] = dailyTotal
    # Save the <dict> items:  <new table reciept total> and <new daily total>
    f = open('data/receipts/' + filename, 'w')
    json.dump(receipts, f, indent=2)
    f.close()


def get_receiptDailyTotal():
    '''
    The restarurant manager had been asking for a grand total for receipts
    every day. This functnion:\n
        a. Provides the total for a given day.\n
        b. Accepts a date item object for the given day and then returns
           a float containing the grand total for that day.\n
        c. This function determines the name of the file to pull data from.\n
        d. Extra Credit, reformat the JSON file so that the Daily GrandTotal
           is stored in the 'receipt' JSON file.\n
    INPUTS:\n
        date - string, "mm/dd/yyyy" format. If mm and/or yyyy is omitted then\n
                       current year is used.
    OUTPTUS:\n
        prints out the daily total in mm/dd/yyy: <$#.##> format.\n
        stores the daiy total in the 'reciept mmddyyyy.json' file.\n
'''
    # Get the Date from the User and check it for validity.
    # and construct a filename from the date entery if it is valid
    date = ""
    today = datetime.now()
    while not date:
        date = input("Input the day you want to the receipt totals from " +
                     "if month and/or year omitted, " +
                     "the current day's ones will be used.\n" +
                     "[mm/dd/yyyy]: ")
        dateData = date.split("/")
        if (len(dateData) == 3):
            mm = dateData[0]
            if len(mm) == 1:
                mm = "0" + mm
            dd = dateData[1]
            if (len(dd) == 1):
                dd = "0" + dd
            yyyy = dateData[2]
            while ((len(yyyy) < 4)):
                if (len(yyyy) == 2):
                    # get 4 character year.get first two characters using
                    # the range [start : end: step].  Similar to loop range but
                    # it uses ":" instead of "," between items.
                    yyyy = today.strftime("%Y")[0:2] + yyyy
                response = input("Is {} the correct year? [y/n]: ".format(yyyy))
                if not response:
                    yyyy = input("{} is an INVALID year, ".format(yyyy) +
                                 "between 1773-9999.\n" +
                                 "Input new year in [yyyy] format: ")
                if not(int(yyyy) in range(1773, 9999)):
                    yyyy = ""
        elif (len(dateData) == 2):
            mm = dateData[0]
            if len(mm) == 1:
                mm = "0" + mm
            dd = dateData[1]
            if (len(dd) == 1):
                dd = "0" + dd
            yyyy = today.strftime("%Y")
        elif (len(dateData) == 1):
            dd = dateData[0]
            if (len(dd) == 1):
                dd = "0" + dd
            mm = today.strftime("%m")
            yyyy = today.strftime("%Y")
        else:
            date = ""

        # Check that month is 1-12 and day is 1-31
        if (not(int(mm) in range(1, 13)) or not(int(dd) in range(1, 32))):
            date = ""
        if not date:
            print("Invalid date input, try again.")

    filename = "receipt {yyyy}{mm}{dd}.json".format(yyyy=yyyy, mm=mm, dd=dd)

    # Attempt to get the daily total saved in the file.  If Total does not
    # exist, then calculate it, write it to the file, and display it here.
    receipts = get_receipts(filename)
    if (receipts == {"Total": 0}):
        print("\nAn Error occurred in 'get_receipts':\n\t{}".format(filename) +
              "\n File or folder not found.  " +
              "Try another date or begin a new Table receipt entry.\n")
        return ("No file found for " + date + ".")
    else:
        # Use file value or calc a new dailyTotal if it is not in the file
        dailyTotal = receipts.get("Total", calc_dailyTotal(filename))
        # Write the dailyTotal if it does not exist in the file or if it does
        # not match the newly calculated one.
        if ((receipts.get("Total", 0)) or
            (receipts.get("Total", 0) != dailyTotal)
            ):
            receipts["Total"] = dailyTotal
            f = open('data/receipts/' + filename, 'w')
            json.dump(receipts, f, indent=2)
            f.close()

    return ("{} days Total: ${}".format(mm + "/" + dd + "/" + yyyy,
              "{:.2f}".format(dailyTotal).rjust(9, " ")))


# ===================================================
# *** MAIN Programs
def mainReceipt():
    quitSeats = False
    while not(quitSeats):
        output =""
        print("====================================\n" +
              'This is the "Table Receipt" program.\n' +
              "====================================")
        response = input("[E]nter Table receipt or " +
                         "[R]etrieve a days total or " +
                         "[Q]uit [E or R or Q]: ")
        if not response:
            print("\n\t<<< Null input. Try again. >>>")
        elif (response[0].lower() == "r"):
            output = (get_receiptDailyTotal())
        elif (response[0].lower() == "e"):
            # Collect table per seat.
            seats = get_seats()
            # Print the table charges per eat and the total for the table.
            print_receipt(seats)
            # Save the table total to file.
            save_receipt(get_receipt_total(seats))
        elif (response[0].lower() == "q"):
            quitSeats = True
            # Ends looping
        else:
            print('\n\t<<< ["{}"] is INVALID input. Try again. >>>'.format(response))
        print(output)

# ===================================================
def main():
    print("Hello World!")

# ===================================================


if __name__ == "__main__":
    # [Test #1] Test the kitchen classes:  Ingredient(), Recipe(), Inventory()
    # from classes.ingredients import Ingredient
    # from classes.recipes import Recipe

    main()
    mainReceipt()
