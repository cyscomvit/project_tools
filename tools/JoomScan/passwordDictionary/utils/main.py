from JoomScan.passwordDictionary.utils.parser import parse
import sys
import http.client
import requests
import argparse
from bs4 import BeautifulSoup
import threading
import time
pwd = ["password","123456","admin"]
def load_component():
    with open("comptotestdb.txt", "r") as f:
        for line in f:
            dbarray.append(line[:-1]) if line[-1] == "\n" else dbarray.append(line)


def check_url(url, path="/"):
    fullurl = url + path
    try:
        conn = requests.get(fullurl, headers=useragentdesktop, timeout=timeoutconnection)
        if conn.headers["content-length"] != "0":
            return conn.status_code
        else:
            return 404
    except StandardError:
        return None


def check_url_head_content_length(url, path="/"):
    fullurl = url + path
    try:
        conn = requests.head(fullurl, headers=useragentdesktop, timeout=timeoutconnection)
        return conn.headers["content-length"]
    except StandardError:
        return None


def check_readme(url, component):
    if check_url(url, "/components/" + component + "/README.txt") == 200:
        print("\t README file found \t > " + url + "/components/" + component + "/README.txt")

    if check_url(url, "/components/" + component + "/readme.txt") == 200:
        print("\t README file found \t > " + url + "/components/" + component + "/readme.txt")

    if check_url(url, "/components/" + component + "/README.md") == 200:
        print("\t README file found \t > " + url + "/components/" + component + "/README.md")

    if check_url(url, "/components/" + component + "/readme.md") == 200:
        print("\t README file found \t > " + url + "/components/" + component + "/readme.md")

    if check_url(url, "/administrator/components/" + component + "/README.txt") == 200:
        print("\t README file found \t > " + url + "/administrator/components/" + component + "/README.txt")

    if check_url(url, "/administrator/components/" + component + "/readme.txt") == 200:
        print ("\t README file found \t > " + url + "/administrator/components/" + component + "/readme.txt")

    if check_url(url, "/administrator/components/" + component + "/README.md") == 200:
        print("\t README file found \t > " + url + "/administrator/components/" + component + "/README.md")

    if check_url(url, "/administrator/components/" + component + "/readme.md") == 200:
        print ("\t README file found \t > " + url + "/administrator/components/" + component + "/readme.md")


def check_license(url, component):
    if check_url(url, "/components/" + component + "/LICENSE.txt") == 200:
        print("\t LICENSE file found \t > " + url + "/components/" + component + "/LICENSE.txt")

    if check_url(url, "/components/" + component + "/license.txt") == 200:
        print ("\t LICENSE file found \t > " + url + "/components/" + component + "/license.txt")

    if check_url(url, "/administrator/components/" + component + "/LICENSE.txt") == 200:
        print("\t LICENSE file found \t > " + url + "/administrator/components/" + component + "/LICENSE.txt")

    if check_url(url, "/administrator/components/" + component + "/license.txt") == 200:
        print ("\t LICENSE file found \t > " + url + "/administrator/components/" + component + "/license.txt")

    if check_url(url, "/components/" + component + "/" + component[4:] + ".xml") == 200:
        print("\t LICENSE file found \t > " + url + "/components/" + component + "/" + component[4:] + ".xml")

    if check_url(url, "/administrator/components/" + component + "/" + component[4:] + ".xml") == 200:
        print ("\t LICENSE file found \t > " + url + "/administrator/components/" + component + "/" + component[
                                                                                                     4:] + ".xml")


def check_changelog(url, component):
    if check_url(url, "/components/" + component + "/CHANGELOG.txt") == 200:
        print ("\t CHANGELOG file found \t > " + url + "/components/" + component + "/CHANGELOG.txt")

    if check_url(url, "/components/" + component + "/changelog.txt") == 200:
        print ("\t CHANGELOG file found \t > " + url + "/components/" + component + "/changelog.txt")

    if check_url(url, "/administrator/components/" + component + "/CHANGELOG.txt") == 200:
        print ("\t CHANGELOG file found \t > " + url + "/administrator/components/" + component + "/CHANGELOG.txt")

    if check_url(url, "/administrator/components/" + component + "/changelog.txt") == 200:
        print ("\t CHANGELOG file found \t > " + url + "/administrator/components/" + component + "/changelog.txt")


def check_mainfest(url, component):
    if check_url(url, "/components/" + component + "/MANIFEST.xml") == 200:
        print ("\t MANIFEST file found \t > " + url + "/components/" + component + "/MANIFEST.xml")

    if check_url(url, "/components/" + component + "/manifest.xml") == 200:
        print ("\t MANIFEST file found \t > " + url + "/components/" + component + "/manifest.xml")

    if check_url(url, "/administrator/components/" + component + "/MANIFEST.xml") == 200:
        print ("\t MANIFEST file found \t > " + url + "/administrator/components/" + component + "/MANIFEST.xml")

    if check_url(url, "/administrator/components/" + component + "/manifest.xml") == 200:
        print("\t MANIFEST file found \t > " + url + "/administrator/components/" + component + "/manifest.xml")


def check_index(url, component):
    if check_url_head_content_length(url, "/components/" + component + "/index.htm") == 200 and check_url_head(url,
     "/components/" + component + "/index.htm") > 1000:
        print("\t INDEX file descriptive found \t > " + url + "/components/" + component + "/index.htm")

    if check_url_head_content_length(url, "/components/" + component + "/index.html") == 200 and check_url_head(url,
                                                                                                                "/components/" + component + "/index.html") > 1000:
        print("\t INDEX file descriptive found \t > " + url + "/components/" + component + "/index.html")

    if check_url_head_content_length(url,
                                     "/administrator/components/" + component + "/INDEX.htm") == 200 and check_url_head(
        url, "/administrator/components/" + component + "/INDEX.htm") > 1000:
        print ("\t INDEX file descriptive found \t > " + url + "/administrator/components/" + component + "/INDEX.htm")

    if check_url_head_content_length(url,
                                     "/administrator/components/" + component + "/INDEX.html") == 200 and check_url_head(
        url, "/administrator/components/" + component + "/INDEX.html") > 1000:
        print ("\t INDEX file descriptive found \t > " + url + "/administrator/components/" + component + "/INDEX.html")


def index_of(url, path="/"):
    fullurl = url + path
    try:
        page = requests.get(fullurl, headers=useragentdesktop, timeout=timeoutconnection)
        soup = BeautifulSoup(page.text, "html.parser")
        if soup.title:
            titlepage = soup.title.string
            if (titlepage and "Index of /" in titlepage):
                return True
            else:
                return False
        else:
            return False
    except:
        return False


def scanner(url, component):
    if check_url(url, "/index.php?option=" + component) == 200:
        print ("Component found: " + component + "\t > " + url + "/index.php?option=" + component)

        check_readme(url, component)

        check_license(url, component)

        check_changelog(url, component)

        check_mainfest(url, component)

        check_index(url, component)

        if index_of(url, "/components/" + component + "/"):
            print ("\t Explorable Directory \t > " + url + "/components/" + component + "/")

        if index_of(url, "/administrator/components/" + component + "/"):
            print("\t Explorable Directory \t > " + url + "/administrator/components/" + component + "/")

    elif check_url(url, "/components/" + component + "/") == 200:
        print("Component found: " + component + "\t > " + url + "/index.php?option=" + component)
        print("\t But possibly it is not active or protected")

        check_readme(url, component)

        check_license(url, component)

        check_changelog(url, component)

        check_mainfest(url, component)

        check_index(url, component)

        if index_of(url, "/components/" + component + "/"):
            print ("\t Explorable Directory \t > " + url + "/components/" + component + "/")

        if index_of(url, "/administrator/components/" + component + "/"):
            print ("\t Explorable Directory \t > " + url + "/administrator/components/" + component + "/")

    elif check_url(url, "/administrator/components/" + component + "/") == 200:
        print ("Component found: " + component + "\t > " + url + "/index.php?option=" + component)
        print ("\t On the administrator components")

        check_readme(url, component)

        check_license(url, component)

        check_changelog(url, component)

        check_mainfest(url, component)

        check_index(url, component)

        if index_of(url, "/administrator/components/" + component + "/"):
            print ("\t Explorable Directory \t > " + url + "/components/" + component + "/")

        if index_of(url, "/administrator/components/" + component + "/"):
            print ("\t Explorable Directory \t > " + url + "/administrator/components/" + component + "/")

    pool.release()



def Joomscan(a):
	load_component()

	hello()

	try:
		parser = argparse.ArgumentParser()
		parser.add_argument("-u", "--url", action="store", dest="url", help="The Joomla URL/domain to scan.")
		parser.add_argument("-t", "--threads", action="store", dest="threads",
							help="The number of threads to use when multi-threading requests (default: 10).")
		parser.add_argument("-v", "--version", action="version", version="%(prog)s " + swversion)

		arguments = parser.parse_args()
	except:
		sys.exit(1)

	if arguments.url:
		url = arguments.url
		if url[:8] != "https://" and url[:7] != "http://":
			print("You must insert http:// or https:// procotol\n")
			sys.exit(1)


		if url[-1:] is "/":
			url = url[:-1]
	else:
		print("")
		parser.parse_args(["-h"])
		sys.exit(1)

	concurrentthreads = 10
	global pool
	if arguments.threads and arguments.threads is int:
		concurrentthreads = arguments.threads
		pool = threading.BoundedSemaphore(concurrentthreads)
	else:
		pool = threading.BoundedSemaphore(concurrentthreads)


	if check_url(url) != 404:

		if check_url(url, "/robots.txt") == 200:
			print("Robots file found: \t \t > " + url + "/robots.txt")
		else:
			print("No Robots file found")

		if check_url(url, "/error_log") == 200:
			print("Error log found: \t \t > " + url + "/error_log")
		else:
			print("No Error Log found")

		# Inizio la scansione dei componenti

		print("\nStart scan...with %d concurrent threads!" % concurrentthreads)

		for component in dbarray:
			# Thread Pool
			pool.acquire(blocking=True)

			t = threading.Thread(target=scanner, args=(url, component,))
			t.start()

		while (threading.active_count() > 1):
			time.sleep(0.1)

		print("End Scanner")

	else:
		print("Site Down, check url please...")


if __name__ == "__main__":
	main(sys.argv[1:])