{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3de90040",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjcAAAHFCAYAAAAOmtghAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAABBMklEQVR4nO3deXxMZ///8ffILpIgtlgaue27EtS+lRZVtL1LWyRFb4q7CG0tt5uqSlGqC0Ht1aouqPbWamqrWloUtZW2VKikdkHbkOT6/eGX+RqZkIwkE8fr+XjM42Guuc45nzNL5u061zljM8YYAQAAWEQ+dxcAAACQnQg3AADAUgg3AADAUgg3AADAUgg3AADAUgg3AADAUgg3AADAUgg3AADAUgg3AADAUgg3yHELFiyQzWbT9u3bnT7+0EMPqWzZsg5tZcuWVWRkZJa2s3nzZo0dO1bnz593rdC70NKlS1WtWjX5+fnJZrNp165dTvutX79eNpstw9uCBQtyte68aMKECVqxYkW69rTnbv369VleZ2aXvfH18fb2VtGiRdW4cWONGjVKR48eTbdM2ufyt99+y1JNGe3nzTjbVosWLVS9evUsredWVq1apbFjxzp9zJW/Kbhzebq7AMCZ5cuXKzAwMEvLbN68WS+99JIiIyNVsGDBnCnMQk6dOqUePXrowQcf1IwZM+Tj46OKFSvedJkJEyaoZcuW6drLlSuXU2XeMSZMmKDHHntMnTt3dmivU6eOtmzZoqpVq+ZKDS1btlRKSorOnDmj7777TvPmzdPrr7+ud955R0899ZS9b4cOHbRlyxaFhIRkeRvO9vNmXN1WVq1atUrTp093GnBc+ZuCOxfhBnnSvffe6+4Ssuzq1auy2Wzy9LwzPlaHDh3S1atX1b17dzVv3jxTy1SoUEH33XdfDldmLYGBgbn2nN34+jz88MMaOnSo7r//fkVGRqpmzZqqUaOGJKlo0aIqWrRojtbz119/ydfXN1e2dSt34t8UuI7DUsiTbhxCTk1N1fjx41WpUiX5+fmpYMGCqlmzpt544w1J0tixY/X8889LksLCwuzD82nD+ampqZo0aZIqV64sHx8fFStWTD179tTx48cdtmuM0YQJExQaGipfX1+Fh4crNjZWLVq0UIsWLez90g4DvPvuuxo6dKhKlSolHx8f/fLLLzp16pT69++vqlWrqkCBAipWrJhatWqljRs3Omzrt99+k81m0+TJkzVx4kSVLVtWfn5+atGihT14DB8+XCVLllRQUJC6dOmikydPZur5W7lypRo2bKj8+fMrICBAbdq00ZYtW+yPR0ZGqkmTJpKkrl27ymazOeyfq7799lt5eXlp2LBhDu1phyXmzp1rb7PZbBo4cKBmzZqlihUrysfHR1WrVtUHH3yQbr179+5Vp06dVKhQIfn6+qp27dpauHChQ5+012TJkiUaNWqUSpYsqcDAQN1///06ePBgunV+/fXXat26tQIDA5U/f341btxYa9ascegzduxY2Ww27du3T0888YSCgoJUvHhx9erVSxcuXHDYl8uXL2vhwoX2917a8+ns0NL27dvVrVs3+2tetmxZPfHEE04PH92uwoULa9asWUpOTtbrr79ub3d2qGjnzp166KGHVKxYMfn4+KhkyZLq0KGD/XNys/1MW99XX32lXr16qWjRosqfP7+SkpJueghs48aNuu++++Tn56dSpUpp9OjRSklJsT+e0aG5tM9P2iHRyMhITZ8+3V5n2i1tm84OS8XFxal79+72/a1SpYqmTJmi1NTUdNt57bXXNHXqVIWFhalAgQJq2LChtm7dmoVXArnpzvgvJiwhJSVFycnJ6doz88P0kyZN0tixY/Wf//xHzZo109WrV/XTTz/Z59f06dNHZ8+e1VtvvaVly5bZh7/TDgU8++yzmj17tgYOHKiHHnpIv/32m0aPHq3169frhx9+UJEiRSRJo0aNUnR0tP71r3/pkUce0bFjx9SnTx9dvXrV6SGbESNGqGHDhpo5c6by5cunYsWK6dSpU5KkMWPGqESJErp06ZKWL1+uFi1aaM2aNelCxPTp01WzZk1Nnz5d58+f19ChQ9WxY0c1aNBAXl5emjdvno4ePaphw4apT58+Wrly5U2fq/fff19PPfWU2rZtqyVLligpKUmTJk2yb79JkyYaPXq06tevrwEDBtgPZWRmyD41NdXpa5g2WtWkSRONHz9ew4cPV7NmzfTwww9r3759GjBggLp3767evXs7LLdy5UqtW7dO48aNk7+/v2bMmKEnnnhCnp6eeuyxxyRJBw8eVKNGjVSsWDG9+eabCg4O1uLFixUZGak//vhDL7zwgsM6R44cqcaNG2vOnDlKTEzUiy++qI4dO+rAgQPy8PCQJC1evFg9e/ZUp06dtHDhQnl5eWnWrFl64IEHtHr1arVu3dphnY8++qi6du2q3r17a8+ePRoxYoQkad68eZKkLVu2qFWrVmrZsqVGjx4tSTd9Pn/77TdVqlRJ3bp1U+HChRUfH6+YmBjVq1dP+/fvt78fs0u9evUUEhKib775JsM+ly9fVps2bRQWFqbp06erePHiSkhI0Lp163Tx4sVM72evXr3UoUMHvfvuu7p8+bK8vLwy3GZCQoK6deum4cOHa9y4cfrf//6n8ePH69y5c3r77beztI+jR4/W5cuX9fHHHzsE+YwOhZ06dUqNGjXSlStX9PLLL6ts2bL6/PPPNWzYMP3666+aMWOGQ//p06ercuXKmjZtmn177du315EjRxQUFJSlWpELDJDD5s+fbyTd9BYaGuqwTGhoqImIiLDff+ihh0zt2rVvup3JkycbSebIkSMO7QcOHDCSTP/+/R3av/vuOyPJjBw50hhjzNmzZ42Pj4/p2rWrQ78tW7YYSaZ58+b2tnXr1hlJplmzZrfc/+TkZHP16lXTunVr06VLF3v7kSNHjCRTq1Ytk5KSYm+fNm2akWQefvhhh/UMHjzYSDIXLlzIcFspKSmmZMmSpkaNGg7rvHjxoilWrJhp1KhRun346KOPbrkPaX0zuh07dszeNzU11bRv394ULFjQ7N2711StWtVUrlzZXLp0yWGdkoyfn59JSEhweK4qV65sypcvb2/r1q2b8fHxMXFxcQ7Lt2vXzuTPn9+cP3/eocb27ds79Pvwww+NJLNlyxZjjDGXL182hQsXNh07dkz33NWqVcvUr1/f3jZmzBgjyUyaNMmhb//+/Y2vr69JTU21t/n7+zu8Z2987tatW5fusev3+9KlS8bf39+88cYbWVr2+n43ey0bNGhg/Pz87PfTPpdpn5ft27cbSWbFihU33VZG+5m2vp49e2b42PWfzebNmxtJ5tNPP3Xo+8wzz5h8+fKZo0ePOuzbjc9B2udn/vz59rYBAwaYjL7WbvybMnz4cCPJfPfddw79nn32WWOz2czBgwcdtlOjRg2TnJxs7/f9998bSWbJkiVOtwf34rAUcs2iRYu0bdu2dLe0wyM3U79+fe3evVv9+/fX6tWrlZiYmOntrlu3TpLSDUnXr19fVapUsR+K2Lp1q5KSkvT444879LvvvvvSnc2V5tFHH3XaPnPmTNWpU0e+vr7y9PSUl5eX1qxZowMHDqTr2759e+XL938fxSpVqki6NgnzemntcXFxGezptVGOEydOqEePHg7rLFCggB599FFt3bpVf/75Z4bL38rEiROdvobFixe397HZbFq0aJECAgIUHh6uI0eO6MMPP5S/v3+69bVu3dphWQ8PD3Xt2lW//PKL/VDI2rVr1bp1a5UpU8Zh2cjISP35558O/0uXrs0zuV7NmjUlyX7IZ/PmzTp79qwiIiKUnJxsv6WmpurBBx/Utm3bdPny5Vuu8++//870YcIbXbp0SS+++KLKly8vT09PeXp6qkCBArp8+bLT90h2MLcYIS1fvrwKFSqkF198UTNnztT+/ftd2k5GnwlnAgIC0j23Tz75pFJTU286ypQd1q5dq6pVq6p+/foO7ZGRkTLGaO3atQ7tHTp0sI/8SenfV8hbOCyFXFOlShWFh4enaw8KCtKxY8duuuyIESPk7++vxYsXa+bMmfLw8FCzZs00ceJEp+u83pkzZyQ5H54uWbKk/Y9TWr/rv2zTOGvLaJ1Tp07V0KFD1a9fP7388ssqUqSIPDw8NHr0aKdfXIULF3a47+3tfdP2v//+22kt1+9DRvuampqqc+fOKX/+/Bmu42b+8Y9/3PL5lqTg4GA9/PDDmj59urp06WKfxHqjEiVKZNh25swZlS5dWmfOnMlwf9L63bjt6/n4+Ei6NrlVkv744w9Jsh/2cubs2bMOYexW68yqJ598UmvWrNHo0aNVr149BQYGymazqX379i6v81bi4uLsz5kzQUFB2rBhg1555RWNHDlS586dU0hIiJ555hn95z//uenhpetl5YwoZ5+r61//nHTmzBmn/2lx9X2FvIVwgzuCp6enoqKiFBUVpfPnz+vrr7/WyJEj9cADD+jYsWM3/bJO+6MUHx+v0qVLOzx24sQJ+/yGtH5pX37XS0hIcPqH0GazpWtbvHixWrRooZiYGIf2tHkLOen6fb3RiRMnlC9fPhUqVCjH64iNjVVMTIzq16+v5cuX65NPPnH6P/qEhIQM29L2JTg4OMP9kZTl+Slp/d96660Mz2LKKMxmhwsXLujzzz/XmDFjNHz4cHt7UlKSzp49myPb/P7775WQkJBuztONatSooQ8++EDGGP34449asGCBxo0bJz8/P4dab8bZZyIjGX3WpP97/X19fSVde36ud/r0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TL6+vunaAQDA3StL4SYiIsLhfvfu3W9r4127dtWZM2c0btw4xcfHq3r16lq1apVCQ0MlSfHx8be85g0AAMD1bOZ2Js7cgRITExUUFKQLFy4oMDAw+zdwN125d9Ysx/vO9v3GPgAAuCAr39+3NaEYuKUbAw9hBwCQw1z6+QUAAIC8inADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAshXADAAAsxdPdBeAu07dv+rZZs3K/DgCAZTFyAwAALIVwAwAALIVwAwAALIVwAwAALIVwAwAALIVwAwAALIVwAwAALIVwAwAALIVwAwAALIVwAwAALIWfX4D7OftJhhvxEw0AgExi5AYAAFgK4QYAAFgK4QYAAFgK4QYAAFgK4QYAAFgK4QYAAFgK4QYAAFgK4QYAAFgK4QYAAFgKVyiG6zJzZWEAAHIZIzcAAMBSCDcAAMBSCDcAAMBSCDcAAMBSCDcAAMBSCDcAAMBSCDcAAMBSCDcAAMBSCDcAAMBSCDcAAMBSCDcAAMBSCDcAAMBSCDcAAMBSCDcAAMBSCDcAAMBSPN1dAJApffs63p81yz11AADyPEZuAACApRBuAACApRBuAACApRBuAACApRBuAACApRBuAACApRBuAACApRBuAACApRBuAACApRBuAACApRBuAACApRBuAACApRBuAACApbg93MyYMUNhYWHy9fVV3bp1tXHjxgz7Llu2TG3atFHRokUVGBiohg0bavXq1blYLQAAyOvcGm6WLl2qwYMHa9SoUdq5c6eaNm2qdu3aKS4uzmn/b775Rm3atNGqVau0Y8cOtWzZUh07dtTOnTtzuXIAAJBX2Ywxxl0bb9CggerUqaOYmBh7W5UqVdS5c2dFR0dnah3VqlVT165d9d///jdT/RMTExUUFKQLFy4oMDDQpbpvqm/f7F8n0ps1y90VAAByUVa+v902cnPlyhXt2LFDbdu2dWhv27atNm/enKl1pKam6uLFiypcuHCGfZKSkpSYmOhwAwAA1uW2cHP69GmlpKSoePHiDu3FixdXQkJCptYxZcoUXb58WY8//niGfaKjoxUUFGS/lSlT5rbqBgAAeZvbJxTbbDaH+8aYdG3OLFmyRGPHjtXSpUtVrFixDPuNGDFCFy5csN+OHTt22zUDAIC8y9NdGy5SpIg8PDzSjdKcPHky3WjOjZYuXarevXvro48+0v3333/Tvj4+PvLx8bntegEAwJ3BbeHG29tbdevWVWxsrLp06WJvj42NVadOnTJcbsmSJerVq5eWLFmiDh065EapsJIbJ3wzMRkALMdt4UaSoqKi1KNHD4WHh6thw4aaPXu24uLi1K9fP0nXDin9/vvvWrRokaRrwaZnz5564403dN9999lHffz8/BQUFOS2/QAAAHmHW8NN165ddebMGY0bN07x8fGqXr26Vq1apdDQUElSfHy8wzVvZs2apeTkZA0YMEADBgywt0dERGjBggW5XT4AAMiD3BpuJKl///7q37+/08duDCzr16/P+YIAAMAdze1nSwEAAGQnt4/cANmGycIAADFyAwAALIZwAwAALIVwAwAALIVwAwAALIVwAwAALIWzpWBdN549ldk+uXmWFWd4AUC2Y+QGAABYCuEGAABYCuEGAABYCuEGAABYChOKgRvl9Um+7p4EDQB5HCM3AADAUgg3AADAUgg3AADAUgg3AADAUphQjDtTZq4+DAC4KzFyAwAALIVwAwAALIVwAwAALIVwAwAALIUJxcCtZOaKwK72AQBkO0ZuAACApRBuAACApRBuAACApRBuAACApRBuAACApXC2FJBTcvPsqBu3deOZWgBwF2HkBgAAWArhBgAAWArhBgAAWArhBgAAWAoTigFX5NRk4cz8jENecyfWDMDSGLkBAACWQrgBAACWQrgBAACWQrgBAACWQrgBAACWQrgBAACWQrgBAACWQrgBAACWQrgBAACWwhWKgbtFZq6qnJkrC+fU1ZkBIJswcgMAACyFcAMAACyFcAMAACyFcAMAACyFcAMAACyFs6UA/J8bz4TKzNlT2bUeV8/CcrVGAJbFyA0AALAUwg0AALAUwg0AALAUwg0AALAUJhQDeZ07f+7gTviphcxMXs6uidIA7giM3AAAAEsh3AAAAEsh3AAAAEsh3AAAAEthQjFgRXltIrCzenJqUq+r+56Z5ZiIDNwRGLkBAACWQrgBAACWQrgBAACWQrgBAACWwoRiAO6R1yY9Z4YrVzp2dTI1E5yRJq9fYTs3TxjIJLeP3MyYMUNhYWHy9fVV3bp1tXHjxpv237Bhg+rWrStfX1/94x//0MyZM3OpUgAAcCdwa7hZunSpBg8erFGjRmnnzp1q2rSp2rVrp7i4OKf9jxw5ovbt26tp06bauXOnRo4cqeeee06ffPJJLlcOAADyKreGm6lTp6p3797q06ePqlSpomnTpqlMmTKKiYlx2n/mzJm65557NG3aNFWpUkV9+vRRr1699Nprr+Vy5QAAIK9yW7i5cuWKduzYobZt2zq0t23bVps3b3a6zJYtW9L1f+CBB7R9+3ZdvXo1x2oFAAB3DrdNKD59+rRSUlJUvHhxh/bixYsrISHB6TIJCQlO+ycnJ+v06dMKCQlJt0xSUpKSkpLs9y9cuCBJSkxMvN1dcO7KlZxZL4Ds4+zz78pnNzN/R5yt19XlXFkP7nw3vhfy2uvu6ns8i9K+t40xt+zr9rOlbDabw31jTLq2W/V31p4mOjpaL730Urr2MmXKZLVUAFaxYIF71+Pu7ePOdie87jlY48WLFxUUFHTTPm4LN0WKFJGHh0e6UZqTJ0+mG51JU6JECaf9PT09FRwc7HSZESNGKCoqyn4/NTVVZ8+eVXBw8E1DlCsSExNVpkwZHTt2TIGBgdm67ryM/b579vtu3GeJ/Wa/re9O2GdjjC5evKiSJUvesq/bwo23t7fq1q2r2NhYdenSxd4eGxurTp06OV2mYcOG+uyzzxzavvrqK4WHh8vLy8vpMj4+PvLx8XFoK1iw4O0VfwuBgYF59s2Rk9jvu8fduM8S+323uRv3O6/v861GbNK49WypqKgozZkzR/PmzdOBAwc0ZMgQxcXFqV+/fpKujbr07NnT3r9fv346evSooqKidODAAc2bN09z587VsGHD3LULAAAgj3HrnJuuXbvqzJkzGjdunOLj41W9enWtWrVKoaGhkqT4+HiHa96EhYVp1apVGjJkiKZPn66SJUvqzTff1KOPPuquXQAAAHmM2ycU9+/fX/3793f62AInE5KaN2+uH374IYerco2Pj4/GjBmT7jCY1bHfd89+3437LLHf7Lf1WW2fbSYz51QBAADcIdz+21IAAADZiXADAAAshXADAAAshXADAAAshXCTTWbMmKGwsDD5+vqqbt262rhxo7tLynHffPONOnbsqJIlS8pms2nFihXuLinHRUdHq169egoICFCxYsXUuXNnHTx40N1l5biYmBjVrFnTfoGvhg0b6osvvnB3WbkqOjpaNptNgwcPdncpOW7s2LGy2WwOtxIlSri7rBz3+++/q3v37goODlb+/PlVu3Zt7dixw91l5aiyZcume61tNpsGDBjg7tJuC+EmGyxdulSDBw/WqFGjtHPnTjVt2lTt2rVzuEaPFV2+fFm1atXS22+/7e5Scs2GDRs0YMAAbd26VbGxsUpOTlbbtm11+fJld5eWo0qXLq1XX31V27dv1/bt29WqVSt16tRJ+/btc3dpuWLbtm2aPXu2atas6e5Sck21atUUHx9vv+3Zs8fdJeWoc+fOqXHjxvLy8tIXX3yh/fv3a8qUKTl+RXt327Ztm8PrHBsbK0n65z//6ebKbpPBbatfv77p16+fQ1vlypXN8OHD3VRR7pNkli9f7u4yct3JkyeNJLNhwwZ3l5LrChUqZObMmePuMnLcxYsXTYUKFUxsbKxp3ry5GTRokLtLynFjxowxtWrVcncZuerFF180TZo0cXcZbjdo0CBTrlw5k5qa6u5SbgsjN7fpypUr2rFjh9q2bevQ3rZtW23evNlNVSG3XLhwQZJUuHBhN1eSe1JSUvTBBx/o8uXLatiwobvLyXEDBgxQhw4ddP/997u7lFz1888/q2TJkgoLC1O3bt10+PBhd5eUo1auXKnw8HD985//VLFixXTvvffqnXfecXdZuerKlStavHixevXqle0/LJ3bCDe36fTp00pJSUn3S+bFixdP9wvmsBZjjKKiotSkSRNVr17d3eXkuD179qhAgQLy8fFRv379tHz5clWtWtXdZeWoDz74QD/88IOio6PdXUquatCggRYtWqTVq1frnXfeUUJCgho1aqQzZ864u7Qcc/jwYcXExKhChQpavXq1+vXrp+eee06LFi1yd2m5ZsWKFTp//rwiIyPdXcptc/vPL1jFjSnXGHPHJ1/c3MCBA/Xjjz/q22+/dXcpuaJSpUratWuXzp8/r08++UQRERHasGGDZQPOsWPHNGjQIH311Vfy9fV1dzm5ql27dvZ/16hRQw0bNlS5cuW0cOFCRUVFubGynJOamqrw8HBNmDBBknTvvfdq3759iomJcfgBZyubO3eu2rVrp5IlS7q7lNvGyM1tKlKkiDw8PNKN0pw8eTLdaA6s49///rdWrlypdevWqXTp0u4uJ1d4e3urfPnyCg8PV3R0tGrVqqU33njD3WXlmB07dujkyZOqW7euPD095enpqQ0bNujNN9+Up6enUlJS3F1i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GD8/P7N06VJjjDFjxowxtWrVcljP66+/bkJDQ+33IyIiTKdOnW66rZEjR5pKlSo5vCemT59uChQoYFJSUowx1943TZo0cVhPvXr1zIsvvuh034G8joOyQB7SsmVLxcTEOLQVLlzY/m9vb28tXrxYNWvWVGhoqNOziu677z7ZbDb7/YYNG2rKlClKSUnRgQMH5OnpqQYNGtgfDw4OVqVKlXTgwAF7W/78+VWuXDn7/ZCQEJ08eVKSdOrUKR07dky9e/fWM888Y++TnJysoKAgh1pq1qzpsA5JOnnypCpXrpyp50OS1q1bpwkTJmj//v1KTExUcnKy/v77b12+fFn+/v6ZXo8z5v8frrv++bpeVFSU+vTpo3fffVf333+//vnPfzo8LxkJDw/P1PYbNmxo/3fhwoXTvQ7Z4cCBA2rYsKHDPjZu3FiXLl3S8ePHdc8990hyfK0kx9ccuNNwWArIQ/z9/VW+fHmH2/XhRpI2b94sSTp79qzOnj2bpfWb6+be3Nh+/Zefl5eXw+M2m82+bGpqqqRrh6Z27dplv+3du1dbt251WO769aStP235zDh69Kjat2+v6tWr65NPPtGOHTs0ffp0Scr04ZubSQsSYWFhTh8fO3as9u3bpw4dOmjt2rWqWrWqli9ffsv13k7oSnue8uXLl+71cmWfb3xt09qu35bk/DXPymsF5CWEG+AO8uuvv2rIkCF65513dN9996lnz57pvoBuDBhbt25VhQoV5OHhoapVqyo5OVnfffed/fEzZ87o0KFDqlKlSqZqKF68uEqVKqXDhw+nC2IZhQRnvL29lZKSctM+27dvV3JysqZMmaL77rtPFStW1IkTJzK9jVtJmzdz//33Z9inYsWKGjJkiL766is98sgjmj9/fqbrv5XrX6tz587p0KFD9lGtokWLKiEhwSHg3DghOTM1VK1aVZs3b3ZYz+bNmxUQEKBSpUrdVv1AXkW4AfKQpKQkJSQkONxOnz4tSUpJSVGPHj3Utm1bPf3005o/f7727t2rKVOmOKzj2LFjioqK0sGDB7VkyRK99dZbGjRokCSpQoUK6tSpk5555hl9++232r17t7p3765SpUqpU6dOma5z7Nixio6O1htvvKFDhw5pz549mj9/vqZOnZrpdZQtW1aXLl3SmjVrdPr0af3555/p+pQrV07Jycl66623dPjwYb377ruaOXNmprdxvfPnzyshIUFHjx5VbGysHnvsMb3//vuKiYlxer2av/76SwMHDtT69et19OhRbdq0Sdu2bbOHwMzUfyvjxo3TmjVrtHfvXkVGRqpIkSL269a0aNFCp06d0qRJk/Trr79q+vTp+uKLLxyWL1u2rH788UcdPHhQp0+fdjqy079/fx07dkz//ve/9dNPP+nTTz/VmDFjFBUVpXz5+AqARblttg8ABxEREUZSululSpWMMca89NJLJiQkxJw+fdq+zIoVK4y3t7d98mjz5s1N//79Tb9+/UxgYKApVKiQGT58uMNk0rNnz5oePXqYoKAg4+fnZx544AFz6NAh++POJsouX77c3Pjn4r333jO1a9c23t7eplChQqZZs2Zm2bJlxpj0k1qNMebcuXNGklm3bp29rV+/fiY4ONhIMmPGjDHGpJ9QPHXqVBMSEmKvddGiRUaSOXfuXIb13uj659PX19eUK1fOREREmB07djj0u35dSUlJplu3bqZMmTLG29vblCxZ0gwcOND89ddfWarf2fORNqH4s88+M9WqVTPe3t6mXr16ZteuXQ7LxcTEmDJlyhh/f3/Ts2dP88orrzhMKD558qRp06aNKVCggP25dfbcr1+/3tSrV894e3ubEiVKmBdffNFcvXrV/njz5s3NoEGDHLbdqVMnExERcdPnFcirbMZkcBAewB2nRYsWql27dpZ+vgAArIYxSQAAYCmEGwAAYCkclgIAAJbCyA0AALAUwg0AALAUwg0AALAUwg0AALAUwg0AALAUwg0AALAUwg0AALAUwg0AALAUwg0AALCU/wc6gAkZxOdBxQAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from scipy.stats import expon\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Generate random numbers from exponential distribution\n",
    "data_expon = expon.rvs(scale=1, loc=0, size=1000)\n",
    "\n",
    "# Plotting the histogram\n",
    "plt.hist(data_expon, bins=100, density=True, alpha=0.6, color='r')\n",
    "plt.xlabel('Exponential Distribution')\n",
    "plt.ylabel('Frequency')\n",
    "plt.title('Histogram of Exponential Distribution')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "826428cf",
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}