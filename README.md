## Hola Cyber Security Enthusiasts!
![image](https://user-images.githubusercontent.com/54901460/135729420-128d8752-f992-4949-802c-658ebb68aef5.png)

We live in a world where we are bombarded with different scenarios and projects in our daily work life. Eventually, these variables affect us to the extent where productivity suffers at multiple levels. OWASP Projects are a collection of related tasks that have a defined roadmap and team members. Our projects are open source and are built by our community of volunteers - people just like you!.

Project Tools is one such project which consists of set of valuable and intriguing tools made exclusively for people interested in cyber security. It’s a fast-paced and always changing environment but we have the right tools for the job. Looking to begin your journey as a cybersecurity expert?? Don't worry, we've got you covered. The key is not a technical background, but your willingness and desire to learn how technology works and to never stop playing. Come on, let's go on an adventure together.

## Tools Available
1. Nmap - It is used to discover hosts and services on a computer network by sending packets and analyzing the responses.
2. Traceroute - It is a network diagnostic tool used to track in real-time the pathway taken by a packet on an IP network from source to destination, reporting the IP addresses of all the routers it pinged in between.
3. Nikto - It is web server scanner which performs comprehensive tests against web servers for multiple items, including over 6700 potentially dangerous files/programs, checks for outdated versions of over 1250 servers, and version specific problems on over 270 servers.

Tool Details have been provided in "More Info secton" of a particular tool.

## Notes
1. This application requires nmap map installed in your local system.
2. Clone the application in your system and run you need to run it as administrator(windows)/super user(linux).
3. You need pipenv library installed on your system.

## Steps for Standard Installation
Command Line (as administrator(windows)/super user(linux):
1. cd project_tools
2. pipenv install
4. cd Dashboard
5. export FLASK_APP = run
6. pipenv run flask run

Results are obtained in terminal/command line.

## Steps for Docker Installation
1. cd project_tools
2. docker build -t project_tools .
3. docker run -itd -p 5000:5000 project_tools

Open up your browser at http://localhost:5000/ You should see the Project tools home page.
