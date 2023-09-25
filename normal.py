{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "21a8f7f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "from scipy.stats import norm\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Generate random numbers from N(0,1)\n",
    "data_normal = norm.rvs(size=10000, loc=0, scale=1)\n",
    "\n",
    "# Plotting the histogram\n",
    "plt.hist(data_normal, bins=100, density=True, alpha=0.6, color='b')\n",
    "plt.xlabel('Normal Distribution')\n",
    "plt.ylabel('Frequency')\n",
    "plt.title('Histogram of Normal Distribution')\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
