{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "48e60588",
   "metadata": {},
   "outputs": [],
   "source": [
    "#import uniform distribution\n",
    "from scipy.stats import uniform\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "#random numbers from uniform distribution\n",
    "n = 10000\n",
    "start = 10\n",
    "width = 20\n",
    "data_uniform = uniform.rvs(size=n, loc=start, scale=width)\n",
    "\n",
    "# Plotting the histogram\n",
    "plt.hist(data_uniform, bins=100, density=True, alpha=0.6, color='g')\n",
    "plt.xlabel('Uniform Distribution')\n",
    "plt.ylabel('Frequency')\n",
    "plt.title('Histogram of Uniform Distribution')\n",
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
