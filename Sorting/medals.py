#The dictionary, medals, shows the medal count for six countries during the Rio Olympics.Sort the country names by medal counts.


medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}

medals_sorted = sorted(medals, key = lambda country : -medals[country])

top_three = medals_sorted[0:3]
