# -*- coding: utf-8 -*-
"""
Created on Tue May  5 15:39:55 2020

@author: Jeff
edited: 05/07/2020 - Yu-Gene Chen
        1. Added remDuplicates()
        2. Added 1-liner code to remove duplicates from parts (isntead of
           calling the remDuplicates() ).
        3. Added comments and generally edited to conform to PEP8 standard.
        4. Edited to make getting info between two tags on an html page work.
           Actually, instead of getting text between two, I get all DIV of a
           after an anchor.  You could also modify it to get all 'text' after
           an anchor.
        5. Good reference is https://www.w3schools.com/xml/xpath_syntax.asp
"""

#############################
#  Functions
#############################


def remDuplicates(myList):
    '''
    #** ***************************\n
    #** Remove Duplicates in a list\n
    #** ***************************\n
    INPUTS:
            myList - list object
    OUTPUTS:
       returns the updated list (i.e. without duplicates)

    Created on Tue May  6 20:03:55 2020
    @author: Yu-Gene Chen
    '''
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
    ''' Print out the text of each WebElement contined in a list.

INPUTS:
    \twebEl_list - list WebElements
    \n\tvarName    - optional input, name of the variable being fed into this function.
    \n\tScreenPrint - optional input, True prints to screen, False does not.
OUTPUTS:
    \tScreenPrint = True:  prints string contents of each WebElement
    \n\treturns text list of the WebElement.text
-----------------------------------\n
Created on Tue May  6 20:03:55 2020\n
@author: Yu-Gene Chen
    '''
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


def Create_TOCDict(tocAnchorList):
    """Create a Table of Contents (toc) dictionaary from a table of contents
    Anchor_ID list.  Take the toc list of Anchor IDs and pair them with
    the proper text text that goes with each ID to create the dictionary.

INPUTS:
------
    :tocAnchorList (list): Anchor_ID list for each item in the table of \
                           contents.
OUTPUTS:
    :return (dict): dictionary, where the toc anchorIDs are the keys and the
                    text title of each toc item is the definition (or value).
-----------------------------------\n
Created on Tue May  6 20:03:55 2020\n
@author: Yu-Gene Chen
    Created on Sun May 31 13:27:46 2020
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



#############################
#
# *** MAIN Program
# ===================================================
def main():
    print("Hello World!")


# ===================================================

if __name__ == "__main__":
    # [Test #1] Test the kitchen classes:  Ingredient(), Recipe(), Inventory()
    # from classes.ingredients import Ingredient
    # from classes.recipes import Recipe
    main()

# --- Write Scripts below here ---

    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import os
    import time
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.common.by import By
    import selenium.webdriver.support.ui as ui
    import selenium.webdriver.support.expected_conditions as EC
    from selenium.webdriver.common.action_chains import ActionChains


    # driver = webdriver.Chrome('/path/to/chromedriver')
    # Note: the above is not just the path but thef full filename path of
    #       chromedrive.exe (without the ".exe").
    # Optional argument, if not specified will search path.
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    prefs = {'download.default_directory':r'C:\Users\Lifygen\projects\python\Downloads'}
    options.add_experimental_option('prefs', prefs)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    chromedriver = dir_path + "/ChromDriver/chromedriver83"
    os.environ["webdriver.chrome.drive"] = chromedriver
    driver = webdriver.Chrome(options=options, executable_path=chromedriver)

    # User Input Data.
    ticker = input('Input the company stock symbol that you\'d like to look ' +
                   'up the latest (2020) "DEF 14A" filing.')
    if not ticker:
        ticker = 'AAPL'
    year = "2020"
    form = "DEF 14A"

    # Open the EDGAR SEC Search Page.
    url = "https://www.sec.gov/edgar/searchedgar/companysearch.html"
    # Go to Website
    driver.get(url)
    # Wait a little to let the webpage come up before trying to manipulate the
    # objects on the EDGAR SEC page.
    time.sleep(1)
    # Enter Ticker into Search Bar and hit search.
    e = driver.find_element_by_id("cik")
    e.send_keys(ticker)
    s = driver.find_element_by_id("cik_find").click()
    time.sleep(1)
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
    # driver.find_elements_by_id("documentsbutton").click()

    # Example of Full Xpaths, use Google Chrome > Inspect > Copy > Full Xpath
    # /html/body/div[4]/div[4]/table/tbody/tr[5]/td[2]/a
    # /html/body/div[4]/div[4]/table/tbody/tr[2]/td[2]/a
    time.sleep(1)
    # Go to HTML version of document.
    L = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/table/" +
                                     "tbody/tr[2]/td[3]/a"
                                     ).click()
    # /html/body/div[4]/div[2]/div/table/tbody/tr[2]/td[3]/a
    time.sleep(1)
    anchor = driver.find_elements_by_css_selector("a")
    parts = [x.get_attribute('name') for x in anchor]
    # Filter out blanks
    parts = list(filter(None, parts))
    # Remove duplicate entries
    #parts = list(dict.fromkeys(parts))
    parts = remDuplicates(parts)

    #content = driver.find_elements_by_xpath("//*[./preceding-sibling::a[.= '"+parts[52]+"']][./following-sibling::a[.= '"+parts[53]+"']]")
    begPart = parts[38]
    endPart = parts[39]

    content = driver.find_elements_by_xpath(
                       "//a[@name='toc799303_37']/following::*"
                       )
    content1 = driver.find_elements_by_xpath("//a[@name='toc799303_37']/following::*")
    content2 = driver.find_elements_by_xpath("//a[@name='toc799303_38']/preceding::*")
#content1 = driver.find_elements_by_xpath("//a[@name='toc799303_37']/following::*")
#              "//body[./preceding-sibling::a[@name='" + BegPart + "']]" +
#              "[a[@name='" + EndPart + "']]"
#              )

    # "//*[./preceding-sibling::a[.= '"+parts[52]+"']][./following-sibling::a[.= '"+parts[56]+"']]"

# *** Do NOT forget to close the DRIVER !!! ***
#   driver.quit()

# *****   Begin test *****
    # Gets all the <DIV>s where Anchor is located to end of document;
    contentProp4 = driver.find_elements_by_xpath(
              "//*[@name='toc799303_37']/following::div"
              )
    i = 0
    for each in contentProp4:
        if "RESOLVED" in each.text:
            print("Resolved was found in WebElement {}.".format(i))
    i += 1
    print("Printing out, contents of <contentProp4>:\n")
    printWebEl(contentProp4, "contentProp4", True)

# *****   end this test *****

# *****
# Fix this later, develop code to get text of the TOC and search
# for keywords in the title
# *****
#    i = 0
#    for each in parts:
#        if "holder" in each:
#            print("'holder' was found in WebElement {}.".format(i))
#            print("Printing out, contents of <content>:\n")
#            i += 1
# *****   end this test *****



# *****************
# Get Proposals 4_6
# *****************
tocDict = Create_TOCDict(parts)

# contentAnchor returns the DIV contents where the Anchor Resides.
contentAnchor = driver.find_elements_by_xpath(
              "//a[@name='toc799303_37']/ancestor::div")
printWebEl(contentAnchor,"contentAnchor", True)

# contentProp4_6 gets all DIV contents after the defined Anchor
# (1st page is a partial duplicate; it is just missing the title)
contentProp4_6 = driver.find_elements_by_xpath(
              "//*[contains(@name,'toc799303_37')]/following::div"
              )
contentProp4_6 = contentAnchor + contentProp4_6

# equivalent to "contentProp4_6 = contentAnchor + contentProp4_6"
cmyAllChp = driver.find_elements_by_xpath(
    "//a[contains(@name,'toc799303_37')]/ancestor::div|//*[contains(@name,'toc799303_37')]/following::div"
    )
printWebEl(cmyAllChp,"cmyAllChp", True)

# Test to get just get chpaters with "RESOLVED" in it.  Note: this ends up only
# getting the Divisions with the words "Resolve" in it.
cAllChp = driver.find_elements_by_xpath(
    "//div[contains(.,'RESOLVED')]")
printWebEl(cAllChp,"cAllChp", True)

cAllChp = driver.find_elements_by_xpath(
    "//div[contains(.,'Proposal No. 4')]")
printWebEl(cAllChp,"cAllChp", True)



cmyAllChp = driver.find_elements_by_xpath(
    "//a[@name='toc799303_37']/ancestor::div and //*[contains(@name,'toc799303_37')]/following::div")
printWebEl(cmyAllChp,"cmyAllChp", True)



c1Chp = driver.find_elements_by_xpath(
    "//*[following-sibling:://a[contains(@name='toc799303_38')]/ancestor::div and " +
    "[preceding-sibling::img [contains(@name='toc799303_37')/ancestor::div]]")
printWebEl(c1Chp,"c1Chp", True)

# //order[preceding-sibling::order[@orderNumber="2"] and following-sibling::order[@orderNumber="3"]]
# And alternatively:
# //*[following-sibling::order[@orderNumber="3"] and preceding-sibling::order[@orderNumber="2"] ]
# works for Test.xml

# //*[preceding-sibling::img [@src="uniqueUrl1"] and following-sibling::img [@src="uniqueUrl2"]]
# works for Test3.xml

c2 = driver.find_elements_by_xpath(
    "//*[preceding:://div/p/a[@name='toc799303_37']/ancestor::div and " +
    "following:://div/p/a[contains(@name='toc799303_38')]]")
printWebEl(c2,"c2", True)




c1 = driver.find_elements_by_xpath(
    "//p[preceding::a[@name='toc799303_37']/ancestor::div]")
printWebEl(c1,"c1", True)

c2 = driver.find_elements_by_xpath(
    "//p[following::a[@name='toc799303_38']/ancestor::div]")
printWebEl(c2,"c2", True)

# Gets all paragraphs between two nodes
c1Chp = driver.find_elements_by_xpath(
    "//p[following::a[@name='toc799303_38']/ancestor::div and " +
    "preceding::a[@name='toc799303_37']/ancestor-or-self::div]")
printWebEl(c1Chp,"c1Chp", True)

#Gets all Divisions between to nodes
c1Chp = driver.find_elements_by_xpath(
    "//div[following::a[@name='toc799303_38']/ancestor-or-self::div and " +
    "preceding::a[@name='toc799303_37']/ancestor-or-self::div]")
printWebEl(c1Chp,"c1Chp", True)



# These two examples get the correct text

#Gets 1 whole chapter (in this case Chapter for Proposal 3 w/o duplicated text)
c1Chp = driver.find_elements_by_xpath(
    "//a[@name='toc799303_37']/ancestor::center|" +
    "//Center[preceding::a[@name='toc799303_37']/ancestor-or-self::Center  and " +
    "following::a[@name='toc799303_38']/ancestor-or-self::p]")
printWebEl(c1Chp,"c1Chp", True)

#Gets 1 whole chapter (in this case Chapter for Proposal 3 w/o duplicated text)
c1Chp = driver.find_elements_by_xpath(
    "//a[@name='toc799303_37']/ancestor::p|" +
    "//p[preceding::a[@name='toc799303_37']/ancestor-or-self::p  and " +
    "following::a[@name='toc799303_38']/ancestor-or-self::p]")
printWebEl(c1Chp,"c1Chp", True)






# order[item/text()='food']

c1 = driver.find_elements_by_xpath(
    "//a[@name='toc799303_37']/ancestor::center")
printWebEl(c1,"c1", True)




# "//*[contains(@name,'toc799303')]/ancestor::p"

# "//div[contains(@name,'toc799303')]/(self::div, following-sibling::div)"

contentProp4_6 = contentAnchor + contentProp4_6

# Remove blank lines (records with all spaces and null records)
length = len(contentProp4_6)
for i in range((length-1), -1, -1):
    myStr = contentProp4_6[i].text
    if ((myStr.rstrip() == "") or (contentProp4_6[i].text == [])):
        contentProp4_6.remove(contentProp4_6[i])

# Remove duplicated texts in the chapters (i.e. proposals)
highLimit = len(contentProp4_6)-1
for i in range(highLimit, 0, -1):
    # Check to see if the length has shrunk from removals
    if i >= len(contentProp4_6):
        break
    for j in range(1, 6):
        k = i - j
        if k < 0:
           k = 0
        if contentProp4_6[i].text in contentProp4_6[k].text:
           contentProp4_6.remove(contentProp4_6[i])
           break
        #print("i= ", i, "k=", k)
        j += 1
    i += 1


# Create Chapters (sorting through looking for the tocTitles merging DIV aka
'''
    # TBD - Create a Text list of Chapters
    #1] WebElements until the next tocTitle is found and break into the next chapter)
    #2] make RESOLVED search into a function.
    #3] How to formulate an XPATH range request.
'''
i = 0
for each in contentProp4_6:
    trialTxt = each.text
    if "RESOLVED".lower() in trialTxt.lower():
        print("Resolved was found in WebElement {}.".format(i))
    i += 1

# Store to Text variable

contentProp4_6_text = printWebEl(contentProp4_6, "contentProp4_6", True)
len(contentProp4_6)


# Handy code to run as a script
contentProp4_6 = contentAnchor + contentProp4_6
printWebEl(contentProp4_6, "contentProp4_6", True)
printWebEl(contentAnchor, "contentAnchor", True)

#Close the Driver
    #driver.quit()














