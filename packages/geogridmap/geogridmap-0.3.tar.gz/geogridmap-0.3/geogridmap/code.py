import itertools
import json

import branca.element
import folium
import folium.plugins
import numpy as np
import pandas as pd
import scipy.optimize
import scipy.stats


class prob_map():
    """
    Class for visualising the outputs of a mixed distribution on a geographic map

    Attributes:quit()
        location: The [latitude, longitude] coordinates of the centre of the map.
                  Latitude ranges from -90 to 90, whilst longitude ranges from -180 to 180.
                  North and East are the positive range whilst South and West are the negative range.

    """

    def __init__(self, location, zoom=12, tile='openstreetmap'):
        self.location = location
        self.zoom = zoom
        self.tile = tile

        mp = folium.Map(location=self.location, zoom_start=self.zoom)
        folium.TileLayer(self.tile).add_to(mp)

        self.mp = mp

    def view_map(self):

        """Function to visualise the map

        Returns:
            Visualisation of the map
        """

        return self.mp

    def plot_points(self, points, radius=10, popup=None, tooltip=None, color='black', fill=True, fill_opacity=1,
                    zoom=None):

        """Function to plot the points on the map

        Args:
           -points(list): The points to be plotted
           -graphical parameters from folium

       Returns:
           The map with points plotted
        """

        mp = self.mp

        # handle single point and list of points or raise errors

        for point in points:
            folium.CircleMarker(point, radius=radius, color=color, fill=fill,
                                fill_opacity=fill_opacity).add_to(mp)

        return mp

    def heat_map(self, points, min_opacity=0.5, max_zoom=18, max_val=1.0, radius=25, blur=15, gradient=None,
                 overlay=True, control=True, show=True):

        """Function to plot heatmap with given points

        Args:
           -points(list): The points to be plotted
           -graphical parameters from folium

       Returns:
           The heatmap
        """
        mp = self.mp

        folium.plugins.HeatMap(points).add_to(mp)

        return (mp)

    def grid(self, north, south, east, west, squares, gmm):

        """Function to define the parameters of the grid plot for a cdf

        Args:
            -north, south (float) : The latitude points for the upper and lower border of the grid
            -east, west (float) : The longitude points for the left and right border of the grid

            squares(int): The number of squares per row
            gmm: The Gaussian Mixture model the CDF is from

        Returns:
            None
        """

        self.north = north
        self.south = south
        self.east = east
        self.west = west

        self.squares = squares
        self.gmm = gmm

    def grid_df(self):

        """Function to create a dataframe with the vertices and probability for each square

        Args:
            None

        Returns:
            Dataframe with probabilities for each square starting from the top left moving right then down
        """
        # Passing the class variables
        north = self.north
        south = self.south
        east = self.east
        west = self.west

        squares = self.squares
        gmm = self.gmm

        # Populating the vertices
        y_points = np.linspace(north, south, squares + 1)
        x_points = np.linspace(west, east, squares + 1)

        grid_top_left = []
        grid_bot_left = []
        grid_top_right = []
        grid_bot_right = []

        for y in range(0, squares):
            for x in range(0, squares):
                top_left = [y_points[y], x_points[x]]
                bot_left = [y_points[y + 1], x_points[x]]
                top_right = [y_points[y], x_points[x + 1]]
                bot_right = [y_points[y + 1], x_points[x + 1]]

                grid_top_left.append(top_left)
                grid_bot_left.append(bot_left)
                grid_top_right.append(top_right)
                grid_bot_right.append(bot_right)

        grid_dic = {'top_left': grid_top_left, 'bottom_left': grid_bot_left, 'top_right': grid_top_right,
                    'bottom_right': grid_bot_right}

        grid_df = pd.DataFrame(data=grid_dic)

        # Calculating the cdf for each respective square
        grid_df = self.grid_prob_returner(grid_df)

        return (grid_df)

    def grid_prob_returner(self, grid):

        """Function to add the probability column to the probability grid

        Args:
            -grid: Dataframe with the vertices for each square starting at the top left moving right then down

        Returns:
            Dataframe with a cdf column
        """
        grid['top_left_prob'] = grid['top_left'].apply(lambda x: self.gmm.cdf(x))
        grid['bot_left_prob'] = grid['bottom_left'].apply(lambda x: self.gmm.cdf(x))
        grid['top_right_prob'] = grid['top_right'].apply(lambda x: self.gmm.cdf(x))
        grid['bot_right_prob'] = grid['bottom_right'].apply(lambda x: self.gmm.cdf(x))

        grid['probability'] = grid['top_right_prob'] + grid['bot_left_prob'] - grid['top_left_prob'] - grid[
            'bot_right_prob']

        grid = grid[['top_left', 'bottom_left', 'top_right', 'bottom_right', 'probability']]

        return (grid)

    def grid_plot(self, boundaries, colors, legend=True):

        """Function to plot the probability grid and determine the color of each square based on probability

        Args:
         -boundaries(list): The boundaries determining the color of each square. The first and last element
                             be 0 and 1 respectively and all elements must be strictly increasing


         -colors(list): The length must the be equal to the length of the boundaries list - 1

         -legend(boolean): Whether to include a legend the default is true

         The boundary from the ith to the i+1 index in the boundaries list maps to the ith color in the
         colors list. Hence the requirements on the lengths

        Returns:
            The map with the probability grid superimposed
        """

        # Checking if the arguments are of a valid length
        self.bound_col_checks(boundaries=boundaries, colors=colors)

        north = self.north
        south = self.south
        east = self.east
        west = self.west

        gmm = self.gmm

        grid_df = self.grid_df()

        grid_perc_array = np.array(grid_df['probability'])

        # Code to find the color for each square based on probability
        color_array = []

        for grid_perc in grid_perc_array:

            for bound_idx in range(len(boundaries) - 1, -1, -1):

                boundary = boundaries[bound_idx]

                if grid_perc >= boundary:
                    color_array.append(colors[bound_idx])
                    break

        # Defining a geojson grid and plotting it on a map
        geojson_grid = self.get_geojson_grid(upper_right=(north, east), lower_left=(south, west), n=self.squares)

        for idx, box in enumerate(geojson_grid):
            geo_json = json.dumps(box)

            color = color_array[idx]

            popup = folium.Popup(grid_perc_array[idx])

            grid_square = folium.GeoJson(geo_json,
                                         style_function=lambda feature, color=color: {
                                             'fillColor': color,
                                             'color': "black",
                                             'weight': 2,
                                             'dashArray': '5, 5',
                                             'fillOpacity': 0.55,
                                         })
            grid_square.add_child(popup)

            mp = self.mp

            mp.add_child(grid_square)

        if legend == True:
            mp = self.legend_maker(mp=mp, boundaries=boundaries, colors=colors)

        return mp

    def bound_col_checks(self, boundaries, colors):

        """Function to check whether input for  and colors are appropriate and raises an error if not

        Args:
            -The probability boundaries and the colors for each boundary

        Returns:
            -An error if the input is not appropriate
        """

        if (len(colors) + 1) != len(boundaries):
            raise ValueError("Number of boundaries must equal number of colors + 1")

        if (boundaries[0] != 0 or boundaries[-1] != 1 or sorted(boundaries) != boundaries
                or len(list(set(boundaries))) != len(boundaries)):
            raise ValueError("Array of bounds does not meet required criteria \n",
                             "*The first element must be 0 \n",
                             "*The final element must be 1 \n",
                             "*The Array must be strictly ascending")

    def get_geojson_grid(self, upper_right, lower_left, n):

        """Function to produce a grid of geojson rectangles, and computes the exposure .

        Args:
        upper_right(tuple): The upper right hand corner of "grid of squares"

        lower_left(tuple): The lower left hand corner of "grid of squares"

        n(integer): The number of rows/columns


        Returns:
            List of "geojson style" dictionary objects
        """

        all_boxes = []

        lat_steps = np.linspace(upper_right[0], lower_left[0], n + 1)
        lon_steps = np.linspace(lower_left[1], upper_right[1], n + 1)

        lat_stride = lat_steps[1] - lat_steps[0]
        lon_stride = lon_steps[1] - lon_steps[0]

        for lat in lat_steps[:-1]:
            for lon in lon_steps[:-1]:
                # Define dimensions of box in grid
                upper_left = [lon, lat + lat_stride]
                upper_right = [lon + lon_stride, lat + lat_stride]
                lower_right = [lon + lon_stride, lat]
                lower_left = [lon, lat]

                # Define json coordinates for polygon
                coordinates = [
                    upper_left,
                    upper_right,
                    lower_right,
                    lower_left,
                    upper_left
                ]

                geo_json = {"type": "FeatureCollection",
                            "properties": {
                                "lower_left": lower_left,
                                "upper_right": upper_right
                            },
                            "features": []}

                grid_feature = {
                    "type": "Feature",
                    "geometry": {
                        "type": "Polygon",
                        "coordinates": [coordinates],
                    }
                }

                geo_json["features"].append(grid_feature)

                all_boxes.append(geo_json)

        return all_boxes

    def legend_maker(self, mp, boundaries, colors):

        """Function to make a legend for the probability grid

        Args:
            mp: The map
            boundaries: The boundaries for the legend
            colors: The colors for the legend

        Returns:
            The map with a legend added
        """

        html_1 = """
        {% macro html(this, kwargs) %}

        <!doctype html>
        <html lang="en">
        <head>
          <meta charset="utf-8">
          <meta name="viewport" content="width=device-width, initial-scale=1">
          <title>jQuery UI Draggable - Default functionality</title>
          <link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">

          <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
          <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>

          <script>
          $( function() {
            $( "#maplegend" ).draggable({
                            start: function (event, ui) {
                                $(this).css({
                                    right: "auto",
                                    top: "auto",
                                    bottom: "auto"
                                });
                            }
                        });
        });

          </script>
        </head>
        <body>


        <div id='maplegend' class='maplegend' 
            style='position: absolute; z-index:9999; border:2px solid grey; background-color:rgba(255, 255, 255, 0.8);
             border-radius:6px; padding: 10px; font-size:14px; right: 20px; bottom: 20px;'>
        """

        html_3 = """

        </body>
        </html>

        <style type='text/css'>
          .maplegend .legend-title {
            text-align: left;
            margin-bottom: 5px;
            font-weight: bold;
            font-size: 90%;
            }
          .maplegend .legend-scale ul {
            margin: 0;
            margin-bottom: 5px;
            padding: 0;
            float: left;
            list-style: none;
            }
          .maplegend .legend-scale ul li {
            font-size: 80%;
            list-style: none;
            margin-left: 0;
            line-height: 18px;
            margin-bottom: 2px;
            }
          .maplegend ul.legend-labels li span {
            display: block;
            float: left;
            height: 16px;
            width: 30px;
            margin-right: 5px;
            margin-left: 0;
            border: 1px solid #999;
            }
          .maplegend .legend-source {
            font-size: 80%;
            color: #777;
            clear: both;
            }
          .maplegend a {
            color: #777;
            }
        </style>
        {% endmacro %}"""

        html_2a = """
        <div class='legend-title'>Probabilities</div>
        <div class='legend-scale'>
          <ul class='legend-labels'> \n """

        html_2c = """ \n
          </ul>
        </div>
        </div>"""

        html_2b = """"""

        for idx, color in enumerate(colors):
            string = str(boundaries[idx]) + "-" + str(boundaries[idx + 1])

            full_string = "<li><span style='background:{};opacity:0.7;'></span>{}</li>".format(color, string)

            html_2b += full_string

            html_2b += "\n"

        html_2 = html_2a + html_2b + html_2c

        html_full = html_1 + html_2 + html_3

        legend = branca.element.MacroElement()
        legend._template = branca.element.Template(html_full)

        mp.get_root().add_child(legend)

        return (mp)


class gmm():
    """
    Class for defining and performing operations on the Gaussian mixture model

    Attributes:
        -means: The coordinates of the individual centroids
        -variances: The variances of the centroid (only diagonal covariance matrices permitted at the moment)
        -weights: The weight of each centroid
    """

    def __init__(self, means, variances, weights):
        self.means = means
        self.variances = variances

        self.weights_checker(weights)

        self.weights = weights

    def weights_checker(self, weights):

        """Function to check if the weight input to the class is appropriate and to raise an error if not

        Args:
            -weights: a list/array of weights

        Returns:
            -An error if the input is not appropriate
        """

        if sum(weights) != 1:
            raise ValueError("The sum of the weights must be equal to 1")

        for weight in weights:

            if weight < 0 or weight > 1:
                raise ValueError("Individual weights must be between 0 and 1")

    def sampler(self, sample_size):

        """Function to produce a random sample from the defined distribution

        Args:
            -sample_size(integer): The number of points in the sample

        Returns:
            -A random sample from the gmm fit
        """

        rand_idx = np.random.multinomial(sample_size, self.weights, 1)[0]

        all_samples = []
        for idx, size in enumerate(rand_idx):
            one_sample = scipy.stats.multivariate_normal(self.means[idx], self.variances[idx]).rvs(size)
            all_samples.append(one_sample)

        all_samples_merged = (list(itertools.chain.from_iterable(all_samples)))

        return all_samples_merged

    def cdf(self, point):

        """Function to calculate the probability of a given observation being less than or equal to the given point
           i.e. to the bottom left of the given point

        Args:
            -point(tuple): The (latitude, longitude) coordinates of the point.

        Returns:
            -The probability of a given observation being less than or equal to a given point
        """

        probability = 0
        for idx, weight in enumerate(self.weights):
            one_prob = scipy.stats.multivariate_normal(self.means[idx], self.variances[idx]).cdf(point)
            adj_prob = one_prob * weight
            probability += adj_prob

        return probability
    
    def inverse_cdf(self, inv_prob, direction):
    
        """Function which outputs the latitude/longitude coordinate at which a certain probability is met

        Args:
            -inv_prob(float): The probability value
            -direction(string): specifices either latitude or longitude
        
        Returns:
            -The point with a cdf output of inv_prob
        """
        
        self.direction_check(direction)
        
        if direction == 'latitude':
            
            start_point = (self.weights@self.means)[0]
             
            lat_cord = scipy.optimize.fmin(self.inverse_cdf_helper, x0 = start_point, args = (inv_prob, direction,),
                                          disp = False)
            
            return (lat_cord[0])
            
        if direction == 'longitude':
            
            start_point = (self.weights@self.means)[1]
            
            long_cord = scipy.optimize.fmin(self.inverse_cdf_helper, x0 = start_point, args = (inv_prob, direction,),
                                           disp = False)

            return (long_cord[0])
    
    def inverse_cdf_helper(self, point, inv_prob,direction):
        
        """Helper function which is minimised within the inv_cdf function

        Args:
            -point(tuple): The (latitude, longitude) coordinates of a given point
            -inv_prob(float): The inv_prob input to the inverse_cdf function
            -direction(string): specifices either latitude or longitude
            
        Returns:
            -The absolute value of the difference between the probability output of the cdf for a given point and
             the required cdf value
        """
        
        if direction == 'latitude':
            
            coordinate = (point,180)
            
        if direction == 'longitude': 
            
            coordinate = (90, point)
        
        prob = self.cdf(coordinate)

        root = prob - inv_prob

        root = np.abs(root)

        return root
    
    def direction_check(self, direction):
        
        """Function to check if the direction input to the class is valid and to raise an error if not

        Args:
            -direction(string): specifices either latitude or longitude

        Returns:
            -An error if the input is not appropriate
        """
        
        direction_list = ['latitude', 'longitude']
            
        if direction not in direction_list:
             raise ValueError("The direction must be either latitude and longitude")


def random_centroid_maker(location, variance, size):
    """Function to produce separate centroids for testing and demonstration

    Args:
        -location(tuple): The (latitude, longitude) coordinates of the mean of the
                           gaussian to generate centroids from
        -variance(tuple): The variance of gaussian to generate centroids from
        -size(integer): The number of centroids to generate

    Returns:
        -A random sample of (latitude, longitude) coordinates to act as centroids for testing and demonstration
    """

    distribution = scipy.stats.multivariate_normal(location, variance)
    centroids = distribution.rvs(size)

    return centroids







