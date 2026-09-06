{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNVnMU4xXI6mYsSkLbqz2aD",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/the-omar-project-portfolio/computational-core/blob/main/binary_search.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yr4pCwFCwzpD",
        "outputId": "14e6d151-0b28-438b-9419-efccd0640a91"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "6\n",
            "-1\n"
          ]
        }
      ],
      "source": [
        "def binary_search(array, target):\n",
        "  low = 0\n",
        "  high = len(array) - 1\n",
        "\n",
        "  while low <= high:\n",
        "    mid = low + (high - low) // 2\n",
        "\n",
        "    if array[mid] == target:\n",
        "      return mid\n",
        "    elif array[mid] > target:\n",
        "      high = mid - 1\n",
        "    elif array[mid] < target:\n",
        "      low = mid + 1\n",
        "  return -1\n",
        "\n",
        "array = [-1, 2, 5, 7, 10, 23, 45, 57]\n",
        "print(binary_search(array, 2))\n",
        "print(binary_search(array, 45))\n",
        "print(binary_search(array, 100))"
      ]
    }
  ]
}