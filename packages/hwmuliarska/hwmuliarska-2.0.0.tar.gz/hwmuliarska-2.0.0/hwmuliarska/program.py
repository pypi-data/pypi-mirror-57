def read_raitings():
    """
    () -> (dict)
    This function returns dictionary with keys: decades. 
    First, the function reads the information from the file 'ratings.list', 
    discards everything and forms a dictionary. 
    Each key contains information about movies made in this decade and their ratings.

    A part of what this function returns:
    {1990: [[9.2, 'The Shawshank Redemption'], [8.9, 'Pulp Fiction'], [8.9, "Schindler's List"], [8.8, 'Fight Club'], 
    [8.7, 'Forrest Gump']...
    """

    f = open('ratings.list', encoding='utf-8', errors='ignore')
    lst = []
    for line in f:
        if line.startswith("BOTTOM"):
            break
        else:
            line = line.strip()
            line = line.split()
            lst.append(line)

    result = []
    for i in range(len(lst)):
        if lst[i] != []:
            if lst[i][0].startswith("0"):
                result.append(lst[i])
    
    films = {}
    for i in result:
        info_film = [float(i[2]), ' '.join(i[3:len(i)-1])]
        date = int(i[-1][1:5])
        if date % 10 != 0:
            if date - (date % 10) not in films:
                films[date - (date % 10)] = []
            films[date - (date % 10)].append(info_film)
        else:
            if date - 10 not in films:
                films[date - 10] = []
            films[date - 10].append(info_film)
    return films



def rate_films(films):
    """
    (dict) -> (dict)
    This function returns dictionary with keys: decades.
    Each key contains the average rating of all films in this decade.

    >>> rate_films(read_raitings())
    {1990: 8.35, 1970: 8.35, 2000: 8.3, 1960: 8.3, 1950: 8.29, 2010: 8.28, 1980: 8.28, 1940: 8.28, 1930: 8.28, 1920: 8.28}
    """

    top_films = {}
    m = 0
    counter = 0
    for date in films:
        for rate in films[date]:
            m += rate[0]
            counter += 1
        general = round((m / counter), 2)
        top_films[date] = general
    return top_films



def top_five_decades(top_films):
    """
    (dict) -> (list)
    This function returns list of five the most successful decades 
    by the average rating of all films in each decade.

    >>> top_five_decades(rate_films(read_raitings()))
    [1990, 1970, 2000, 1960, 1950]
    """
    
    rate1 = 0
    rate2 = 0
    rate3 = 0
    rate4 = 0
    rate5 = 0
    for date in top_films:
        if top_films[date] > rate1:
            rate1 = top_films[date]
            top1 = date
        elif top_films[date] > rate2:
            rate2 = top_films[date]
            top2 = date
        elif top_films[date] > rate3:
            rate3 = top_films[date]
            top3 = date
        elif top_films[date] > rate4:
            rate4 = top_films[date]
            top4 = date
        elif top_films[date] > rate5:
            rate5 = top_films[date]
            top5 = date
    return [top1, top2, top3, top4, top5]



def rates_prepearing(dates):
    """
    (list) -> (list)
    This function returns list of ratings of five the most successful decades.

    >>> rates_prepearing(top_five_decades(rate_films(read_raitings())))
    [8.35, 8.35, 8.3, 8.3, 8.29]
    """
    result = []
    top_films = rate_films(read_raitings())
    for date in dates:
        result.append(float(top_films[date]))
    return result



def main():
    """
    (list), (list) -> visualization (pie chart)
    This function creates a visualization as a pie chart. 
    It shows the ratings of five the most successful decades as a percentage
    by using different colors.
    """
    import pandas as pd 
    import matplotlib.pyplot as plt

    dates = top_five_decades(rate_films(read_raitings()))
    rates = rates_prepearing(dates)
    plt.pie(rates, labels=dates, startangle=90, autopct='%.1f%%')
    plt.title('Top-5 successful decades')
    plt.show()



if __name__ == '__main__':
    main()
