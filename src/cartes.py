import folium


m=folium.Map()



villes=[
    [
      48.866667,2.333333  
    ],
    [
        40.416775,-3.703790
    ],
    [
        40.712784,-74.005941
    ],
    [
        55.757425,37.619183
    ],
    [
        48.1113387,-1.6800198
    ]
]

for ville in villes:
    folium.Marker(
        location=ville
    
    ).add_to(m)

m.save("carte.html")