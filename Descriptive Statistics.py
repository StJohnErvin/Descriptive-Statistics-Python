{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "af6a0e9a",
   "metadata": {},
   "source": [
    "## Descriptive Statistics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "782eb81c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Descriptive Statistics\n",
      "Mean :  5.76\n",
      "Mode :  5\n",
      "Median :  5\n",
      "Range :  8\n",
      "Population Variance :  5.14\n",
      "Population Standard Deviation :  5\n"
     ]
    }
   ],
   "source": [
    "import statistics\n",
    "\n",
    "friends_usage = [5,4,3,5,8,2,5,2,5,8,10,8,7,9,10,5,7,5,7,5,4,3,5,8,4]\n",
    "\n",
    "mean = statistics.mean(friends_usage)\n",
    "mode = statistics.mode(friends_usage)\n",
    "median = statistics.median(friends_usage)\n",
    "pstdev = round(statistics.mode(friends_usage),2)\n",
    "pvariance = round(statistics.pvariance(friends_usage),2)\n",
    "srange = (max(friends_usage)-min(friends_usage))\n",
    "\n",
    "print(\"Descriptive Statistics\")\n",
    "print(\"Mean : \",mean)\n",
    "print(\"Mode : \",mode)\n",
    "print(\"Median : \",median)\n",
    "print(\"Range : \",srange)\n",
    "print(\"Population Variance : \",pvariance)\n",
    "print(\"Population Standard Deviation : \",pstdev)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fcfcda6f",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
