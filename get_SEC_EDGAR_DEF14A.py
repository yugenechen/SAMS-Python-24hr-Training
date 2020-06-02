# -*- coding: utf-8 -*-
"""
Created on Sun May 31, 2020

@authors: Jeff Sherman & Yu-Gene Chen
edited: 05/07/2020 -
        1.  Good reference is https://www.w3schools.com/xml/xpath_syntax.asp
        2.  Retrieves SEC EDGAR "DEF 14A" filing info for specified company.
            Just call get_SEC_EDGAR_DEF14A(ticker="").  if no ticker is \
            supplied then the program will solicit the user for an input from
            the console command line.
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import sys
from termcolor import colored, cprint

#############################
#  Functions
#############################


def remDuplicates(myList):
    """Removes Duplicates in a list.

    INPUTS:
    -----
    :myList (list): - the input list object that will have duplicates removed.

    OUTPUTS:
    -----
        :return (list): the updated list with duplicates removed.

    Created on Tue May  6 20:03:55 2020
    @author: Yu-Gene Chen
    """
    for eachItem in myList:
        # Count the duplicate items.
        itemDuplicates = myList.count(eachItem)
        # Loop through the duplicate items and <list>.remove them.
        for i in range(1, itemDuplicates):
            myList.remove(eachItem)
    return myList
    # OR comment all the above and do the following,
    #    a. Cast list as a <dict> using list items as keys, this elliminates
    #       duplicate items because keys have to be unique.
    #    b. Re-cast back to <list> OR <dict>.keys returns a list of keys:
    #return list(dict.fromkeys(myList))

def printWebEl(webEl_list,varName="WebElement",ScreenPrint=False, myReturn=False):
    """Print out the text of each WebElement contined in a list.

    INPUTS:
    -----
    :webEl_list (list): list of Web Elements
    :varName (str): optional input, name of the variable being fed into this f(x).
    :ScreenPrint (bool): optional input,
                     True prints to screen,
                     False (default) does not print to screen.
    :myReturn (bool): optional input,
                  True, generates a return value
                  False, no value is returned by the fucntion call

    OUTPUTS:
    -----
    :ScreenPrint = True:  prints string contents of each WebElement
    :returns text list of the WebElement.text
    -----
    Created on Tue May  6 20:03:55 2020\n
    @author: Yu-Gene Chen
    """
    i = 0
    textList=[]
    if ScreenPrint:
            print("\n**************************************" +
                  "\nPrinting out, <{}> contents:".format(varName) +
                  "\n**************************************")
    for each in webEl_list:
        if ScreenPrint:
            print("======================================\n" +
                  " {} [WebElement {}].".format(varName, i) + "\n" +
                  "======================================")
            print(webEl_list[i].text)
        textList.append(webEl_list[i].text)
        i += 1
    if myReturn:
        return textList


def Create_TOCDict(tocAnchorList, driver):
    """Create a Table of Contents (toc) dictionaary from a table of contents
    Anchor_ID list.  Take the toc list of Anchor IDs and pair them with
    the proper text text that goes with each ID to create the dictionary.

    INPUTS:
    ------
    :tocAnchorList (list): Anchor_ID list for each item in the table of \
                           contents.
    OUTPUTS:
    -----
    :return (dict): dictionary, where the toc anchorIDs are the keys and the \
                    text title of each toc item is the definition (or value).
    -----------------------------------\n
    Created on Tue May  6 20:03:55 2020\n
    @author: Yu-Gene Chen
    """
# Create a TOC dictionary {tocCode:tocTitle}
    i = 0
    toc = {}
    for each in tocAnchorList:
        # Gets the TEXT TITLEs of the table of contents items
        TocTitle = driver.find_elements_by_xpath(
                "//a[contains(@name,'" + each + "')]/ancestor::p")
        toc[each] = TocTitle[0].text
        i += 1
    return toc



#############################
#
# *** MAIN Program
# ===================================================
def get_SEC_EDGAR_DEF14A(ticker=""):
    """Gets company ""DEF 14A" filings and captures table of contents chapters.

    INPUT:
    -----
    :ticker (str): - the stock ticker symbol for the company you'd like to \
                     retrieve "DEF 14A" info from.

    OUTPUT:
    -----
    :return (tuple): - a tuple of (tocDict, tocChapters, keyWordFound),

    WHERE:
    -----
    :toDict (dict): - a dictionary of the Table of Contents with the tocIDs as \
                     the keys and the toc_text as the value.
    :tocChapters (dict): - a dictionary of text of the chapters making up each \
                          Table of Contents subject.  The tocIDs are used as \
                          the keys
    :keyWordsFound (dict): - a dictionary of lists of keywords found in each \
                            chapter.  The tocIDs are used as the keys.  The \
                            values are formatted as:
                             - [<tockID index#>, <tocText>, \
                                     *<one or more matching keywords>].
                             - No key entry is made if there were no \
                                    keyword matches.
        Note:  Maybe should drop <tocID index#> from the list of info since I \
               calculate but do not deliver the tocText list.  The tocText \
               list is generated in the Create_TOCDict() function.
    """
    print("Hello World!")
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import os
    import time
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.common.by import By
    import selenium.webdriver.support.ui as ui
    import selenium.webdriver.support.expected_conditions as EC
    from selenium.webdriver.common.action_chains import ActionChains
    from termcolor import colored, cprint


    # driver = webdriver.Chrome('/path/to/chromedriver')
    # Note: the above is not just the path but thef full filename path of
    #       chromedrive.exe (without the ".exe").
    # Optional argument, if not specified will search path.
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    prefs = {'download.default_directory':
             r'C:\Users\Lifygen\projects\python\Downloads'}
    options.add_experimental_option('prefs', prefs)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    chromedriver = dir_path + "/ChromDriver/chromedriver83"
    os.environ["webdriver.chrome.drive"] = chromedriver
    driver = webdriver.Chrome(options=options, executable_path=chromedriver)

    # User Input Data if not ticker was passed in intial call.
    iText = colored("[Input Ticker]:", 'red', attrs=['bold', 'underline'])
    CursorText = colored(" <-{: ", 'red', 'on_yellow', attrs=[ 'bold'])
    msgText = colored("Input a company stock symbol to " +
                      "look up their latest (2020) \"DEF 14A\" filing.\n" +
                      "(Note:  defaults to \"AAPL\" if [Enter] " +
                      "without any ticker.)\n",
                      'magenta'
                      )
    if not ticker:
        ticker = input(msgText + iText + CursorText)

        if not ticker:
            # If still no ticker then use Apple's ticker
            ticker = 'AAPL'
    # Placeholder initial values in case the code is used to scrape other forms.
    year = "2020"
    form = "DEF 14A"

    # Open the EDGAR SEC Search Page.
    url = "https://www.sec.gov/edgar/searchedgar/companysearch.html"
    # Go to EDGAR SEC Website
    driver.get(url)
    # Wait a little to let the webpage come up before trying to manipulate the
    # objects on the EDGAR SEC page.
    time.sleep(10)
    # Enter Ticker into Search Bar and hit search.
    e = driver.find_element_by_id("cik")
    e.send_keys(ticker)
    s = driver.find_element_by_id("cik_find").click()
    time.sleep(15)
    # Search for the form that you are looking for, set to 100 Entries per page
    # and hit [enter].
    c = driver.find_element_by_xpath("/html/body/div[4]/div[2]/form/table" +
                                     "/tbody/tr/td[5]/select/option[5]"
                                     ).click()
    t = driver.find_element_by_id("type").send_keys(form)
    time.sleep(1)
    a = ActionChains(driver)
    a.send_keys(Keys.RETURN)
    a.perform()
    time.sleep(1)

    #######################################
    # ** Will need to insert logic here **#
    # ** to determine which button to   **#
    # ** press based on the year input  **#
    #######################################
    # Right now it will just bring you to the most recent document.

    # This gets the first button with ID "documentsbutton" will have to use
    # xpath to get the other buttons.
    driver.find_element_by_id("documentsbutton").click()
    time.sleep(1)
    # Go to HTML version of document.
    L = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/table/" +
                                     "tbody/tr[2]/td[3]/a"
                                     ).click()
    # /html/body/div[4]/div[2]/div/table/tbody/tr[2]/td[3]/a
    time.sleep(1)
    anchor = driver.find_elements_by_css_selector("a")
    tocID = [x.get_attribute('name') for x in anchor]
    # Filter out blanks
    tocID = list(filter(None, tocID))
    # Remove duplicate entries
    #tocID = list(dict.fromkeys(tocID))
    tocID = remDuplicates(tocID)
# *****************
# Get all chapters based on headings or keys in the toc
# *****************
    # Create toc dictionary
    tocDict = Create_TOCDict(tocID, driver)
    #Get whole chapters (in this case Chapter for Proposal 3 w/o duplicated text)
    tocChapters={}
    for i in range(len(tocID)):
        if (i < len(tocID)-1):
            c1Chp = driver.find_elements_by_xpath(
                "//a[@name=tocID[i]]/ancestor::p|" +
                "//p[preceding::a[@name='" + tocID[i] + "']/ancestor-or-self::p  and " +
                "following::a[@name='" + tocID[i+1] + "']/ancestor-or-self::p]")
            # pre-debugging checks
            #print("iterating on", i,":  ", tocID[i], "to", tocID[i+1])
        else:
            c1Chp = driver.find_elements_by_xpath(
                "//a[@name='" + tocID[i] + "']/ancestor::p|" +
                "//p[preceding::a[@name='" + tocID[i] + "']/ancestor-or-self::p]")
            # pre-debugging checks
            #print("Last record", i)
        paragraphList = printWebEl(c1Chp,"c1Chp", False, True)
        chapter = ""
        for paragraph in paragraphList:
            if paragraph.strip(" "):
                chapter += paragraph + "\n\n"
                if "|" in paragraph:
                    chapter += "\n\n"
        tocChapters.update({tocID[i]: chapter})
        # pre-debugging checks
        #print(chapter)
        #print(tocChapters[tocID[i]])

# *****
# Fix this later, develop code to get title text of the TOC and search
# for keywords in the title.  For now, this code just looks for keywords in
# the chapters.
# *****
    keyWordFound = {}
    checkList = ("holder", "propos", "vot", "resolved")
    i = 0
    for each in tocChapters:
        for checkWord in checkList:
           if checkWord in tocChapters[each].lower():
               # pre-debugging checks
               #print("'{}' was found in WebElement {}.".format(checkWord,i))
               #print("Printing out, contents of <content>:\n")
               if each in keyWordFound:
                   keyWordFound[each].append(checkWord)
               else:
                   keyWordFound.update({each: [i, tocDict[each], checkWord]})
        i += 1
    # pre-debugging checks
    #print(keyWordFound)
# *****   end this test *****

#Close the Driver
    driver.close()
    driver.quit()

    return (tocDict, tocChapters, keyWordFound)

# ===================================================

if __name__ == "__main__":
    DEF14A_Output = get_SEC_EDGAR_DEF14A()
    TocDict = DEF14A_Output[0]
    TocChpts = DEF14A_Output[1]
    KeyWordSearch =  DEF14A_Output[2]

    print("\n\n\n")
    text1 = colored("TocDict", 'magenta', attrs=['bold', 'underline'])
    print(text1 + " is the variable for the Table of Contents dictionary.")

    text2 = colored("TocChpts", 'green', attrs=['bold', 'underline'])
    print(text2 + " is the dictioanry variable holding the chapters.")

    text3 = colored("KeyWordSearch", 'cyan', attrs=['bold', 'underline'])
    print(text3 + " is the dictionary variable holding the results of the keyword search.")

    iText = colored("These variables are local variavles ready for your " +
                    "inspection. \nDEF14A_Output is the return tuple that " +
                    "is also a local variable ready for your use.",
                    'red', attrs=['bold'])
    print(iText)


# --- Write Scripts below here ---
