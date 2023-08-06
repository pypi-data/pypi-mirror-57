import geogridmap
new_york = [40.712, -74.006]
geogridmap.prob_map(location = new_york, zoom = 10)

print(geogridmap.random_centroid_maker(new_york, [0.002, 0.002], 3))

