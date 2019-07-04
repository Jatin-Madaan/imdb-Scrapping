from bs4 import BeautifulSoup
import pandas as pd
import requests
no = []
titlel = []
ratingl = []
castl = []
for i in range(1, 11):
    page = requests.get('https://www.imdb.com/list/ls005526372/?sort=list_order,asc&st_dt=&mode=detail&page=' + str(i))
    soup = BeautifulSoup(page.content, 'html.parser')
    movies = soup.find_all('div', class_= 'lister-item mode-detail')
    #items = movies.find_all('h3', class_= 'listner-item-header')
    
    for movie in movies:
        for title in movie.find_all('h3', class_= 'lister-item-header'):
            no.append(title.find('span', class_='lister-item-index unbold text-primary').get_text())
            titlel.append(title.find('a').get_text())
        for rating in movie.find_all('div', class_= 'ipl-rating-star small'):
            ratingl.append(rating.find('span', class_='ipl-rating-star__rating').get_text())
        Starcast = ""
        for cast in movie.find_all('p',class_='text-muted text-small'):
            for star in cast.find_all('a'):
                Starcast += star.get_text() + " "
        castl.append(Starcast)
if(len(no) > len(ratingl)):
    for i in range(len(no) - len(ratingl)):
        ratingl.append("N\A")

imdbList = pd.DataFrame(
    {
        'Rank':no,
        'Title':titlel,
        'Rating' : ratingl,
        'Cast' : castl,
    }
)
print(imdbList)
imdbList.to_csv('result.csv')