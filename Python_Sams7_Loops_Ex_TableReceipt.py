#  SAMS Python Chapter 7 Quiz and Excercise
# 1. What is the difference between a for loop and while loop?
#    [Answer]:
#       for loop - iterates through a list (numbers or items);
#                  it loops a finite number of times.
#       while loop -  loops an undetermined amount of times.  Loop is dependent
#                     on a logical condition.  It loops until the loop condition
#                     is  no longer met.

# 2. How would you get a range of even numbers, from 1 to 100?
#    [Answer]:  Use a step 2.
#               myEvenRange = []
#               for loopIndex in range(2,102,2) :
#                   myEvenRange.append([loopIndex])
#               print myEvenRange
#       

# 3. How do you exit a loop?
#    [Answer]:  break -  is the command to exit a loop
#     Note, these are alternatives to exiting whole code module execution -
#         sys.exit("text_msg_arg") - exits module exection and allows
#                  a text message argument for custom messages.
#         os._exit(n) - this method in Python is used to exit the process
#                  with specified status without calling cleanup handlers, 
#                  flushing stdio buffers, etc.
#             Note: This method is normally used in a child process
#                   after an os.fork() system call. The standard way of exiting
#                   the process is sys.exit(n) method.
#         exit() - Requires the site.py module to be imported.
#                  It exits module execution and uses raise the SystemExit
#                  exception by which the Python interpreter exits and no
#                  stack traceback is printed. Performing a print exit()
#                  presents a message to the user.  Considered best used for
#                  troubleshooting and development but not in production code.       
#         quit() - Requires the site.py module to be imported.
#                  It exits module execution and uses raise the SystemExit
#                  exception by which the Python interpreter exits and no
#                  stack traceback is printed. Performing a print exit()
#                  presents a message to the user.  Considered best used for
#                  troubleshooting and development but not in production code.
#-------------
# Sample Code:
#-------------
#myEvenRange = []
#myRange = []
#for loopIndex in range(2,102,2) :
#    myEvenRange.append(loopIndex)
#    myRange += [loopIndex]
#    print loopIndex
    
#    if (loopIndex >= 50):
#        print "Try to exit or quit the loop using the 'break' command."
#        break
        
#print "myEvenRange using .append() methods: \n", myEvenRange
#print "myRange using +=[] technique: \n", myRange

#**********
#EXCERCISE:  ReceiptEntry program
#**********
# Rewrite the receipt script from the previous hour to be a bit easier to use by
# making use of "iteration and list iteration methods".
#     a) The waiter should be able to input a receipt value for each seat,
#     b) and the script should print out the total for all of the seats.
# Note:  there was no receipt program in the previous hour.  There was one in
#        Chapther 2.
#     c) Extra credit - allow the waiter to go back and null out the last entry
#                       and re-enter the last seat entry.
#        
# see the book for an example of the output.
#
def ReceiptEntry():
    total = 0
    seatBill= [0]
    entry = "True"
    seat = 1
    # Note:  put the Receipt total of all seats in the seatBill[0] position.
    print "default entry: ", entry, "!!!"
    while not(entry in ["q", "quit"]):
        entry = raw_input("Enter the cost of the meal for Seat#" + str(seat) + " or ('q'=quit, 'b'=backup):\n")
        try:
            seatBill.append(float(entry))
            seatBill[0] = seatBill[0] + seatBill[seat]
            seat += 1
            print seatBill
        except ValueError:
            if (entry in ['r', 'reenter', 'b', 'back']):
                seat -= 1
                seatBill[0] = seatBill[0] - seatBill[seat]
                del seatBill[seat]
                print seatBill
            elif not(entry in ['q', 'quit']):
                print "Invalid entry, TRY AGAIN using format #.##, 'q', or 'b.'"

    print "The table receipt Total = " + str(seatBill[0])
    print seatBill
         
