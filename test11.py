import requests
import bs4


# main_ul = bsp.find("ul",{"class","e1p6yfdy3"})

# main_li = main_ul.findAll("li",{"class","eloznup73"})

# href_list = []

# for li in main_li:
#   sub_ul = li.find("ul")
#   sub_li = sub_ul.findAll("li")
#   for sli in sub_li:
#     href_list.append(sli.find("a")["href"])

# print(href_list)    



# main_a = bsp.findAll("a",{"class","permanent-img"})
# href_list=[]

# for href in main_a:
#   href_list.append(href.attrs("href"))
# print(" , ".join(href_list))  

def getHref(html_tag):
  mul = bsp.find("ul",{"class","permanent-list-body"})
  href_list=[]
  al1 = mul.findAll("li")
  # print(main_ul)
  for a in al1:
    sul = a.findAll("ul",{"class","permanent-area"})
    for li1 in sul:
      li = li1.findAll("li")
      for li_1 in li:
        if li_1.find("a"):
          href_list.append(li_1.find("a")["href"])
  return href_list        
  


url = "https://www.museum.go.kr/site/main/content/permanent_exhibition_guide"
site = "https://www.museum.go.kr"
result = requests.get(url=url)

bsp = bs4.BeautifulSoup(result.content, "html.parser")

href_list = getHref(bsp)
site_info = dict()
dic_column = ["title","menu"]
for href in href_list:
  link = site+href
  result2 = requests.get(url=link)
  sub_bsp = bs4.BeautifulSoup(result2.content,"html.parser")
  ptitle = sub_bsp.find("h2",{"class","page-title"}).text
  showtitle = sub_bsp.find("p",{"class","showroom-title"}).text 
  ul = sub_bsp.find("ul",{"class","swiper-wrapper"})
  li = ul.findAll("li")
  menu = [l.find("a").text.strip() for l in li]
  site_info[ptitle] = dict(zip(dic_column,[showtitle,menu]))
  print(site_info)