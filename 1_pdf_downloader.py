import urllib2

"""
This is a simple pdf downloader for grabbing
a bunch of public pdfs. Very useful when
manually opening and clicking "Save as" on
multiple files is more of a hustle than writing
24 lines of python. :)

There are 19 pdfs to be downloaded.

The format of the URL where the pdf resides is:
http://www.aa.bb.co.uk/foo/bar/soft-eng/lect05.pdf

and the downloaded files will be saved with the same name as contained
in the section after the last forward slash.
"""

def main():

    for i in range(19):
        j = i+1
        if j < 10:
            index = "0"+str(j)
        else:
            index = str(j)
        download_file("http://www.aa.bb.co.uk/foo/bar/soft-eng/lect" + index + ".pdf", index)

def download_file(file_url, index):
    #get the file
    response = urllib2.urlopen(file_url)

    ## name of the file to save the pdf as.
    file_name = "soft_eng_lect_"+ index + ".pdf"

    #write contents to disk
    file = open(file_name, 'w')
    file.write(response.read())
    file.close()
    print("Lecture " + index + ": Complete")

if __name__ == "__main__":
    main()
