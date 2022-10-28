import requests
from bs4 import BeautifulSoup
import nltk
import urllib
import re


def get_info(web_url):
    req = requests.get(web_url)
    html = req.text
    urls = []
    soup = BeautifulSoup(html, features="html.parser")
    # get url of differenr jobs
    for link in soup.findAll('a'):
        urls.append(link.get('href'))

    # get all job ids
    ids = []
    for url in urls:
        ids.append(url[-10:])
    print(ids)

    # M is the container recording info of all jobs
    M = []
    for id in ids:
        # get url of differnt jobs
        url = 'https://boards.greenhouse.io/embed/job_app?for=coursera&token=' + id + '&b=https%3A%2F%2Fabout.coursera.org%2Fcareers%2Fjobs%2F'

        response = requests.get(url)
        result = response.text


        soup1 = BeautifulSoup(result, features='html.parser')
        ans1 = soup1.find("span", style="font-weight: 400;")
        mlist = ""
        for tag in ans1:
            mlist = mlist+str(tag.string)

        content = soup1.find("div", id="content")
        uls = content.find_all("ul")
        mlist1 = ""
        mlist2 = ""
        mlist3 = ""
        # print(content)
        for i in range(3):
            if (i == 0):
                for li in uls[i]:
                    if(len(li) > 1):
                        for i in li:
                            mlist1 += str(i.string)
                    else:
                        mlist1 += str(li.string)

            if(i == 1):
                for li in uls[i]:
                    if (len(li) > 1):
                        for i in li:
                            mlist2 += str(i.string)
                    else:
                        mlist2 += str(li.string)

            if(i == 2):
                for li in uls[i]:
                    if (len(li) > 1):
                        for i in li:
                            mlist3 += str(i.string)
                    else:
                        mlist3 += str(li.string)

        res = ""
        # print(uls[0])
        for li in uls[1]:
            if(len(li) > 1):
                for i in li:
                    res = res + str(i.string)
            else:
                res += str(li.string)
            # print(cur)
        # print(res)


        m = {
            "Discription": mlist,
            "Responsibility": mlist1,
            "Basic qualification": mlist2,
            "Preferred qualification": mlist3
        }

        M.append(m)
    return M

web_url = 'https://boards.greenhouse.io/embed/job_board?for=coursera'
M = get_info(web_url)

for m in M:
    print(m)