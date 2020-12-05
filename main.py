import Nightscout
import SlidingWindow
import DimensionalityReduction
import matplotlib.pyplot as plt
import Preprocessing

nightscout_url = 'https://anna.ns.10be.de/'
number_of_days = 14

# get data
ns = Nightscout.Nightscout(nightscout_url, number_of_days)
ns.query()
sgv = ns.get_filtered_sgv()

# smoothing
pr = Preprocessing.Preprocessing(sgv)
sgv = pr.smoothing()

# sliding window
window = SlidingWindow.SlidingWindow(sgv)
window.normalize()
sliding_matrix = window.get_window_matrix()

# downprojection: reduce sliding_matrix dimensions from "window_size" to 2 so it can be plotted in 2D
reduced_matrix = DimensionalityReduction.DimensionalityReduction(sliding_matrix).pca()

# plot
fig, ax = plt.subplots(2, gridspec_kw={'height_ratios': [1, 4]})
ax[0].plot(range(0,len(sgv)*5,5),sgv/10)
ax[0].set(xlabel="time [minutes]")
ax[0].set(ylabel="blood glucose [mg/dl]")
ax[0].set_title("Time series")
ax[1].scatter(reduced_matrix[:,0], reduced_matrix[:,1], alpha=0.2)
ax[1].plot(reduced_matrix[:,0], reduced_matrix[:,1], alpha=0.2)
ax[1].set_title("PCA")
ax[1].set(xlabel="PCA 1")
ax[1].set(ylabel="PCA 2")
plt.show()
