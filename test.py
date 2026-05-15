# 3rd party
import folium

# this package
import folium_bottom_sheet


class MSC(folium_bottom_sheet.MapSearchControl):
	default_js = [
			folium_bottom_sheet.MapSearchControl.default_js[0],
			(
					"folium-bottom-sheet_js",
					"folium_bottom_sheet/folium-bottom-sheet.js",
					),
			]


map = folium.Map()

layer = folium.FeatureGroup()

marker = folium.Marker(title="Test marker", location=[0, 0], popup="Test popup")
marker.add_to(layer)

marker2 = folium.Marker(tooltip="Another marker", searchName="Another marker", location=[0.5, 0])
marker2.add_to(layer)

layer.add_to(map)

# search1 = MSC(
# 		provider=folium_bottom_sheet.OpenStreetMapProvider(),
# 		auto_complete_delay=1000,
# 		show_marker=False,
# 		search_label="Search OpenStreetMap"
# 		)
# search1.add_to(map)

search2 = MSC(
		provider=folium_bottom_sheet.MapSearchProvider(map=map, layer=layer, feature_type="settlement"),
		auto_complete_delay=1000,
		show_marker=False,
		max_suggestions=15,
		search_label="Search OSM and map",
		)
search2.add_to(map)

map.save("index.html")
