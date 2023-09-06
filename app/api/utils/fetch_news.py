import requests
def parseHTML(val):
    news_list = []
    url = requests.get(val).text
    xmlItems = url.split('<item>')[1::][1::]
    for i in range(0,4):
        desc = xmlItems[i].split('<title>' )[1].split('</title>')[0].split('<![CDATA[')[1].split(']]>')[0]
        link = xmlItems[i].split('<link>' )[1].split('</link>')[0]
        image = xmlItems[i].split('href="' )[1].split('"/>')[0]
        date = xmlItems[i].split('<pubDate>')[1].split('</pubDate>')[0].split(', ')[1].split(' ')
        author = xmlItems[i].split('<dc:creator>' )[1].split('</dc:creator>')[0]
        month = date[1]
        day = date[0]
        year = date[2]
        # print(xmlItems[i])
        news_list.append({"title":desc, 
                          "link":link, 
                          "image":image, 
                          "date":date, 
                          "author":author, 
                          "day":day,
                          "month":month,
                          "year":year,
                          })
    return  news_list