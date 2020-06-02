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


    # driver = webdriver.Chrome('/path/to/chromedriver')  # Optional argument, if not specified will search path.
    # driver.get('http://www.google.com/');
    # time.sleep(5) # Let the user actually see something!
    # search_box = driver.find_element_by_name('q')
    # search_box.send_keys('ChromeDriver')
    # search_box.submit()
    # time.sleep(5) # Let the user actually see something!
    # driver.quit()

    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    prefs = {'download.default_directory':r'C:\Users\Lifygen\projects\python\Downloads'}
    options.add_experimental_option('prefs', prefs)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    chromedriver = dir_path + "/chromedriver"
    os.environ["webdriver.chrome.drive"] = chromedriver
    #driver = webdriver.Chrome(chrome_options=options,
    #                          executable_path=chromedriver
    #                          )
    driver = webdriver.Chrome(options=options, executable_path=chromedriver)

    # User Input Data.
    ticker = "AAPL"
    year = "2020"
    form = "DEF 14A"

    # Main Company Search Page.
    url = "https://www.sec.gov/edgar/searchedgar/companysearch.html"

    # Go to Website
    driver.get(url)

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

    #c = driver.find_element_by_xpath("/html/body/div[4]/div[2]/form/table" +
    #                                 "/tbody/tr/td[5]/select/option[5]"
    #                                 ).click()
    # /html/body/div[4]/div[2]/form/table/tbody/tr/td[5]/select/option[5]

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
    #driver.quit()
    '''
    # *****
    # Yu-Gene Additions and EXPERIMENTS to reduce footpriNt of xpath call and
    # get just one anchor worth of data (i.e. one whole chapter)
    # *****
    '''
    # manually copied from the webbrowoser the AAPL_URL based on above query
    # then manually coded it into AAPL_URL here:
    # AAPL_URL = "https://www.sec.gov/Archives/edgar/data/320193/000119312520001450/d799303ddef14a.htm"
    # driver.get(url)
    # time.sleep(1)
# Above manually setting HTML does not work - connection is rejected.

    # Gets all the <DIV>s where Acnhor is located to end of document;
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

# *************
# experiment
# *************
    # Self - gets a blank because Self is the 'A' anchor object [I think]
    contentSelf = driver.find_elements_by_xpath(
              "//*[@name='toc799303_37']//self::div")
    printWebEl(contentSelf, "contentSelf", True)

    # Ancestor Gets the first page of the proposal, i.e. page with anchor
    # '/' allows children '//' no children
    #  '//ancestor' and '/ancestor yield same results'
    contentAncestor = driver.find_elements_by_xpath(
              "//a[@name='toc799303_37']//ancestor::div")
    printWebEl(contentAncestor, "contentAncestor", True)
    #//div = returns []
    #//* and //a both = returns the div text
    #//body = returns Anchor's <B> text; the toc title_text

    # contentAnchor returns the DIV contents where the Anchor Resides.
    # (does the same thing as <contentAncestor>)
    contentAnchor = driver.find_elements_by_xpath(
              "//a[@name='toc799303_37']/ancestor::div")
    printWebEl(contentAnchor, "contentAnchor", True)

    contentAncDiv = driver.find_elements_by_xpath(
              "//*[contains(@name,'toc799303_37')]/ancestor::div")
    test = printWebEl(contentAncDiv, "contentAncDiv")


    # Gets the TEXT TITLEs of the table of contents items
    contentTocTitle = driver.find_elements_by_xpath(
            "//*[contains(@name,'toc799303')]/ancestor::p"
            )
    test = printWebEl(contentTocTitle, "contentTocTitle")

    # Gets a single TEXT TITLE of a named table of contents item
    contentAncP = driver.find_elements_by_xpath(
              "//*[contains(@name,'toc799303_37')]/ancestor::p")
    test = printWebEl(contentAncP, "contentAncP", True)

    # Try another:Parent - gets the anchor TOC title
    contentParent = driver.find_elements_by_xpath(
           "//*[contains(@name,'toc799303_37')]/parent::*")
    test = printWebEl(contentParent, "contentParent"); test

# ** Failed Tests ** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
    # Explicitly get the TOC item (it is a <B> bold text within <p> paragraph)
# The following worked in ChromeDriverV81 but fails in ChromeDriverV83
#    contentB = driver.find_elements_by_xpath(
#            "//a[preceding-sibling::@name,'toc799303_37')]")
#    test = printWebEl(contentB,"contentB",True)

    #
    # Get a RANGE: Gets the ???? page of the proposal, i.e. page with anchor
    # with all children '/ancestor'
# Failes on ChromeDriverV83
#    contentRange1 = driver.find_elements_by_xpath(
#              "//*[./preceding-sibling::contains @name,'toc799303_37']/ancestor::div" +
#              "[./following-sibling::/a[@name='toc799303_38'/ancestor::div]"
#              )
#    test = printWebEl(contentRange1, "contentRange1")

    # //*[@class='featured-box']//*[text()='Testing']

    # Try another Range:
# Failes in Chrome 83
#    contentRange2 = driver.find_elements_by_xpath(
#           "[//*[(@name,'toc799303_37')]/ancestor::div][]")
#           "//a[@name='toc799303_37']//ancestor" +
#           "[./following-sibling:://a[@name='toc799303_38']"
#             )
#    test = printWebEl(contentRange2, "contentRange2")
    #Close the Driver
    #driver.quit()
# *****   end this experiment *****
# Fails on Chrome 83
#    printWebEl([contentRange1[0]])
#    printWebEl(contentRange1)

# get data between two nodes
#    contentRange3 = driver.find_elements_by_xpath(
#        "//a[preceding-sibling::/a[@name='toc799303_37']//ancestor::div]" +
#        "//a[following-sibling::/a[@name='toc799303_38']//ancestor::div]"
#        )
# test = printWebEl(contentRange3)

# Stackovervlow example:
# https://stackoverflow.com/questions/45966049/xpath-get-elements-that-are-between-2-elements-where-we-cant-use-an-id-or-text
# //a[preceding-sibling::b='Account Detail' and following-sibling::b]

# Working code that gets text between two nodes
# https://stackoverflow.com/questions/7957480/xpath-select-elements-between-two-nodes?rq=1
stackoverflow = driver.find_elements_by_xpath(
    "//tr[preceding-sibling::tr/td[@class = 'd2']]" +
    "[count(.|//tr[following-sibling::tr/td[@class = 'd2']])=" +
    "count(//tr[following-sibling::tr/td[@class = 'd2']])]")

# Example:              "//a[preceding-sibling::b[1]='Account Detail']"
contentRange4 = driver.find_elements_by_xpath(
    "//a[preceding-sibling::b='Proposal No. 4 – Shareholder Proposal' " +
    "and following-sibling::b]"
    )
test = printWebEl(contentRange4)

# "//*[contains(@name,'toc799303_37')]/parent::*"

# "//a[preceding-sibling:://b[contains(text(),'toc799303')]]"


contentTest = driver.find_elements_by_xpath("/html/head/title/text()")

# Instead of doing this tocCode 'toc799303' use the PARTS list or
# dictionary.
contentAllProposals = driver.find_elements_by_xpath(
              "//*[contains(@name,'toc799303')]/following::div"
              )
test = printWebEl(contentAllProposals, "contentAllProposals", True)

# *****************
# Get Proposals 4_6
# *****************
# Create a TOC dictionary {tocCode:tocTitle}
i = 0
toc = {}
for each in parts:
    # Gets the TEXT TITLEs of the table of contents items
    TocTitle = driver.find_elements_by_xpath(
            "//a[contains(@name,'" + each + "')]/ancestor::p")
    toc[each] = TocTitle[0].text
    i += 1

# contentAnchor returns the DIV contents where the Anchor Resides.
contentAnchor = driver.find_elements_by_xpath(
              "//a[@name='toc799303_37']/ancestor::div")
# contentProp4_6 gets all DIV contents after the defined Anchor
# (1st page is a partial duplicate; it is just missing the title)
contentProp4_6 = driver.find_elements_by_xpath(
              "//*[contains(@name,'toc799303_37')]/following::div"
              )
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














