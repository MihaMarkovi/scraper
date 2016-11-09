from urllib import urlopen

from BeautifulSoup import BeautifulSoup


base_url = "https://scrapebook22.appspot.com/"

response = urlopen(base_url).read()


soup = BeautifulSoup(response)





# print(soup.html.head.title.string)
names = []
emails = []
cities = []

for link in soup.findAll("a"):
    if link.string == "See full profile":
        person_url = base_url + link["href"]
        person_html = urlopen(person_url).read()
        person_soup = BeautifulSoup(person_html)
        #najde podatek
        email = person_soup.find("span", attrs={"class": "email"})
        name = person_soup.find("div", attrs={"class": "col-md-8"}).h1.string
        city = person_soup.find("span", attrs={"data-city": True})
        #dodam stvari v TXT datoteko
        names.append(str(name.string))
        emails.append(str(email.string))
        cities.append(str(city.string))
print(names)
print(emails)
print(cities)

csv_file = open("persons_list.csv", "w")

csv_file.write(str(names) + "\n")

csv_file.write(str(emails) + "\n")

csv_file.write(str(cities) + "\n")
csv_file.close()
#in_file = open("email.txt", "w")
with open("email.txt", "w") as in_file:
    for email in emails:
        in_file.write(email + "; \n")

#in_file.close()

