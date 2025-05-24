{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/soone0801/20250503/blob/main/python/lesson4-1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "* def咖啡生產器(咖啡豆盤子(放咖啡豆-參數),水杯(放水-參數))⮕咖啡\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "vGXvOitmJP2O"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def caculate_bmi(height:int,weight:int)->float:\n",
        "    return weight / ((height/100) ** 2)\n",
        "def get_state(bmi:float)->str:\n",
        "    if bmi < 18.5:\n",
        "        return \"太瘦啦\"\n",
        "    elif bmi < 24:\n",
        "        return \"可以 正常\"\n",
        "    elif bmi < 27:\n",
        "        return \"小肥兒\"\n",
        "    else:\n",
        "        return \"媽的 肥仔\"\n",
        "\n",
        "height:int = int(input(\"請輸入身高(CM):\"))\n",
        "weight:int = int(input(\"請輸入體重(KG):\"))\n",
        "\n",
        "bmi = caculate_bmi(height,weight)\n",
        "print(f\"BMI = {bmi}\")\n",
        "print(get_state(bmi))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UBDuZKPLA668",
        "outputId": "5fe30752-933c-45cc-ba5d-1c6d3b2c0b9e"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "請輸入身高(CM):187\n",
            "請輸入體重(KG):74\n",
            "BMI = 21.161600274528865\n",
            "可以 正常\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uxI7x6BuDHIH",
        "outputId": "c9b9f6d3-62c0-48fa-ef61-df08e613c68f"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "name": "歡迎使用 Colab",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}