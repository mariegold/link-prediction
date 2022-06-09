PICKLE_PATH  = './latest_graph.pickle'

# Set up plotting
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 12})
color = sns.color_palette("muted", as_cmap=True)
sns.set_palette(color)