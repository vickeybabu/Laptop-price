{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "b4bdaeda",
   "metadata": {},
   "source": [
    "#### Import the libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f32a88b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd  # data preprocessing\n",
    "import numpy as np   # mathematical computation\n",
    "import matplotlib.pyplot as plt # visualization\n",
    "import seaborn as sns   # visualization"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "a66470d4",
   "metadata": {},
   "source": [
    "#### Read the dataset"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5e89957a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0</th>\n",
       "      <th>Company</th>\n",
       "      <th>TypeName</th>\n",
       "      <th>Ram</th>\n",
       "      <th>Weight</th>\n",
       "      <th>Price</th>\n",
       "      <th>Touchscreen</th>\n",
       "      <th>Ips</th>\n",
       "      <th>Cpu brand</th>\n",
       "      <th>HDD</th>\n",
       "      <th>SSD</th>\n",
       "      <th>Gpu brand</th>\n",
       "      <th>os</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>Apple</td>\n",
       "      <td>Ultrabook</td>\n",
       "      <td>8</td>\n",
       "      <td>1.37</td>\n",
       "      <td>71378.6832</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Intel Core i5</td>\n",
       "      <td>0</td>\n",
       "      <td>128</td>\n",
       "      <td>Intel</td>\n",
       "      <td>Mac</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>Apple</td>\n",
       "      <td>Ultrabook</td>\n",
       "      <td>8</td>\n",
       "      <td>1.34</td>\n",
       "      <td>47895.5232</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Intel Core i5</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Intel</td>\n",
       "      <td>Mac</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2</td>\n",
       "      <td>HP</td>\n",
       "      <td>Notebook</td>\n",
       "      <td>8</td>\n",
       "      <td>1.86</td>\n",
       "      <td>30636.0000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Intel Core i5</td>\n",
       "      <td>0</td>\n",
       "      <td>256</td>\n",
       "      <td>Intel</td>\n",
       "      <td>Others/No OS/Linux</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>Apple</td>\n",
       "      <td>Ultrabook</td>\n",
       "      <td>16</td>\n",
       "      <td>1.83</td>\n",
       "      <td>135195.3360</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Intel Core i7</td>\n",
       "      <td>0</td>\n",
       "      <td>512</td>\n",
       "      <td>AMD</td>\n",
       "      <td>Mac</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>4</td>\n",
       "      <td>Apple</td>\n",
       "      <td>Ultrabook</td>\n",
       "      <td>8</td>\n",
       "      <td>1.37</td>\n",
       "      <td>96095.8080</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Intel Core i5</td>\n",
       "      <td>0</td>\n",
       "      <td>256</td>\n",
       "      <td>Intel</td>\n",
       "      <td>Mac</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Unnamed: 0 Company   TypeName  Ram  Weight        Price  Touchscreen  Ips  \\\n",
       "0           0   Apple  Ultrabook    8    1.37   71378.6832            0    1   \n",
       "1           1   Apple  Ultrabook    8    1.34   47895.5232            0    0   \n",
       "2           2      HP   Notebook    8    1.86   30636.0000            0    0   \n",
       "3           3   Apple  Ultrabook   16    1.83  135195.3360            0    1   \n",
       "4           4   Apple  Ultrabook    8    1.37   96095.8080            0    1   \n",
       "\n",
       "       Cpu brand  HDD  SSD Gpu brand                  os  \n",
       "0  Intel Core i5    0  128     Intel                 Mac  \n",
       "1  Intel Core i5    0    0     Intel                 Mac  \n",
       "2  Intel Core i5    0  256     Intel  Others/No OS/Linux  \n",
       "3  Intel Core i7    0  512       AMD                 Mac  \n",
       "4  Intel Core i5    0  256     Intel                 Mac  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# df is a vraiable which stores dataframe\n",
    "df = pd.read_csv('laptop_price_data.csv')\n",
    "print(type(df))  # dataframe\n",
    "df.head()  # top 5 rows"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "966fcfc3",
   "metadata": {},
   "source": [
    "#### Shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b4a683bc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1302, 13)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape\n",
    "# rows = 1302,columns= 13"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "48c44fb3",
   "metadata": {},
   "source": [
    "## Data Preprocessing"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "1d24d8c5",
   "metadata": {},
   "source": [
    "#### 1) Handle the Null Values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a3e00c09",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Unnamed: 0     0\n",
       "Company        0\n",
       "TypeName       0\n",
       "Ram            0\n",
       "Weight         0\n",
       "Price          0\n",
       "Touchscreen    0\n",
       "Ips            0\n",
       "Cpu brand      0\n",
       "HDD            0\n",
       "SSD            0\n",
       "Gpu brand      0\n",
       "os             0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# isnulll()  returns True if a cell contains cnull values\n",
    "df.isnull().sum()\n",
    "# Returns sum of null values for each column"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b40eaf78",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1302"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Unnamed: 0'].nunique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "e3a903e4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Company', 'TypeName', 'Ram', 'Weight', 'Price', 'Touchscreen', 'Ips',\n",
       "       'Cpu brand', 'HDD', 'SSD', 'Gpu brand', 'os'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.drop('Unnamed: 0',axis=1,inplace=True)\n",
    "df.columns"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "076e724f",
   "metadata": {},
   "source": [
    "#### 2) Handle the duplicates"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "fc288372",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "30"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# dupliacted() returns True, if the rows is duplicated (repeated)\n",
    "df.duplicated().sum()\n",
    "# Returns the sum of all the entire duplicated rows"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "f49ff890",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# inpalce=True ensures that changes are reflected in the actual dataframe.\n",
    "df.drop_duplicates(inplace=True)\n",
    "df.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "7ed6a192",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1272, 12)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape\n",
    "# rows=1272,cols=12"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "a73d6b89",
   "metadata": {},
   "source": [
    "#### 3) Check the datatypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "9dce537f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Company         object\n",
       "TypeName        object\n",
       "Ram              int64\n",
       "Weight         float64\n",
       "Price          float64\n",
       "Touchscreen      int64\n",
       "Ips              int64\n",
       "Cpu brand       object\n",
       "HDD              int64\n",
       "SSD              int64\n",
       "Gpu brand       object\n",
       "os              object\n",
       "dtype: object"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "b15d4821",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['Company', 'TypeName', 'Cpu brand', 'Gpu brand', 'os'], dtype='object')\n",
      "Index(['Ram', 'Weight', 'Price', 'Touchscreen', 'Ips', 'HDD', 'SSD'], dtype='object')\n"
     ]
    }
   ],
   "source": [
    "cat_cols = df.dtypes[df.dtypes=='object'].index\n",
    "num_cols = df.dtypes[df.dtypes!='object'].index\n",
    "print(cat_cols)\n",
    "print(num_cols)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "61a315ff",
   "metadata": {},
   "source": [
    "### EDA - Exploratory Data Analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "4566789f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['Company', 'TypeName', 'Ram', 'Weight', 'Price', 'Touchscreen', 'Ips',\n",
      "       'Cpu brand', 'HDD', 'SSD', 'Gpu brand', 'os'],\n",
      "      dtype='object')\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Company</th>\n",
       "      <th>TypeName</th>\n",
       "      <th>Ram</th>\n",
       "      <th>Weight</th>\n",
       "      <th>Price</th>\n",
       "      <th>Touchscreen</th>\n",
       "      <th>Ips</th>\n",
       "      <th>Cpu brand</th>\n",
       "      <th>HDD</th>\n",
       "      <th>SSD</th>\n",
       "      <th>Gpu brand</th>\n",
       "      <th>os</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Apple</td>\n",
       "      <td>Ultrabook</td>\n",
       "      <td>8</td>\n",
       "      <td>1.37</td>\n",
       "      <td>71378.6832</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Intel Core i5</td>\n",
       "      <td>0</td>\n",
       "      <td>128</td>\n",
       "      <td>Intel</td>\n",
       "      <td>Mac</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Apple</td>\n",
       "      <td>Ultrabook</td>\n",
       "      <td>8</td>\n",
       "      <td>1.34</td>\n",
       "      <td>47895.5232</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Intel Core i5</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Intel</td>\n",
       "      <td>Mac</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>HP</td>\n",
       "      <td>Notebook</td>\n",
       "      <td>8</td>\n",
       "      <td>1.86</td>\n",
       "      <td>30636.0000</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>Intel Core i5</td>\n",
       "      <td>0</td>\n",
       "      <td>256</td>\n",
       "      <td>Intel</td>\n",
       "      <td>Others/No OS/Linux</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Apple</td>\n",
       "      <td>Ultrabook</td>\n",
       "      <td>16</td>\n",
       "      <td>1.83</td>\n",
       "      <td>135195.3360</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Intel Core i7</td>\n",
       "      <td>0</td>\n",
       "      <td>512</td>\n",
       "      <td>AMD</td>\n",
       "      <td>Mac</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Apple</td>\n",
       "      <td>Ultrabook</td>\n",
       "      <td>8</td>\n",
       "      <td>1.37</td>\n",
       "      <td>96095.8080</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Intel Core i5</td>\n",
       "      <td>0</td>\n",
       "      <td>256</td>\n",
       "      <td>Intel</td>\n",
       "      <td>Mac</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Company   TypeName  Ram  Weight        Price  Touchscreen  Ips  \\\n",
       "0   Apple  Ultrabook    8    1.37   71378.6832            0    1   \n",
       "1   Apple  Ultrabook    8    1.34   47895.5232            0    0   \n",
       "2      HP   Notebook    8    1.86   30636.0000            0    0   \n",
       "3   Apple  Ultrabook   16    1.83  135195.3360            0    1   \n",
       "4   Apple  Ultrabook    8    1.37   96095.8080            0    1   \n",
       "\n",
       "       Cpu brand  HDD  SSD Gpu brand                  os  \n",
       "0  Intel Core i5    0  128     Intel                 Mac  \n",
       "1  Intel Core i5    0    0     Intel                 Mac  \n",
       "2  Intel Core i5    0  256     Intel  Others/No OS/Linux  \n",
       "3  Intel Core i7    0  512       AMD                 Mac  \n",
       "4  Intel Core i5    0  256     Intel                 Mac  "
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "print(df.columns)\n",
    "df.head()"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "f10c20a0",
   "metadata": {},
   "source": [
    "### 1) Top 7 most bought laptop brands"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "b03c9951",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Dell         291\n",
       "Lenovo       289\n",
       "HP           268\n",
       "Asus         151\n",
       "Acer         101\n",
       "MSI           54\n",
       "Toshiba       47\n",
       "Apple         21\n",
       "Samsung        8\n",
       "Razer          7\n",
       "Mediacom       7\n",
       "Microsoft      6\n",
       "Xiaomi         4\n",
       "Vero           4\n",
       "Chuwi          3\n",
       "Google         3\n",
       "Fujitsu        3\n",
       "LG             3\n",
       "Huawei         2\n",
       "Name: Company, dtype: int64"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Company'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "63d17353",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAlkAAAHFCAYAAADBtOziAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAABAr0lEQVR4nO3dd3gUVf/+8XvTNiGNngQIhBp66EVUOgREiIgK0iI2QLCAiuBDs1B8RCyIja4IGI2IgIgCQRAQpAjS5KEjARRCAgiBJOf3hz/2yxJKEjJZkrxf1zXXtTvnzMxnzo7uzczsxGaMMQIAAEC2cnN1AQAAAHkRIQsAAMAChCwAAAALELIAAAAsQMgCAACwACELAADAAoQsAAAACxCyAAAALEDIAgAAsAAhC8gAm82WoSkuLs7SOuLi4m64/b59+95w+QMHDjj6jho16pp9+vTp4+hjlTFjxmj+/PkZ6nu55jfffNOyerLDjBkzZLPZ9Ouvv9607+TJkzVjxowMrzssLEzR0dFZLy4DduzYoVGjRunAgQOWbudGmjVrpurVq7ts+5k1atQoS/87Qe7n4eoCgNxg7dq1Tu9fffVVrVixQsuXL3eaX7VqVUvrqFOnTrpaJOmDDz7QrFmzdN9992VoPf7+/poxY4ZGjBghN7f/+7fW2bNnFRMTo4CAACUlJWVb3VcbM2aMunTpoqioKMu2cTubPHmyihYtanlwyowdO3Zo9OjRatasmcLCwlxdDpAnELKADGjUqJHT+2LFisnNzS3dfKsFBASk26YxRt27d1eZMmXUunXrDK3noYce0pQpU7Rs2TKnZebNm6fU1FRFRUXps88+y9baASulpqYqJSVFdrvd1aUADlwuBLLJqVOn1L9/f5UsWVJeXl4qV66cXn75ZSUnJzv1s9lsGjBggD766CNVqlRJdrtdVatW1dy5c7O03RUrVmjfvn165JFHnM5K3Uh4eLjuuOMOTZs2zWn+tGnT1LlzZwUGBqZbJi0tTW+88YYqV64su92u4sWLq1evXjpy5IhTv82bN6tDhw4qXry47Ha7SpQooXvuucfRz2az6dy5c5o5c6bjsmSzZs1uWnNaWppef/11lS5dWt7e3qpXr56WLVuWrt/q1avVsmVL+fv7q0CBArrjjju0aNEipz7Xu8xz+ZLflZfMkpOTNXjwYAUHB6tAgQK6++67tXHjxutewjtz5oz69eunokWLqkiRIurcubOOHj3qaA8LC9P27du1cuVKx/5n9szRhQsXNHjwYNWqVUuBgYEqXLiwGjdurG+++SZd34wcbzNmzNADDzwgSWrevLmjrisvaU6bNk0RERHy9vZW4cKFdd9992nnzp1O24qOjpafn5+2b9+uli1bytfXV8WKFdOAAQP0zz//ZHj/Vq1apUaNGsnHx0clS5bU8OHDlZqa6mi/fAn5jTfe0GuvvaayZcvKbrdrxYoVWRqbTz/9VFWqVFGBAgUUERGhhQsXpuu7aNEi1apVS3a7XWXLlr3u5euYmBg1bNhQgYGBKlCggMqVK6c+ffpkeN+RxxgAmda7d2/j6+vreH/+/HlTs2ZN4+vra958802zdOlSM3z4cOPh4WHat2/vtKwkExoaaqpWrWrmzJljFixYYCIjI40kExMTk+laHn74YePm5mYOHjx407779+83ksx///tfM3XqVOPt7W1OnTpljDFm165dRpJZvny5eeqpp8zV/3t44oknjCQzYMAAs2TJEvPhhx+aYsWKmdDQUPPXX38ZY4w5e/asKVKkiKlXr5754osvzMqVK828efNM3759zY4dO4wxxqxdu9b4+PiY9u3bm7Vr15q1a9ea7du337Tm0NBQc+edd5qvvvrKxMTEmPr16xtPT0+zZs0aR9+4uDjj6elp6tata+bNm2fmz59v2rRpY2w2m5k7d66j38iRI9PtnzHGTJ8+3Ugy+/fvd8zr1q2bcXNzMy+99JJZunSpefvtt01oaKgJDAw0vXv3TrdsuXLlzMCBA833339vpkyZYgoVKmSaN2/u6Ldp0yZTrlw5U7t2bcf+b9q06YafW5kyZZy2dfr0aRMdHW0+/fRTs3z5crNkyRLz/PPPGzc3NzNz5kynZTNyvJ04ccKMGTPGSDLvv/++o64TJ04YY4yjrVu3bmbRokVm1qxZply5ciYwMND88ccfjm317t3beHl5mdKlS5vXX3/dLF261IwaNcp4eHiYDh063HAfjTGmadOmpkiRIqZEiRLm3XffNd9//715+umnjSTz1FNPOfpdPiZKlixpmjdvbr788kuzdOlSs3///kyPTVhYmGnQoIH54osvzOLFi02zZs2Mh4eH2bt3r6Pfjz/+aNzd3c2dd95pYmNjHcdf6dKlnY6jNWvWGJvNZrp27WoW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ae/evY5+NWvWdFouJCREJ06ckCTt3LlToaGhjoAlSVWrVlXBggW1c+dOSVLXrl118OBBrVu3TpI0e/Zs1apVS1WrVnWso3HjxrLZbI51NGnSRGfPntWRI0euWfvQoUOVmJjomA4fPnyrwwEAAHKR2/pMVlpamu69916NHz8+XVtISIjjtaenp1ObzWZTWlqapH8vF14Zji67cn5ISIiaN2+uzz//XI0aNdKcOXP05JNPXrPvlfMub+ta7Ha77HZ7RnYTAADkQbf1maw6depo+/btCgsLU4UKFZwmX1/fDK2jatWqOnTokNOZpB07digxMVFVqlRxzOvevbvmzZuntWvXau/everatavTOtasWeMIVpK0Zs0a+fv7q2TJktmwpwAAIK+5bUJWYmKitmzZ4jQ9+eSTOnXqlLp166b169dr3759Wrp0qfr06aPU1NQMrbdVq1aqWbOmunfvrk2bNmn9+vXq1auXmjZtqnr16jn6de7cWUlJSerXr5+aN2/uFJ769++vw4cPa+DAgdq1a5e++eYbjRw5UoMGDbrm/VgAAAC3zeXCuLg41a5d22le79699fPPP2vIkCFq27atkpOTVaZMGUVGRmY43NhsNs2fP18DBw7U3XffLTc3N0VGRuq9995z6hcQEKB7771XMTExmjZtmlNbyZIltXjxYr3wwguKiIhQ4cKF9eijj+o///nPre00AADIs2zmymtgsExSUpICAwP1+9Aq8vd2d3U5AADkaqVHbMuR7Vz+/k5MTFRAQECmluVaFwAAgAUIWQAAABYgZAEAAFiAkAUAAGABQhYAAIAFCFkAAAAWIGQBAABYgJAFAABgAUIWAACABQhZAAAAFiBkAQAAWICQBQAAYAFCFgAAgAUIWQAAABbwcHUB+U3oS+sUEBDg6jIAAIDFOJMFAABgAUIWAACABQhZAAAAFiBkAQAAWICQBQAAYAFCFgAAgAUIWQAAABYgZAEAAFiAkAUAAGABQhYAAIAF+LM6Oaz1h63l4cOwAwByp58H/uzqEnINzmQBAABYgJAFAABgAUIWAACABQhZAAAAFiBkAQAAWICQBQAAYAFCFgAAgAUIWQAAABYgZAEAAFiAkAUAAGABQhYAAIAFCFkAAAAWIGQBAABYgJAFAABgAUIWAACABQhZAAAAFsj3ISs6OlpRUVHp5sfFxclms+n06dOO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oqCgIEnSgAEDdOrUKX3++ef67rvvdP/996tSpUpq06aNoqKidMcdd0j693Jh8+bNlZCQoIIFC0r693Jh7dq1tX//foWFhWnKlCnq16+fGjRooFatWun+++9XzZo1r1vPtc5khYaGck8WkIdwTxaQ9+X4PVlpaWkZmnIqYEn/nsVKSUlRyZIl5eHhIQ8PD33wwQeKjY1VQkKC2rVrp4MHD+rZZ5/V0aNH1bJlSz3//POS/i80Xpk3L1265LT+xx57TPv27VPPnj21bds21atXT++9995167Hb7QoICHCaAABA/pGlkHW7SUlJ0axZszRhwgRt2bLFMf32228qU6aMZs+eLUkqVqyYoqOj9dlnn+ntt9/Wxx9/7JgvyfH3GKV/z2RdLTQ0VH379lVsbKwGDx6sTz75xPqdAwAAuVKWr1utX79ecXFxOnHihNLS0pza3nrrrVsuLDMWLlyohIQEPfroowoMDHRq69Kli6ZOnaoTJ06obt26qlatmpKTk7Vw4UJVqVJF0r9/5Do0NFSjRo3Sa6+9pj179mjChAlO63n22WfVrl07VapUSQkJCVq+fLljeQAAgKtlKWSNGTNG//nPfxQeHq6goCDZbDZH25Wvc8rUqVPVqlWrdAFLku6//36NGTNG9913n4YOHaoDBw7Ix8dHd911l+bOnStJ8vT01Jw5c9SvXz9FRESofv36eu211/TAAw841pOamqqnnnpKR44cUUBAgCIjIzVx4sQc20cAAJC7ZOnG96CgII0fP17R0dEWlJQ38TBSIO/hxncg78vxG9/d3NzUpEmTrCwKAACQL2QpZD333HN6//33s7sWAACAPCNL162ef/553XPPPSpfvryqVq0qT09Pp/bY2NhsKQ4AACC3ylLIGjhwoFasWKHmzZurSJEiLrnZHQAA4HaWpZA1a9YsffXVV7rnnnuyux4AAIA8IUv3ZBUuXFjly5fP7loAAADyjCyFrFGjRmnkyJH6559/srseAACAPCFLlwvfffdd7d27V0FBQQoLC0t34/umTZuypTgAAIDcKkshKyoqKpvLAAAAyFuyFLJGjhyZ3XUAAADkKbf09102btyonTt3ymazqWrVqqpdu3Z21QUAAJCrZSlknThxQl27dlVcXJwKFiwoY4wSExPVvHlzzZ07V8WKFcvuOgEAAHKVLP26cODAgUpKStL27dt16tQpJSQk6Pfff1dSUpKefvrp7K4RAAAg18nSmawlS5boxx9/VJUqVRzzqlatqvfff19t2rTJtuIAAAByqyyFrLS0tHSPbZAkT09PpaWl3XJRedmdS75TQECAq8sAAAAWy9LlwhYtWuiZZ57R0aNHHfP+/PNPPffcc2rZsmW2FQcAAJBbZSlkTZo0SWfOnFFYWJjKly+vChUqqGzZsjpz5ozee++97K4RAAAg18nS5cLQ0FBt2rRJP/zwg3bt2iVjjKpWrapWrVpld30AAAC5UqbOZC1fvlxVq1ZVUlKSJKl169YaOHCgnn76adWvX1/VqlXTqlWrLCkUAAAgN8lUyHr77bf1+OOPX/PG7cDAQD355JN66623sq04AACA3CpTIeu3335TZGTkddvbtGmjjRs33nJRAAAAuV2mQtbx48ev+eiGyzw8PPTXX3/dclEAAAC5XaZCVsmSJbVt27brtm/dulUhISG3XBQAAEBul6mQ1b59e40YMUIXLlxI13b+/HmNHDlSHTp0yLbiAAAAciubMcZktPPx48dVp04dubu7a8CAAQoPD5fNZtPOnTv1/vvvKzU1VZs2bVJQUJCVNedKSUlJCgwMVGJiIk98BwAgl7iV7+9MPScrKChIa9asUb9+/TR06FBdzmc2m01t27bV5MmTCVg38dGw7+RjL+DqMgANmHCvq0sAgDwt0w8jLVOmjBYvXqyEhAT973//kzFGFStWVKFChayoDwAAIFfK0hPfJalQoUKqX79+dtYCAACQZ2TpbxcCAADgxghZAAAAFiBkAQAAWICQBQAAYAFCFgAAgAUIWQAAABYgZAEAAFiAkAUAAGABQhYAAIAFCFkAAAAWIGQBAABYgJAFAABgAUIWAACABfJsyFqzZo3c3d0VGRnp6lIAAEA+lGdD1rRp0zRw4ECtXr1ahw4dsmw7qampSktLs2z9AAAgd8qTIevcuXP64osv1K9fP3Xo0EEzZsxwal+wYIHq1asnb29vFS1aVJ07d3a0Xbx4US+++KJKliwpX19fNWzYUHFxcY72GTNmqGDBglq4cKGqVq0qu92ugwcP5tCeAQCA3CJPhqx58+YpPDxc4eHh6tGjh6ZPny5jjCRp0aJF6ty5s+655x5t3rxZy5YtU7169RzLPvLII/r55581d+5cbd26VQ888IAiIyO1Z88eR59//vlHY8eO1ZQpU7R9+3YVL148x/cRAADc3jxcXYAVpk6dqh49ekiSIiMjdfbsWS1btkytWrXS66+/rq5du2r06NGO/hEREZKkvXv3as6cOTpy5IhKlCghSXr++ee1ZMkSTZ8+XWPGjJEkXbp0SZMnT3Ysdy3JyclKTk52vE9KSsr2/QQAALevPHcma/fu3Vq/fr26du0qSfLw8NBDDz2kadOmSZK2bNmili1bXnPZTZs2yRijSpUqyc/PzzGtXLlSe/fudfTz8vJSzZo1b1jH2LFjFRgY6JhCQ0OzaQ8BAEBukOfOZE2dOlUpKSkqWbKkY54xRp6enkpISJCPj891l01LS5O7u7s2btwod3d3pzY/Pz/Hax8fH9lsthvWMXToUA0aNMjxPikpiaAFAEA+kqdCVkpKimbNmqUJEyaoTZs2Tm3333+/Zs+erZo1a2rZsmV65JFH0i1fu3Ztpaam6sSJE7rrrrtuqRa73S673X5L6wAAALlXngpZCxcuVEJCgh599FEFBgY6tXXp0kVTp07VxIkT1bJlS5UvX15du3ZVSkqKvvvuO7344ouqVKmSunfvrl69emnChAmqXbu2/v77by1fvlw1atRQ+/btXbRnAAAgt8lT92RNnTpVrVq1ShewpH/PZG3ZskUBAQGKiYnRggULVKtWLbVo0UK//PKLo9/06dPVq1cvDR48WOHh4erYsaN++eUXLvUBAIBMsZnLzzaApZKSkhQYGKg3nporH3sBV5cDaMCEe11dAgDc9i5/fycmJiogICBTy+apM1kAAAC3C0IWAACABQhZAAAAFiBkAQAAWICQBQAAYAFCFgAAgAUIWQAAABYgZAEAAFiAkAUAAGABQhYAAIAFCFkAAAAWIGQBAABYgJAFAABgAUIWAACABQhZAAAAFvBwdQH5zZNj2ikgIMDVZQAAAItxJgsAAMAChCwAAAALELIAAAAsQMgCAACwACELAADAAoQsAAAACxCyAAAALEDIAgAAsAAhCwAAwAI88T2H/ffxnvL29HR1GXnSy5996eoSAABw4EwWAACABQhZAAAAFiBkAQAAWICQBQAAYAFCFgAAgAUIWQAAABYgZAEAAFiAkAUAAGABQhYAAIAFCFkAAAAWIGQBAABYgJAFAABgAUIWAACABQhZAAAAFiBkAQAAWICQBQAAYIF8E7Kio6Nls9nUt2/fdG39+/eXzWZTdHS0JOnEiRN68sknVbp0adntdgUHB6tt27Zau3atY5mwsDC9/fbbOVQ9AADIbfJNyJKk0NBQzZ07V+fPn3fMu3DhgubMmaPSpUs75t1///367bffNHPmTP3xxx9asGCBmjVrplOnTrmibAAAkAt5uLqAnFSnTh3t27dPsbGx6t69uyQpNjZWoaGhKleunCTp9OnTWr16teLi4tS0aVNJUpkyZdSgQQOX1Q0AAHKffHUmS5IeeeQRTZ8+3fF+2rRp6tOnj+O9n5+f/Pz8NH/+fCUnJ7uiRAAAkAfku5DVs2dPrV69WgcOHNDBgwf1888/q0ePHo52Dw8PzZgxQzNnzlTBggXVpEkTDRs2TFu3bs3UdpKTk5WUlOQ0AQCA/CPfhayiRYvqnnvu0cyZMzV9+nTdc889Klq0qFOf+++/X0ePHtWCBQvUtm1bxcXFqU6dOpoxY0aGtzN27FgFBgY6ptDQ0GzeEwAAcDvLdyFLkvr06eM4W3XlpcIreXt7q3Xr1hoxYoTWrFmj6OhojRw5MsPbGDp0qBITEx3T4cOHs6t8AACQC+TLkBUZGamLFy/q4sWLatu2bYaWqVq1qs6dO5fhbdjtdgUEBDhNAAAg/8hXvy68zN3dXTt37nS8vtLJkyf1wAMPqE+fPqpZs6b8/f3166+/6o033lCnTp1cUS4AAMiF8mXIknTdM0t+fn5q2LChJk6cqL179+rSpUsKDQ3V448/rmHDhuVwlQAAILeyGWOMq4vID5KSkhQYGKj/PNhR3p6eri4nT3r5sy9dXQIAII+5/P2dmJiY6Vt/8uU9WQAAAFYjZAEAAFiAkAUAAGABQhYAAIAFCFkAAAAWIGQBAABYgJAFAABgAUIWAACABQhZAAAAFiBkAQAAWICQBQAAYAFCFgAAgAUIWQAAABYgZAEAAFiAkAUAAGABmzHGuLqI/CApKUmBgYFKTExUQECAq8sBAAAZcCvf35zJAgAAsAAhCwAAwAKELAAAAAsQsgAAACxAyAIAALAAIQsAAMAChCwAAAALELIAAAAsQMgCAACwgIerC8hvdv93pfy8fV1dRq5R5eUWri4BAIAs4UwWAACABQhZAAAAFiBkAQAAWICQBQAAYAFCFgAAgAUIWQAAABYgZAEAAFiAkAUAAGABQhYAAIAFCFkAAAAWIGQBAABYgJAFAABgAUIWAACABQhZAAAAFiBkAQAAWCBPhqywsDC9/fbb120/cOCAbDabtmzZIkmKi4uTzWbT6dOnc6Q+AACQ97ksZNlsthtO0dHRlm07NDRU8fHxql69umXbAAAA+ZuHqzYcHx/veD1v3jyNGDFCu3fvdszz8fGxbNvu7u4KDg62bP0AAAAuO5MVHBzsmAIDA2Wz2Zzmff755ypfvry8vLwUHh6uTz/91Gn5UaNGqXTp0rLb7SpRooSefvppp/Z//vlHffr0kb+/v0qXLq2PP/7Y0Xb15cLLfv75Z0VERMjb21sNGzbUtm3bHG0nT55Ut27dVKpUKRUoUEA1atTQnDlzsn9gAABAnnBb3pP19ddf65lnntHgwYP1+++/68knn9QjjzyiFStWSJK+/PJLTZw4UR999JH27Nmj+fPnq0aNGk7rmDBhgurVq6fNmzerf//+6tevn3bt2nXD7b7wwgt68803tWHDBhUvXlwdO3bUpUuXJEkXLlxQ3bp1tXDhQv3+++964okn1LNnT/3yyy/XXFdycrKSkpKcJgAAkH/cliHrzTffVHR0tPr3769KlSpp0KBB6ty5s958801J0qFDhxQcHKxWrVqpdOnSatCggR5//HGndbRv3179+/dXhQoVNGTIEBUtWlRxcXE33O7IkSPVunVr1ahRQzNnztTx48f19ddfS5JKliyp559/XrVq1VK5cuU0cOBAtW3bVjExMddc19ixYxUYGOiYQkNDb31gAABArnFbhqydO3eqSZMmTvOaNGminTt3SpIeeOABnT9/XuXKldPjjz+ur7/+WikpKU79a9as6Xh9+VLkiRMnbrjdxo0bO14XLlxY4eHhjm2mpqbq9ddfV82aNVWkSBH5+flp6dKlOnTo0DXXNXToUCUmJjqmw4cPZ3wAAABArndbhizp32B0JWOMY15oaKh2796t999/Xz4+Purfv7/uvvtux6U9SfL09Ey3vrS0tCzXMWHCBE2cOFEvvviili9fri1btqht27a6ePHiNZez2+0KCAhwmgAAQP5xW4asKlWqaPXq1U7z1qxZoypVqjje+/j4qGPHjnr33XcVFxentWvXOt2onhXr1q1zvE5ISNAff/yhypUrS5JWrVqlTp06qUePHoqIiFC5cuW0Z8+eW9oeAADIu1z2CIcbeeGFF/Tggw+qTp06atmypb799lvFxsbqxx9/lCTN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3xnX6zh58qQOHz6skJAQSYyh9O+/9AcMGKDY2FgtX75cZcuWdWrnWLy5m43htXAs3pwxRsnJyTl/DGbxRn1kwty5c42np6eZOnWq2bFjh3n22WeNr6+vOXDggKtLuy0NHjzYxMXFmX379pl169aZDh06GH9/f8d4jRs3zgQGBprY2Fizbds2061bNxMSEmKSkpJcXLnrnDlzxmzevNls3rzZSDJvvfWW2bx5szl48KAxJmNj1rdvX1OqVCnz448/mk2bNpkWLVqYiIgIk5KS4qrdylE3GsMzZ86YwYMHmzVr1pj9+/ebFStWmMaNG5uSJUsyhlfo16+fCQwMNHFxcSY+Pt4x/fPPP44+HIs3drMx5Fi8uaFDh5qffvrJ7N+/32zdutUMGzbMuLm5maVLlxpjcvYYJGTlkPfff9+UKVPGeHl5mTp16jj9HBfOHnroIRMSEmI8PT1NiRIlTOfOnc327dsd7WlpaWbkyJEmODjY2O12c/fdd5tt27a5sGLXW7FihZGUburdu7cxJmNjdv78eTNgwABTuHBh4+PjYzp06GAOHTrkgr1xjRuN4T///GPatGljihUrZjw9PU3p0qVN7969041Pfh/Da42fJDN9+nRHH47FG7vZGHIs3lyfPn0c37fFihUzLVu2dAQsY3L2GLQZY0zmzn0BAADgZrgnCwAAwAKELAAAAAsQsgAAACxAyAIAALAAIQsAAMAChCwAAAALELIAAAAsQMgCAACwACELAFzowIEDstls2rJli6tLAZDNCFkAAAAWIGQByNfS0tI0fvx4VahQQXa7XaVLl9brr78uSdq2bZtatGghHx8fFSlSRE888YTOnj3rWLZZs2Z69tlnndYXFRWl6Ohox/uwsDCNGTNGffr0kb+/v0qXLq2PP/7Y0V62bFlJUu3atWWz2dSsWTPL9hVAziJkAcjXhg4dqvHjx2v48OHasWOHPv/8cwUFBemff/5RZGSkChUqpA0bNigmJkY//vijBgwYkOltTJgwQfXq1dPmzZvVv39/9evXT7t27ZIkrV+/XpL0448/Kj4+XrGxsdm6fwBcx8PVBQCAq5w5c0bvvPOOJk2apN69e0uSypcvrzvvvFOffPKJzp8/r1mzZsnX11eSNGnSJN17770aP368goKCMryd9u3bq3///pKkIUOGaOLEiYqLi1PlypVVrFgxSVKRIkUUHByczXsIwJU4kwUg39q5c6eSk5PVsmXLa7ZFREQ4ApYkNWnSRGlpadq9e3emtlOzZk3Ha5vNpuDgYJ04cSLrhQPIFQhZAPItHx+f67YZY2Sz2a7Zdnm+m5ubjDFObZcuXUrX39PTM93yaWlpmS0XQC5DyAKQb1WsWFE+Pj5atmxZuraqVatqy5YtOnfunGPezz//LDc3N1WqVEmSVKxYMcXHxzvaU1NT9fvvv2eqBi8vL8eyAPIWQhaAfMvb21tDhgzRiy++qFmzZmnv3r1at26dpk6dqu7du8vb21u9e/fW77//rhUrVmjgwIHq2bOn436sFi1aaNGiRVq0aJF27dql/v376/Tp05mqoXjx4vLx8dGSJUt0/PhxJSYmWrCnAFyBkAUgXxs+fLgGDx6sESNGqEqVKnrooYd04sQJFShQQN9//71OnTql+vXrq0uXLmrZsqUmTZrkWLZPnz7q3bu3evXqpaZNm6ps2bJq3rx5prbv4eGhd999Vx999JFKlCihTp06ZfcuAnARm7n6hgIAAADcMs5kAQAAWICQBQAAYAFCFgAAgAUIWQAAABYgZAEAAFiAkAUAAGABQhYAAIAFCFkAAAAWIGQBAABYgJAFAABgAUIWAACABQhZAAAAFvh/36cPo5zGEQEAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(y = df['Company'], order=df['Company'].value_counts()[:7].sort_values(ascending=False).index)\n",
    "plt.title('Top 7 Most bought laptop brands')\n",
    "plt.show()"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "905ccc21",
   "metadata": {},
   "source": [
    "#### Inference\n",
    "1) Dell and Lenovo are the most bought laptops."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "d491aabe",
   "metadata": {},
   "source": [
    "### Count of different laptop types"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "241e42e8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Notebook              705\n",
       "Gaming                205\n",
       "Ultrabook             194\n",
       "2 in 1 Convertible    116\n",
       "Workstation            29\n",
       "Netbook                23\n",
       "Name: TypeName, dtype: int64"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['TypeName'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "730fbdf3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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BE4AAABYisAJAAAASxE4AQAAYCkCJwAAACxF4AQAAIClCJwAAACwFIETAAAAliJwAgAAwFIETgAAAFiKwAkAAABLETgBAABgKQInAAAALEXgBAAAgKUInAAAALAUgRMAAACWInDmckFBQXrrrbcsP47NZtOyZcssPw4AALj7EDgtFhERIZvNpjfeeMOhfdmyZbLZbJnez+0KjgAAANmNwHkbuLm5afz48frzzz9zuhQAAIDbjsB5GzRp0kR+fn4aN25cun2WLFmiihUrytXVVUFBQZo8ebJ9XVhYmI4cOaKBAwfKZrM5zIxu3rxZDRo0kLu7uwICAtSvXz9dvHjRYd/nz59Xp06d5OXlJX9/f02bNs1h/dGjR9WqVSt5eXnJx8dH7du31++//+7QZ8aMGSpTpoxcXFwUEhKiuXPnZnjOo0aNUvHixRUTE/NvwwMAAHI5AudtkD9/fo0dO1bTpk3Tb7/9lmp9dHS02rdvr44dO2r37t0aMWKEhg0bpjlz5kiSli5dqpIlS2rUqFGKj49XfHy8JGn37t1q1qyZ2rZtq127dumzzz7Txo0b1adPH4f9T5w4UVWqVNGOHTs0dOhQDRw4UGvWrJEkGWPUunVrnT17Vhs2bNCaNWt04MABdejQwb79559/rv79+2vQoEHas2ePnn32WT311FNav359qnMxxqh///768MMPtXHjRt13331pjsnVq1eVmJjosAAAgNzJZowxOV1EbhYREaFz585p2bJlqlOnjipUqKAPP/xQy5YtU5s2bWSMUefOnXX69Gl988039u1eeuklrVixQnv37pX013c4BwwYoAEDBtj7dO3aVe7u7po1a5a9bePGjWrYsKEuXrwoNzc3BQUFqXz58vr666/tfTp27KjExEStXLlSa9asUfPmzXXo0CEFBARIkn7++WdVrFhRW7duVa1atVSvXj1VrFhR7733nn0f7du318WLF7VixQpJf100tGjRIn3xxRfavn271qxZo5IlS6Y7LiNGjNDIkSNTtVftO1P5Xd2zOMoAACA90RO7WrbvxMRE+fr6KiEhQT4+Pun2Y4bzNho/frwiIyP1888/O7THxsaqXr16Dm316tVTXFycbty4ke7+oqOjNWfOHHl5edmXZs2aKTk5WYcOHbL3q1OnjsN2derUUWxsrP3YAQEB9rApSRUqVFCBAgUc+qRVX8r6FAMHDtSWLVv0/fffZxg2JWno0KFKSEiwL8eOHcuwPwAAuHsROG+jBg0aqFmzZnrllVcc2o0xqa5Yz8zEc3Jysp599lnFxMTYl59++klxcXEqU6ZMhtumHC+tY6fVnlZ9/2xr2rSpjh8/rtWrV/9r7a6urvLx8XFYAABA7uSU0wXkNePGjVO1atUUHBxsb6tQoYI2btzo0G/z5s0KDg5W/vz5JUkuLi6pZjurV6+uvXv3qmzZshke84cffkj1ODQ01H7so0eP6tixYw4fqSckJKh8+fKSpPLly2vjxo3q2vXvKfnNmzfb16d47LHH9Oijj6pTp07Knz+/Onbs+K/jAQAAcj8C521WpUoVde7c2eFK8UGDBqlWrVoaPXq0OnTooC1btmj69Ol699137X2CgoL03XffqWPHjnJ1dVWRIkU0ZMgQ1a5dW71799YzzzwjT09PxcbGas2aNQ7737RpkyZMmKDWrVtrzZo1WrRokf27l02aNLHX9NZbbykpKUm9evVSw4YNVbNmTUnSiy++qPbt26t69epq3LixvvzySy1dulRr165NdX5t2rTR3Llz1aVLFzk5Oaldu3ZWDSUAALhL8JF6Dhg9erTDR+bVq1fXwoULtWDBAlWqVEmvv/66Ro0apYiICHufUaNG6fDhwypTpoyKFi0q6a/wumHDBsXFxenBBx9UtWrVNGzYMJUoUcLheIMGDVJ0dLSqVaum0aNHa/LkyWrWrJmkv38hqGDBgmrQoIGaNGmie++9V5999pl9+9atW+vtt9/WxIkTVbFiRc2aNUuzZ89WWFhYmufXrl07RUZGqkuXLlq6dGk2jRoAALhbcZU67ggpV7lxlToAANmLq9QBAACQ6xE4AQAAYCkCJwAAACxF4AQAAIClCJwAAACwFIETAAAAliJwAgAAwFIETgAAAFiKwAkAAABLETgBAABgKQInAAAALEXgBAAAgKUInAAAALAUgRMAAACWInACAADAUgROAAAAWIrACQAAAEsROAEAAGApp5wuALjZd//3hHx8fHK6DAAAkI2Y4QQAAIClCJwAAACwFIETAAAAliJwAgAAwFIETgAAAFiKwAkAAABLETgBAABgKQInAAAALEXgBAAAgKUInAAAALAUgRMAAACW4rfUcUc59kZtebvlz+kycIcq9frunC4BAHALmOEEAACApQicAAAAsBSBEwAAAJYicAIAAMBSBE4AAABYisAJAAAASxE4AQAAYCkCJwAAACxF4AQAAIClCJwAAACwFIETAAAAliJwAgAAwFIETgAAAFiKwAkAAABLETgBAABgKQInAAAALEXgBAAAgKUInAAAALAUgROpBAUF6a233srpMgAAQC5B4LxDnTx5Uv3791fZsmXl5uam4sWLq379+po5c6YuXbpk6bG3bdumnj17WnoMAACQdzjldAFI7eDBg6pXr54KFCigsWPHqnLlykpKStKvv/6qjz76SP7+/nrssccsO37RokUt2zcAAMh7mOG8A/Xq1UtOTk7avn272rdvr/Lly6ty5cr63//+pxUrVujRRx+VJE2ZMkWVK1eWp6enAgIC1KtXL124cMG+nzlz5qhAgQL66quvFBISIg8PD7Vr104XL15UZGSkgoKCVLBgQfXt21c3btywb/fPj9RtNps++OADtWnTRh4eHipXrpyWL1/uUPPy5ctVrlw5ubu7Kzw8XJGRkbLZbDp37pylYwUAAO58BM47zJkzZ/TNN9+od+/e8vT0TLOPzWaTJOXLl09Tp07Vnj17FBkZqXXr1umll15y6Hvp0iVNnTpVCxYs0KpVqxQVFaW2bdtq5cqVWrlypebOnav33ntPixcvzrCukSNHqn379tq1a5datGihzp076+zZs5Kkw4cPq127dmrdurViYmL07LPP6tVXX82G0QAAALkBgfMOs3//fhljFBIS4tBepEgReXl5ycvLS0OGDJEkDRgwQOHh4SpdurQaNWqk0aNHa+HChQ7bXb9+XTNmzFC1atXUoEEDtWvXThs3btSHH36oChUqqGXLlgoPD9f69eszrCsiIkJPPPGEypYtq7Fjx+rixYvaunWrJGnmzJkKCQnRxIkTFRISoo4dOyoiIiLD/V29elWJiYkOCwAAyJ0InHeolFnMFFu3blVMTIwqVqyoq1evSpLWr1+vpk2b6p577pG3t7e6du2qM2fO6OLFi/btPDw8VKZMGfvj4sWLKygoSF5eXg5tp06dyrCeKlWq2P/29PSUt7e3fZt9+/apVq1aDv3vv//+DPc3btw4+fr62peAgIAM+wMAgLsXgfMOU7ZsWdlsNv3yyy8O7ffee6/Kli0rd3d3SdKRI0fUokULVapUSUuWLFF0dLTeeecdSX/NaqZwdnZ22I/NZkuzLTk5OcO6MtrGGJMqIBtjMtzf0KFDlZCQYF+OHTuWYX8AAHD3InDeYQoXLqymTZtq+vTpDjOV/7R9+3YlJSVp8uTJql27toKDg3XixInbWOnfQkNDtW3btlT1ZcTV1VU+Pj4OCwAAyJ0InHegd999V0lJSapZs6Y+++wzxcbGat++fZo3b55++eUX5c+fX2XKlFFSUpKmTZumgwcPau7cuZo5c2aO1Pvss8/ql19+0ZAhQ/Trr79q4cKFmjNnjqTUXw0AAAB5D4HzDlSmTBnt3LlTTZo00dChQ1W1alXVrFlT06ZN0+DBgzV69Gjdd999mjJlisaPH69KlSrpk08+0bhx43Kk3tKlS2vx4sVaunSpqlSpohkzZtivUnd1dc2RmgAAwJ3DZv7ty3bALRgzZoxmzpyZ6e9mJiYmytfXV3uGlpe3W36Lq8PdqtTru3O6BADATVLevxMSEjL8ehy/NIRs8e6776pWrVoqXLiwNm3apIkTJ6pPnz45XRYAALgDEDiRLeLi4vR///d/Onv2rEqVKqVBgwZp6NChOV0WAAC4AxA4kS3efPNNvfnmmzldBgAAuANx0RAAAAAsReAEAACApQicAAAAsBSBEwAAAJYicAIAAMBSBE4AAABYisAJAAAASxE4AQAAYCkCJwAAACxF4AQAAIClCJwAAACwFIETAAAAliJwAgAAwFIETgAAAFiKwAkAAABLOeV0AcDNAl7+QT4+PjldBgAAyEbMcAIAAMBSBE4AAABYisAJAAAASxE4AQAAYCkCJwAAACxF4AQAAIClCJwAAACwFIETAAAAliJwAgAAwFIETgAAAFiKwAkAAABL8VvquKM0ndlUTu68LPOyTX035XQJAIBsxgwnAAAALEXgBAAAgKUInAAAALAUgRMAAACWInACAADAUgROAAAAWIrACQAAAEsROAEAAGApAicAAAAsReAEAACApQicAAAAsBSBEwAAAJYicAIAAMBSBE4AAABYisAJAAAASxE4AQAAYCkCJwAAACxF4AQAAIClCJwAAACwFIEzB40YMUL33XefZfsPCwvTgAEDLNt/iqCgIL311luWHwcAANydbilwJiUlae3atZo1a5bOnz8vSTpx4oQuXLiQrcXdzdILe8uWLZPNZktzm4iICLVu3drawgAAAG4zp6xucOTIET388MM6evSorl69qqZNm8rb21sTJkzQlStXNHPmTCvqxE2uX78uZ2fnnC4DAAAgU7I8w9m/f3/VrFlTf/75p9zd3e3tbdq00bfffputxeUlI0aMUGRkpL744gvZbDbZbDZFRUXp8OHDstlsWrhwocLCwuTm5qZ58+bpzJkzeuKJJ1SyZEl5eHiocuXK+vTTT1PtNykpSX369FGBAgVUuHBhvfbaazLG2Nf/+eef6tq1qwoWLCgPDw81b95ccXFxDvtYsmSJKlasKFdXVwUFBWny5MkZnsvs2bPl6+urNWvWZM/gAACAu1qWA+fGjRv12muvycXFxaE9MDBQx48fz7bC8prBgwerffv2evjhhxUfH6/4+HjVrVvXvn7IkCHq16+fYmNj1axZM125ckU1atTQV199pT179qhnz57q0qWLfvzxR4f9RkZGysnJST/++KOmTp2qN998Ux988IF9fUREhLZv367ly5dry5YtMsaoRYsWun79uiQpOjpa7du3V8eOHbV7926NGDFCw4YN05w5c9I8j0mTJmnw4MFavXq1mjZtmu75Xr16VYmJiQ4LAADInbL8kXpycrJu3LiRqv23336Tt7d3thSVF3l5ecnd3V1Xr16Vn59fqvUDBgxQ27ZtHdoGDx5s/7tv375atWqVFi1apAceeMDeHhAQoDfffFM2m00hISHavXu33nzzTT3zzDOKi4vT8uXLtWnTJnu4/eSTTxQQEKBly5bp8ccf15QpU9S4cWMNGzZMkhQcHKyff/5ZEydOVEREhEM9Q4cOVWRkpKKiolS5cuUMz3fcuHEaOXJklsYIAADcnbI8w9m0aVOHK5JtNpsuXLig4cOHq0WLFtlZG25Ss2ZNh8c3btzQmDFjVKVKFRUuXFheXl765ptvdPToUYd+tWvXdrhIqU6dOoqLi9ONGzcUGxsrJycnh4BauHBhhYSEKDY2VpIUGxurevXqOeyzXr169n2kmDx5smbNmqWNGzf+a9iU/gqnCQkJ9uXYsWOZHwwAAHBXyXLgfPPNN7VhwwZVqFBBV65cUadOnRQUFKTjx49r/PjxVtR4V/Lx8VFCQkKq9nPnzsnHxyfL+/P09HR4PHnyZL355pt66aWXtG7dOsXExKhZs2a6du1apvd583c5/9meElJv/juj7R588EHduHFDCxcuzNSxXV1d5ePj47AAAIDcKcsfqfv7+ysmJkaffvqpduzYoeTkZPXo0UOdO3d2uIgorwsNDdXXX3+dqn3btm0KCQlJcxsXF5c0v66Qlu+//16tWrXSk08+KemvrzrExcWpfPnyDv1++OGHVI/LlSun/Pnzq0KFCkpKStKPP/5o/0j9zJkz+vXXX+37qVChgjZu3Oiwj82bNys4OFj58+e3t91///3q27evmjVrpvz58+vFF1/M1HkAAIDcL8uBU5Lc3d3VvXt3de/ePbvryTV69eql6dOnq3fv3urZs6fc3d21Zs0affjhh5o7d26a2wQFBWn16tXat2+fChcuLF9f33T3X7ZsWS1ZskSbN29WwYIFNWXKFJ08eTJV4Dx27JheeOEFPfvss9qxY4emTZtmv8q8XLlyatWqlZ555hnNmjVL3t7eevnll3XPPfeoVatWkqRBgwapVq1aGj16tDp06KAtW7Zo+vTpevfdd1PVVKdOHX399dd6+OGH5eTkpIEDB97q8AEAgFzklgLn8ePHtWnTJp06dUrJyckO6/r165cthd3tgoKC9P333+vVV1/VQw89pCtXrig4OFhz5szR448/nuY2zzzzjKKiolSzZk1duHBB69evV1BQUJp9hw0bpkOHDqlZs2by8PBQz5491bp161Qf43ft2lWXL1/W/fffr/z586tv377q2bOnff3s2bPVv39/tWzZUteuXVODBg20cuVK+30+q1evroULF+r111/X6NGjVaJECY0aNSrVBUMp6tWrpxUrVqhFixbKnz8/rwcAACCbSe+LfOmYPXu2nnvuObm4uKhw4cIO3++z2Ww6ePBgtheJ3C8xMVG+vr66f/z9cnK/pf8HIZfY1HdTTpcAAMiklPfvhISEDK/HyPI7++uvv67XX39dQ4cOVb58/BQ7AAAAMpblxHjp0iV17NiRsAkAAIBMyXJq7NGjhxYtWmRFLQAAAMiFsvyR+rhx49SyZUutWrVKlStXtl9ckmLKlCnZVhwAAADuflkOnGPHjtXq1avt95L850VDAAAAwM2yHDinTJmijz76KN3b4gAAAAA3y/J3OF1dXVP9tjYAAACQniwHzv79+2vatGlW1AIAAIBcKMsfqW/dulXr1q3TV199pYoVK6a6aGjp0qXZVhwAAADuflkOnAUKFFDbtm2tqAUAAAC5UJYD5+zZs62oAwAAALkUPxcEAAAAS2V5hlOSFi9erIULF+ro0aO6du2aw7od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9NNPqcbpo48+0r333itXV1d169ZNGzZs0Ntvvy2bzSabzabDhw+n+kg9xbJlyxQcHCw3Nzc1bdpUx44dy3CMZs+erfLly8vNzU2hoaF69913MzW2AAAgd8t04OzevbvOnz+vKVOmqHLlyqpbt65OnDihjz/+WEeOHNH//d//qXTp0qpXr55mzZqlHTt2ZLmYhIQESVKhQoWytN369et14MABrV+/XpGRkZozZ47mzJmT5eNn5JNPPpGXl5d69eqV5vqU7zx+/vnn6t+/vwYNGqQ9e/bo2Wef1VNPPaX169c79B85cqTat2+vXbt2qUWLFurcubPOnj2rfPnyqWPHjvrkk08c+s+fP1916tTRvffeK2OMHnnkEZ08eVIrV65UdHS0qlevrsaNGzt8tL9//34tXLhQS5YsUUxMjKZOnao6deromWeeUXx8vOLj4xUQEJDm+Vy6dEljxoxRZGSkNm3apMTERHXs2DHd8Xn//ff16quvasyYMYqNjdXYsWM1bNgwRUZGZmZ4AQBALpbpwBkZGanLly9rxowZ6tSpk44ePaply5apZcuWqW4GX6pUKX344YdZKsQYoxdeeEH169dXpUqVsrRtwYIFNX36dIWGhqply5Z65JFH/vP3PP8pLi5O9957r5ydnTPsN2nSJEVERKhXr14KDg7WCy+8oLZt22rSpEkO/SIiIvTEE0+obNmyGjt2rC5evGi/+Kpz587atGmTjhw5IumvWc8FCxboySeflPRXwN69e7cWLVqkmjVrqly5cpo0aZIKFCigxYsX249x7do1zZ07V9WqVVOVKlXk6+srFxcXeXh4yM/PT35+fsqfP3+a53H9+nVNnz5dderUUY0aNRQZGanNmzene4HY6NGjNXnyZLVt21alS5dW27ZtNXDgQM2aNSvN/levXlViYqLDAgAAcqdMB86UHySKi4vT0KFD5efnl25fFxcXh4+YM6NPnz7atWuXPv300yxtJ0kVK1Z0CE4lSpTQqVOnsryfjBhjMvUdx9jYWNWrV8+hrV69eoqNjXVoq1Kliv1vT09PeXt722uuVq2aQkND7WOxYcMGnTp1Su3bt5ckRUdH68KFCypcuLC8vLzsy6FDh3TgwAH7fgMDA1W0aNFbOl8nJyfVrFnT/jg0NFQFChRIdR6SdPr0aR07dkw9evRwqOf//u//HOq52bhx4+Tr62tf0ptpBQAAd78s/dKQVReV9O3bV8uXL9d3332nkiVLZnn7f8462my2bP9FpODgYG3cuFHXr1//11nOf45TWmH132ru3Lmz5s+fr5dfflnz589Xs2bNVKRIEUl/zXiWKFFCUVFRqY598+2MPD09M3NqmT6P9NpS6n7//ff1wAMPOKxLbwZ16NCheuGFF+yPExMTCZ0AAORSWbpoKDg4WIUKFcpwyQpjjPr06aOlS5dq3bp1Kl26dJa2v506deqkCxcupHshTMoFN+XLl9fGjRsd1m3evFnly5fP8vF2796t6OhoLV68WJ07d7avq169uk6ePCknJyeVLVvWYUkJpelxcXHJ1G/cJyUlafv27fbH+/bt07lz5xQaGpqqb/HixXXPPffo4MGDqepJ7zl1dXWVj4+PwwIAAHKnLM1wjhw5Mlvv1di7d2/Nnz9fX3zxhby9vXXy5ElJkq+vr9zd3bPtOGmJiYmRJF24cEGnT59WTEyMXFxcVKFChTT7P/DAA3rppZc0aNAgHT9+XG3atJG/v7/279+vmTNnqn79+urfv79efPFFtW/f3n4Rz5dffqmlS5dq7dq1WaqvdOnSqlu3rnr06KGkpCSHq/6bNGmiOnXqqHXr1ho/frxCQkJ04sQJrVy5Uq1bt3b4KPyfgoKC9OOPP+rw4cPy8vJK9z8Jzs7O6tu3r6ZOnSpnZ2f16dNHtWvX1v33359m/xEjRqhfv37y8fFR8+bNdfXqVW3fvl1//vmnw0wmAADIe7IUODt27KhixYpl28FnzJgh6a+bkd9s9uzZioiIyLbjpKVatWr2v6OjozV//nwFBgbq8OHD6W4zfvx41ahRQ++8845mzpyp5ORklSlTRu3atbN/Z7V169Z6++23NXHiRPXr10+lS5fW7NmzU51jZnTu3Fm9e/dW165dHQK4zWbTypUr9eqrr6p79+46ffq0/Pz81KBBAxUvXjzDfQ4ePFjdunVThQoVdPnyZR06dCjNfh4eHhoyZIg6deqk3377TfXr19dHH32U7n6ffvppeXh4aOLEiXrppZfk6empypUrZ+mm+gAAIHeymZSrgf5F/vz5FR8fn62BE0iRmJgoX19frahTV55OWfp/UJ7X8LsNOV0CACCPSnn/TkhIyPDrcVm+Sh0AAADIikxPJWX3Vd8AAADIG275py0BAACAzCBwAgAAwFIETgAAAFiKwAkAAABLETgBAABgKQInAAAALEXgBAAAgKUInAAAALAUgRMAAACWInACAADAUgROAAAAWIrACQAAAEsROAEAAGApAicAAAAsReAEAACApQicAAAAsJRTThcA3Kz+qq/l4+OT02UAAIBsxAwnAAAALEXgBAAAgKUInAAAALAUgRMAAACWInACAADAUgROAAAAWIrACQAAAEsROAEAAGApAicAAAAsReAEAACApQicAAAAsBSBEwAAAJZyyukCgJvNeuVrubt6/Of99Jn8aDZUAwAAsgMznAAAALAUgRMAAACWInACAADAUgROAAAAWIrACQAAAEsROAEAAGApAicAAAAsReAEAACApQicAAAAsBSBEwAAAJYicAIAAMBSBE4AAABYisAJAAAASxE4AQAAYCkCJwAAACxF4AQAAIClCJwAAACwFIETAAAAliJw3iEiIiLUunXrnC5DkhQWFqYBAwbkdBkAACCXIHBmYObMmfL29lZSUpK97cKFC3J2dtaDDz7o0Pf777+XzWbTr7/+ervL1Jw5c1SgQIEsbxcVFSWbzaZz5845tC9dulSjR4/OnuIAAECeR+DMQHh4uC5cuKDt27fb277//nv5+flp27ZtunTpkr09KipK/v7+Cg4OztIxbty4oeTk5GyrOTsUKlRI3t7eOV0GAADIJQicGQgJCZG/v7+ioqLsbVFRUWrVqpXKlCmjzZs3O7SHh4frzz//VNeuXVWwYEF5eHioefPmiouLs/dLmY386quvVKFCBbm6uurIkSOpjh0dHa1ixYppzJgxkqSffvpJ4eHh8vb2lo+Pj2rUqKHt27crKipKTz31lBISEmSz2WSz2TRixAhJ0rx581SzZk15e3vLz89PnTp10qlTpyRJhw8fVnh4uCSpYMGCstlsioiIkJT6I/XMntPq1atVvnx5eXl56eGHH1Z8fPx/Gn8AAJA7EDj/RVhYmNavX29/vH79eoWFhalhw4b29mvXrmnLli0KDw9XRESEtm/fruXLl2vLli0yxqhFixa6fv26fR+XLl3SuHHj9MEHH2jv3r0qVqyYwzGjoqLUuHFjjRw5Uq+++qokqXPnzipZsqS2bdum6Ohovfzyy3J2dlbdunX11ltvycfHR/Hx8YqPj9fgwYPtdY0ePVo//fSTli1bpkOHDtlDZUBAgJYsWSJJ2rdvn+Lj4/X222+nOQaZPadJkyZp7ty5+u6773T06FF7HWm5evWqEhMTHRYAAJA7OeV0AXe6sLAwDRw4UElJSbp8+bJ27typBg0a6MaNG5o6daok6YcfftDly5dVv359Pf3009q0aZPq1q0rSfrkk08UEBCgZcuW6fHHH5ckXb9+Xe+++66qVq2a6nhffPGFunTpolmzZumJJ56wtx89elQvvviiQkNDJUnlypWzr/P19ZXNZpOfn5/Dvrp3727/+95779XUqVN1//3368KFC/Ly8lKhQoUkScWKFUv3O6BxcXFavnx5ps5p5syZKlOmjCSpT58+GjVqVLrjOm7cOI0cOTLd9QAAIPdghvNfhIeH6+LFi9q2bZu+//57BQcHq1ixYmrYsKG2bdumixcvKioqSqVKldK+ffvk5OSkBx54wL594cKFFRISotjYWHubi4uLqlSpkupYP/74o/73v/8pMjLSIWxK0gsvvKCnn35aTZo00RtvvKEDBw78a+07d+5Uq1atFBgYKG9vb4WFhUn6K7xmVmxsbKbOycPDwx42JalEiRL2j+/TMnToUCUkJNiXY8eOZbomAABwdyFw/ouyZcuqZMmSWr9+vdavX6+GDRtKkvz8/FS6dGlt2rRJ69evV6NGjWSMSXMfxhjZbDb7Y3d3d4fHKcqUKaPQ0FB99NFHunbtmsO6ESNGaO/evXrkkUe0bt06VahQQZ9//nm6dV+8eFEPPfSQvLy8NG/ePG3bts3e/5/7zkhmz8nZ2dlhvc1mS3dbSXJ1dZWPj4/DAgAAcicCZyaEh4crKipKUVFR9llCSWrYsKFWr16tH374QeHh4apQoYKSkpL0448/2vucOXNGv/76q8qXL/+vxylSpIjWrVunAwcOqEOHDg7fkZSk4OBgDRw4UN98843atm2r2bNnS/prxvTGjRsOfX/55Rf98ccfeuONN/Tggw8qNDQ01Yyji4uLJKXa9mb/9ZwAAAAInJkQHh6ujRs3KiYmxj7DKf0VON9//31duXJF4eHhKleunFq1aqVnnnlGGzdu1E8//aQnn3xS99xzj1q1apWpYxUrVkzr1q3TL7/8oieeeML+3dE+ffooKipKR44c0aZNm7Rt2zZ74AsKCtKFCxf07bff6o8//tClS5dUqlQpubi4aNq0aTp48KCWL1+e6t6agYGBstls+uqrr3T69GlduHAhVT3ZcU4AACBvI3BmQnh4uC5fvqyyZcuqePHi9vaGDRvq/PnzKlOmjAICAiRJs2fPVo0aNdSyZUvVqVNHxhitXLky1UfOGfHz89O6deu0e/dude7cWfny5dOZM2fUtWtXBQcHq3379mrevLn9opu6devqueeeU4cOHVS0aFFNmDBBRYsW1Zw5c7Ro0SJVqFBBb7zxhiZNmuRwnHvuuUcjR47Uyy+/rOLFi6tPnz5p1pMd5wQAAPIum8noi3bAbZKYmChfX19N6L1A7q4e/3l/fSY/mg1VAQCAjKS8fyckJGR4PQYznAAAALAUgRMAAACWInACAADAUgROAAAAWIrACQAAAEsROAEAAGApAicAAAAsReAEAACApQicAAAAsBSBEwAAAJYicAIAAMBSBE4AAABYisAJAAAASxE4AQAAYCkCJwAAACxF4AQAAIClCJwAAACwFIETAAAAlnLK6QKAmz07trl8fHxyugwAAJCNmOEEAACApQicAAAAsBSBEwAAAJYicAIAAMBSBE4AAABYisAJAAAASxE4AQAAYCkCJwAAACxF4AQAAIClCJwAAACwFIETAAAAluK31HFHmfhMF7k5O2d5u1fnLbagGgAAkB2Y4QQAAIClCJwAAACwFIETAAAAliJwAgAAwFIETgAAAFiKwAkAAABLETgBAABgKQInAAAALEXgBAAAgKUInAAAALAUgRMAAACWInACAADAUgROAAAAWIrACQAAAEsROAEAAGApAicAAAAsReAEAACApQicAAAAsBSBEwAAAJYicOZic+bMUYECBSw/zogRI3TfffdZfhwAAHB3InDmsIiICNlsNr3xxhsO7cuWLZPNZsv0foKCgvTWW29lc3UAAAD/HYHzDuDm5qbx48frzz//zOlSAAAAsh2B8w7QpEkT+fn5ady4cen22bx5sxo0aCB3d3cFBASoX79+unjxoiQpLCxMR44c0cCBA2Wz2VLNjC5btkzBwcFyc3NT06ZNdezYMYf1M2bMUJkyZeTi4qKQkBDNnTvXYf3Ro0fVqlUreXl5ycfHR+3bt9fvv/+ebq2HDh1S2bJl9fzzzys5OTmrwwEAAHIZAucdIH/+/Bo7dqymTZum3377LdX63bt3q1mzZmrbtq127dqlzz77TBs3blSfPn0kSUuXLlXJkiU1atQoxcfHKz4+3r7tpUuXNGbMGEVG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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(y=df['TypeName'],order=df['TypeName'].value_counts().sort_values(ascending=False).index)\n",
    "plt.title('Count of different laptop types')\n",
    "plt.show()"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "b545614d",
   "metadata": {},
   "source": [
    "#### Inference\n",
    "1) Notebook is the most sought after laptop Types"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "b893c872",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Company', 'TypeName', 'Ram', 'Weight', 'Price', 'Touchscreen', 'Ips',\n",
       "       'Cpu brand', 'HDD', 'SSD', 'Gpu brand', 'os'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "f6d1d902",
   "metadata": {},
   "source": [
    "#### Boxplot of Price wrt. differnt CPU Brand"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "9992c275",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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hw4d0uTJk13Pk5KSdOzYMbfX+Xcwqehxy9u3N31V5LgVzZdrAwBf4HWQjYiIKPFRnc2ZM0cPPPCAPv/8c+3bt6/INmFhYXrrrbfcls2bN0/NmjUrsv2nn36qAwcO6KuvvtLzzz+vjIwMdezYUampqaXWM3fuXB04cEBpaWnq2LGjbr31Vm3YsKHItqdPny61P6s5c+ZMVZdQLSUnJ+vIkSOSpCNHjuiXX35xPR83bpzbugULFlTauOXp25u+KnLciubLtQGAL/A6yErSzp07NWbMGPXp00d9+/bVmDFjtHPnzoquzaecPHlSixYt0n333acbb7xRb775ZpHthg0bprlz57ote/PNNzVs2LAi2zdo0EBNmjRRy5YtNXDgQH366ae68sordddddyk3N7fEmkJDQ9WkSRO1bdtWM2fOlN1u17JlyyRJkZGReu655zR8+HCFhIRo5MiRkqTFixfr8ssvl81mU2RkpJKSktz6zMnJ0eOPP67w8HDZbDa1bt1as2fPdq3fsWOH/vKXv+iiiy5S48aNdeedd7qCjiS999576tChg4KCgtSgQQP17dtXJ0+elCStXr1aV1xxhYKDgxUaGqoePXooKyvLte2MGTN06aWXqlatWrrssss0f/58t9oMw9DMmTM1cOBABQcH67nnnivx+FQ20zRdz51Op06dOuXxw+3KmllE58UO+sfT4sYs2HfBGj2xf/9+LViwoMjtTNPUtm3bXOtM09SCBQu0f/9+r8bwZNzy9O1NXxU5bkXz5doAwFd4HWTfe+89RUVFafPmzerYsaOio6OVnp6uqKgovfvuu5VRo09YuHChLrvsMl122WWKi4vT3Llzi/xhP2DAAB09elSff/65JOnzzz/Xr7/+qptuusmjcfz8/PTQQw8pKytLmzdv9ri+wMBABQQEuF2lfOmll1xfq6efflqbN2/Wbbfdpttvv13bt29XYmKinn76abdQPnToUL3zzjuaNm2aMjIyNHPmTF100UWSzk2R6NWrlzp16qRNmzbp448/1qFDh3Tbbbe51t9xxx0aMWKEMjIytHr1ag0ePFimaers2bMaNGiQevXqpW3btmnDhg0aNWqUDMOQJL3//vt66KGHlJCQoK+//lr33HOP/t//+39atWqV236OHz9eAwcO1Pbt2zVixIhCxyEnJ0fZ2dluj8pS8DZ0AwcOlMPh8PgxcODAPzoq+fcVdwXaFjdmwb69uVWeaZqaOnWqF8X8sY23gdmTccvStzd9VeS4Fc2XawMAX+L1XQsef/xxjR07VhMnTnRbPn78eD3xxBO69dZbK6w4XzJ79mzFxcVJkvr3768TJ04oNTVVffv2dWsXGBiouLg4zZkzR1dffbXmzJmjuLg4BQYGejxW27ZtJZ2bR3vFFVeU2j4nJ0cvvfSSsrOz3T4m+M9//rMeffRR1+vY2Fj16dPH9Qlsbdq00Y4dO/TSSy9p+PDh2rVrlxYtWqQVK1a49qtly5au7WfMmKEuXbro+eefdy2bM2eOwsPDtWvXLp04cUJnz57V4MGDXdNMOnToIEn69ddfdfz4cd1444269NJLJUnt2rVz9TN58mQNHz5co0ePliTFx8friy++0OTJk9W7d29Xu7/97W9FBth8L7zwgiZMmFDqMUNhWVlZSktL82qb3NxcpaWlKSsrS5GRkRU6bln69qavihy3ovlybQDgS7wOsgcPHtTQoUMLLY+Li9NLL71UIUX5mp07d2rjxo2uN1MFBARoyJAhmjNnTqEgK0l33XWXunfvrueff17vvvuuNmzYoLNnz3o8Xv7VlvyrlcW544475O/vr1OnTikkJESTJ0/W9ddf71ofExPj1j4jI8P9SqCkHj166F//+pdyc3O1detW+fv7q1evXkWOt3nzZq1atcp1hbagPXv26LrrrlOfPn3UoUMHORwOXXfddbrllltUr1491a9fX8OHD5fD4VC/fv3Ut29f3XbbbWratKmrtlGjRhWq7eWXX3Zbdv4+nW/s2LGKj493vc7OzlZ4eHiJ25SVzWZzPf/ggw9kt9s93tbpdP7xtfD3YtACbYsbs2DfBWssTUREhLp166b09PRSp7W4yvH3V9euXcs1P764ccvStzd9VeS4Fc2XawMAX+L11IJrr71Wn332WaHln3/+ua655poKKcrXzJ49W2fPnlWzZs0UEBCggIAAzZgxQ0uWLNHRo0cLtY+KilLbtm11xx13qF27doqKivJqvIyMDElSixYtSmw3depUbd26VQcOHNCvv/6qhIQEt/Xn3+PXNM1C4bjgnyiDgoJKHC8vL0833XSTtm7d6vbYvXu3evbsKX9/f61YsUL//e9/1b59e73yyiu67LLLtHfvXknn3py2YcMG/elPf9LChQvVpk0bffHFF67+i6rt/GXn79P5bDab6tat6/aoLAVrs9vtCgoK8vjhFkBL/n3lvEH/eFrcmAX7Lu2XofP355FHHvGimD+28WYcT8ctS9/e9FWR41Y0X64NAHyJR0F22bJlrseAAQP0xBNPaMyYMUpOTlZycrLGjBmjJ598UjfffHNl13vBnT17Vm+99ZaSkpLcwttXX32liIiIYt9FPGLECK1evbrEP4MXJS8vT9OmTVOLFi1KvS9vkyZN1KpVKzVq1Mijvtu3b++au5tv/fr1atOmjfz9/dWhQwfl5eVpzZo1RW7fpUsXffPNN4qMjFSrVq3cHvkB0zAM9ejRQxMmTNCWLVtUq1Ytvf/++64+OnfurLFjx2r9+vWKiorS22+/LencNIOiais4/QCVr3nz5oqNjS0yKBmGoejoaNc6wzAUGxtb7B05yjNuefr2pq+KHLei+XJtAOArPAqygwYNcj1Gjx6tX375RdOnT9fQoUM1dOhQTZ8+XT///LPuv//+yq73gvvoo4909OhR3XXXXYqKinJ73HLLLW7v6C9o5MiR+vnnn3X33XeX2P+RI0d08OBBff/991q2bJn69u2rjRs3avbs2fL39+ZvzqVLSEhQamqqnn32We3atUvz5s3Tq6++6ppHGxkZqWHDhmnEiBFaunSp9u7dq9WrV2vRokWSpPvvv1+//vqr7rjjDm3cuFHff/+9PvnkE40YMUK5ubn68ssv9fzzz2vTpk3at2+flixZop9//lnt2rXT3r17NXbsWG3YsEFZWVn65JNPtGvXLldQfeyxx/Tmm29q5syZ2r17t6ZMmaIlS5a4zfHFhREXF6cGDRpIkho2bKiGDRu6nj/33HNu62JjYytt3PL07U1fFTluRfPl2gDAF3gUZPPy8jx6eDqvzkpmz56tvn37KiQkpNC6v/71r9q6davS09MLrQsICFDDhg0VEFDyNOS+ffuqadOm6tChg5588km1a9dO27Ztc3uDU0Xp0qWLFi1apHfeeUdRUVF65plnNHHiRA0fPtzVZsaMGbrllls0evRotW3bViNHjnTdPissLEzr1q1Tbm6uHA6HoqKi9NBDDykkJER+fn6qW7eu1q5dq7/85S9q06aNxo0bp6SkJF1//fWqXbu2vv32W/31r39VmzZtNGrUKI0ZM0b33HOPpHO/LL388st66aWXdPnll+v111/X3Llz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HKiLLrpIdevW1W233aZDhw651icmJqpTp06aM2eO68quaZo6fvy4Ro0apUaNGqlu3br685//rK+++qrYes6fWlCvXj3dd999iomJUUREhPr06aPRo0frs88+83gffYVpmq7nTqdTp06dcnsUvEppFtVBcf0WeF5Uv5483MYuUOf+/fu1YMEC1zLTNLVgwQLt37+/1LrO37Zg/572AQBAaQKqugBI8+bNU3x8vL788ktt2LBBw4cPV48ePdSvXz+lpaWpUaNGmjt3rvr37y9/f39JUkpKiuLi4jRt2jRdc8012rNnj0aNGiVJGj9+fKlj/vrrr/r44481adIkBQcHF1ofGhoq6VzwGDRokIKDg7VmzRqdPXtWo0eP1pAhQ7R69WpX+++++06LFi3S4sWLXTXecMMNql+/vpYvX66QkBC9/vrr6tOnj3bt2qX69et7fZx++uknLVmyRL169Sq2TU5OjnJyclyvfWUaQsGaBg4cWGLbM5JqedhvwWvfpfXriZycHNWuXVumaWrq1KmF1ucvnzx5sgzDKLKP/Dbnh1hv+gAAwBNckfUB0dHRGj9+vFq3bq2hQ4cqJibGNUf14osvlnQuWDZp0sT1etKkSXryySc1bNgwtWzZUv369dOzzz6r119/3aMxv/vuO5mmqbZt25bY7tNPP9W2bdv09ttvq2vXrrryyis1f/58rVmzRmlpaa52p0+f1vz589W5c2dFR0dr1apV2r59u959913FxMSodevWmjx5skJDQ/Xee+95dXzuuOMO1a5dW82aNVPdunU1a9asYtu+8MILCgkJcT3Cw8O9GgvnZGVlKS0tTbm5uW7Lc3NzlZaWpqysrFK3zZ9OcD5P+gAAwBNckfUB0dHRbq+bNm2qw4cPl7jN5s2blZaWpkmTJrmW5ebmyul06vfff1ft2rVL3D7/allpV8QyMjIUHh7uFgjbt2+v0NBQZWRkqFu3bpKkiIgIV8jOr+/EiRNq0KCBW3+nTp3Snj17ShzzfFOnTtX48eO1c+dO/f3vf1d8fLymT59eZNuxY8cqPj7e9To7O9snwqzNZnM9/+CDD2S3293WO51O1xXVQC/6Ldi2qH49UXDs/DojIiLUrVs3paenu4VZf39/de3aVREREcX2l7/t5s2biwyznvQBAIAnCLI+IDDQPboYhlHs1ax8eXl5mjBhggYPHlxonSdhpnXr1jIMQxkZGSXeRcE0zSLD7vnLz5+ekJeXp6ZNm7pNP8iXP23BU02aNFGTJk3Utm1bNWjQQNdcc42efvppNW3atFBbm83mFhp9RcFjZbfbFRQUVHxbb/ot8Ly0fj3q7391GoahRx55RHfeeWeh9Y888kiJvwAVt603fQAA4AmmFlhAYGBgoT/xdunSRTt37lSrVq0KPfz8Sv+y1q9fXw6HQ6+99ppOnjxZaP2xY8cknbv6um/fPv3www+udTt27NDx48fVrl27Yvvv0qWLDh48qICAgEL1NWzY0MM9Lyz/SnLBOaeoHM2bN1dsbKxbuI2NjVWzZs283jafN30AAFAagqwFREZGKjU1VQcPHtTRo0clSc8884zeeustJSYm6ptvvlFGRoYWLlyocePGedzv9OnTlZubqyuuuEKLFy/W7t27lZGRoWnTpql79+6SpL59+yo6OlqxsbFKT0/Xxo0bNXToUPXq1UsxMTHF9t23b191795dgwYNUkpKijIzM7V+/XqNGzdOmzZt8qi+5cuXa+7cufr666+VmZmp5cuX67777lOPHj3c7t6AyhMXF+eaHtKwYUPFxsaWadv8X6687QMAgJIQZC0gKSlJK1asUHh4uDp37ixJcjgc+uijj7RixQp169ZNV111laZMmeLVvMMWLVooPT1dvXv3VkJCgqKiotSvXz+lpqZqxowZkv74MIZ69eqpZ8+e6tu3r1q2bKmFCxeW2LdhGFq+fLl69uypESNGqE2bNrr99tuVmZmpxo0be1RfUFCQ3njjDV199dVq166dHn74Yd1444366KOPPN5HlI/dbldCQoIaN26s+Ph4r+bgFtw2Li6uTH0AAFASwyzuHjlANZCdna2QkBAdP35cdevWrbI6Tp06JYfDIencrdPOn8tacP3T/1v27P/+fVpSrWJmzp6W6WpXVL8VURsAABeapz+/uSILAAAASyLIAgAAwJIIsgAAALAkgiwAAAAsiSALAAAASyLIAgAAwJIIsgAAALAkgiwAAAAsiSALAAAASwqo6gKAmsButyslJcX13Jf4cm0AAJSEIAtcAIZh+OxHv/pybQAAlISpBQAAALAkgiwAAAAsiSALAAAASyLIAgAAwJIIsgAAALAkgiwAAAAsiSALAAAASyLIAgAAwJIIsgAAALAkPtkL8DGni3xtetQWAICahCAL+Jh/lvIaAACcw9QCAAAAWBJXZAEfYLfblZKS4nptmqZycnIkSTabTYZheNQHAAA1CUEW8AGGYSgoKMhtWe3atauoGgAArIGpBQAAALAkgiwAAAAsiSALAAAASyLIAgAAwJIIsgAAALAkgiwAAAAsiSALAAAASyLIAgAAwJIIsgAAALAkgiwAAAAsiY+oBSqBaZpyOp2FluXk5EiSbDabDMMotR+73e5ROwAAaiKCLFAJnE6nHA5HuftJSUlRUFBQBVQEAED1w9QCAAAAWBJXZIFKNqDTaAX4Beps7hkt+2r6uWUdRyvAP7DI9mfzzmjZ1ukXskQAACyJIAtUsgC/QAX413Jf5l94GQAA8A5TCwAAAGBJBFkAAABYEkEWAAAAlkSQBQAAgCURZAEAAGBJBFkAAABYEkEWAAAAlkSQBQAAgCURZAEAAGBJBFkAAABYEh9RC3jJNE05nU5Jkt1ul2EYVVxRyaxWLwAAnuKKLOAlp9Mph8Mhh8PhCoi+zGr1AgDgKYIsAAAALIkgCwAAAEsiyAIAAMCSCLIAAACwJIIsAAAALIkgCwAAAEsiyAIAAMCSCLIAAACwJIIsAAAALIkgCwAAAEuydJB98803FRoaWtVlVLjVq1fLMAwdO3asqktBNfPFF1/o1ltv1bp168q0/bp167zeft26dbr++uvVq1cvzZo1q9g+Z82aVWK7so7vTZ1l7buobQvu14ABAzRgwIBKqbsmKHh8K/McgOd8+evgy7Wh4lV5kP3hhx901113KSwsTLVq1VJERIQeeughHTlyxK1dZGSk/vWvf1VNkWWsoTIDaWRkpAzDkGEYql27tqKiovT6669X+DioXqZNm6ZDhw4pKSlJTqfTq22dTqeSkpK82t7pdGry5Mk6efKkTNPU/Pnz3b4fCvY5f/78YtuVdfzK3LeSti24LDk5WceOHdOxY8c0efLkCq27Jih4LCdPnlxp5wA8V5nfi+Xly7WhclRpkP3+++8VExOjXbt26d///re+++47zZw5U6mpqerevbt+/fXXKqnrzJkzVTKutyZOnKgDBw5o27ZtGjRokO69914tXLiwyLanT5++wNVVvuq4T5Ut/3vqyJEjWrBggVfbJicnu37B9HT7gttIkmmaGjduXJHrTdMstl1Zx/dUefouatuCy/Ly8lxtK7rumuD84/vLL7+4nnMsq0Zlfi+Wly/XhspRpUH2/vvvV61atfTJJ5+oV69euuSSS3T99dfr008/1Y8//qinnnpKknTttdcqKytLjzzyiOsqZEEpKSlq166dLrroIvXv318HDhxwWz937ly1a9dOdrtdbdu21fTp013rMjMzZRiGFi1apGuvvVZ2u13Jycke1W8YhmbNmqWbb75ZtWvXVuvWrbVs2TJXv71795Yk1atXT4ZhaPjw4ZLO/ZB+8cUX1bJlSwUFBaljx4567733vD5+derUUZMmTdSqVSs999xzat26tZYuXeo6ZmPGjFF8fLwaNmyofv36SZLWrFmjK664QjabTU2bNtWTTz6ps2fPuvrMy8vTP//5T7Vq1Uo2m02XXHKJJk2a5Fr/448/asiQIapXr54aNGiggQMHKjMz07V+9erVuuKKKxQcHKzQ0FD16NFDWVlZkqSvvvpKvXv3Vp06dVS3bl117dpVmzZtcm27ePFiXX755bLZbIqMjFRSUpLb/kZGRuq5557T8OHDFRISopEjR3p9zCpCwcDldDp16tSpQo+CVwEKtq+o/r15FFWLaZpasGCB9u/f71FN+/fv14IFC7zafv/+/UV+L23btk2bNm0q1Gdx7co6vqfK03dR2yYnJys5ObnY/UpOTq6QumuCks6RijwH4LnK/F4sL1+uDZUnoKoG/vXXX5WSkqJJkyYpKCjIbV2TJk0UGxurhQsXavr06VqyZIk6duyoUaNGFQovv//+uyZPnqz58+fLz89PcXFxevTRR12/hb3xxhsaP368Xn31VXXu3FlbtmzRyJEjFRwcrGHDhrn6eeKJJ5SUlKS5c+fKZrN5vB8TJkzQiy++qJdeekmvvPKKYmNjlZWVpfDwcC1evFh//etftXPnTtWtW9e1n+PGjdOSJUs0Y8YMtW7dWmvXrlVcXJwuvvhi9erVq6yHVHa73e1q8rx583Tfffdp3bp1Mk1TP/74o/7yl79o+PDheuutt/Ttt99q5MiRstvtSkxMlCSNHTtWb7zxhqZOnaqrr75aBw4c0Lfffus61r1799Y111yjtWvXKiAgQM8995z69++vbdu2yc/PT4MGDdLIkSP173//W6dPn9bGjRtdv3jExsaqc+fOmjFjhvz9/bV161YFBgZKkjZv3qzbbrtNiYmJGjJkiNavX6/Ro0erQYMGrl8AJOmll17S008/XehqXb6cnBzl5OS4XmdnZ5f5eBanYP8DBw4stX1u3lkFyvNzKjfvj18sPOm/rEzT1NSpUzV58uRCvxwW1c6b7U3T1JQpU9yuRhaUmJio1q1blxryx48fr2XLlnk9vqfKsm+lbZubm1vimLm5uZoyZYqSkpLKXHdNUNzxLapNec4BeK483y+VzZdrQ+WqsiC7e/dumaapdu3aFbm+Xbt2Onr0qH7++Wc1atRI/v7+riuQBZ05c0YzZ87UpZdeKkkaM2aMJk6c6Fr/7LPPKikpSYMHD5YktWjRQjt27NDrr7/uFmQffvhhVxtvDB8+XHfccYck6fnnn9crr7yijRs3qn///qpfv74kqVGjRq43pZ08eVJTpkzRypUr1b17d0lSy5Yt9fnnn+v1118vU5A9e/askpOTtX37dt13332u5a1atdKLL77oev3UU08pPDxcr776qgzDUNu2bfXTTz/piSee0DPPPKOTJ0/q5Zdf1quvvuo6NpdeeqmuvvpqSdI777wjPz8/zZo1y/Ufwty5cxUaGqrVq1crJiZGx48f14033uj6ehT8+u7bt0+PPfaY2rZtK0lq3bq1a92UKVPUp08fPf3005KkNm3aaMeOHXrppZfcguyf//xnPfroo8UeixdeeEETJkzw+hjWRLm5uUpLS1NWVpYiIyOLbZeVlaW0tDSvts/KynK72n6+7Oxsbd68udQaf/vtNy1btszr8T1Vln0rbVtPbNq0qVx11wSeHN+KOAfgufJ8v1Q2X64NlavKgmxp8q/UlPYbVO3atV2hSZKaNm2qw4cPS5J+/vln15vJCl7JPXv2rEJCQtz6iYmJKVOd0dHRrufBwcGqU6eOa/yi7NixQ06n0/Wn/nynT59W586dvRr7iSee0Lhx45STk6NatWrpscce0z333ONaf/4+ZWRkqHv37m7HtEePHjpx4oT279+vgwcPKicnR3369ClyvM2bN+u7775TnTp13JY7nU7t2bNH1113nYYPHy6Hw6F+/fqpb9++uu2229S0aVNJUnx8vO6++27Nnz9fffv21a233ur62mVkZBS6+tijRw/961//Um5urvz9/Yvcp/ONHTtW8fHxrtfZ2dkKDw8vcRtvFbxi/8EHH8hutxdq43Q6Xfvj7+fdt1nB9sX1741Tp05p0KBBhcfx91fXrl0VERFR4vYRERHq1q2b0tPT3a42lrR9RESEYmJiig2zdevWVevWrbVly5Zir9rmtxswYIA+//xzr8b3VFn2rbRtPdGtW7dy1V0TeHJ8K+IcgOfK8/1Sk2tD5aqyObKtWrWSYRjasWNHkeu//fZb1atXTw0bNiyxn/w/TeczDMMVgvN/QL7xxhvaunWr6/H111/riy++cNsuODi4TPtR1Pgl/WDOX/ef//zHraYdO3Z4PU/2scce09atW5WVlaUTJ07oxRdflJ/fH1/S8/fJNM0i/wScX/f5UzyKqr1r165udW/dulW7du3S3/72N0nnrtBu2LBBf/rTn7Rw4UK1adPGdawTExP1zTff6IYbbtDKlSvVvn17vf/++6XWVlBpXyebzaa6deu6PSpawTrtdruCgoIKPQqGT2//nOVJ/94+ihsnf955afU88sgjXm1vGIbi4+PdzseCJk6cqISEhFLHnjhxovz9/b0e31Nl2bfStvX39y92v/PXx8fH82fOUhR3fItqw7G8MMrz/VLZfLk2VK4qC7INGjRQv379NH36dJ06dcpt3cGDB7VgwQINGTLEdfLVqlXL66sejRs3VrNmzfT999+rVatWbo8WLVpU2L4Up1atWpLc58y1b99eNptN+/btK1STt1cOGzZsqFatWiksLMyjb9L27dtr/fr1bgFx/fr1qlOnjpo1a6bWrVsrKChIqampRW7fpUsX7d69W40aNSpUe8Er3J07d9bYsWO1fv16RUVF6e2333ata9OmjR555BF98sknGjx4sObOneuq7fPPP3cbb/369WrTpo3raizKL/88MQxDsbGxatasmUfbNW/eXLGxsV5t37x5c8XFxRVaHh0drS5duhTqs7h2ZR3fU+Xpu6ht4+LiFBcXV+x+xcXFVUjdNUFJ50hFngPwXGV+L5aXL9eGylOldy149dVXlZOTI4fDobVr1+qHH37Qxx9/rH79+qlZs2Zu75aPjIzU2rVr9eOPP7puv+KJxMREvfDCC3r55Ze1a9cubd++XXPnztWUKVMqY5fcREREyDAMffTRR/r555914sQJ1alTR48++qgeeeQRzZs3T3v27NGWLVv02muvad68eZVaz+jRo/XDDz/ogQce0LfffqsPPvhA48ePd105s9vteuKJJ/T444/rrbfe0p49e/TFF19o9uzZks69Wathw4YaOHCgPvvsM+3du1dr1qzRQw89pP3792vv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rVrq2rWrVqxY4bZ8xYoV+tOf/lRFVVWsnJwcZWRkqGnTpmrRooWaNGnitr+nT5/WmjVrXPvbtWtXBQYGurU5cOCAvv76a1eb7t276/jx49q4caOrzZdffqnjx4+7tfn666914MABV5tPPvlENptNXbt2rdR99pSvHY/u3btr7dq1brfH+eSTTxQWFqbIyMiKPwBeOnLkiH744Qc1bdpUUvU+NqZpasyYMVqyZIlWrlypFi1auK2v6edOacenKDXp/DmfaZrKycmp8edNpan0t5MBPiz/9luzZ882d+zYYT788MNmcHCwmZmZWdWllUlCQoK5evVq8/vvvze/+OIL88YbbzTr1Knj2p9//OMfZkhIiLlkyRJz+/bt5h133FHkrV+aN29ufvrpp2Z6err55z//uchbv0RHR5sbNmwwN2zYYHbo0KHIW7/06dPHTE9PNz/99FOzefPmF/z2W7/99pu5ZcsWc8uWLaYkc8qUKeaWLVtct1fzpeNx7Ngxs3HjxuYdd9xhbt++3VyyZIlZt27dSrsVTknH5rfffjMTEhLM9evXm3v37jVXrVpldu/e3WzWrFmNODb33XefGRISYq5evdrt9lG///67q01NPndKOz41+fwZO3asuXbtWnPv3r3mtm3bzL///e+mn5+f+cknn5imWbPPm8pCkEWN99prr5kRERFmrVq1zC5durjdQsZq8u9JGBgYaIaFhZmDBw82v/nmG9f6vLw8c/z48WaTJk1Mm81m9uzZ09y+fbtbH6dOnTLHjBlj1q9f3wwKCjJvvPFGc9++fW5tjhw5YsbGxpp16tQx69SpY8bGxppHjx51a5OVlWXecMMNZlBQkFm/fn1zzJgxbrd5uRBWrVplSir0GDZsmGmavnc8tm3bZl5zzTWmzWYzmzRpYiYmJlbabXBKOja///67ed1115kXX3yxGRgYaF5yySXmsGHDCu13dT02RR0XSebcuXNdbWryuVPa8anJ58+IESNcP08uvvhis0+fPq4Qa5o1+7ypLIZpWu0jHAAAAADmyAIAAMCiCLIAAACwJIIsAAAALIkgCwAAAEsiyAIAAMCSCLIAAACwJIIsAAAALIkgCwAAAEsiyAIALOXaa6/Vww8/XNVlAPABBFkAQJUZPny4DMOQYRgKDAxUy5Yt9eijj+rkyZPFbrNkyRI9++yzF7BKAL4qoKoLAADUbP3799fcuXN15swZffbZZ7r77rt18uRJzZgxw63dmTNnFBgYqPr161dRpQB8DVdkAQBVymazqUmTJgoPD9ff/vY3xcbGaunSpUpMTFSnTp00Z84ctWzZUjabTaZpFppakJOTo8cff1zh4eGy2Wxq3bq1Zs+e7Vq/Y8cO/eUvf9FFF12kxo0b684779Qvv/xSBXsKoKIRZAEAPiUoKEhnzpyRJH333XdatGiRFi9erK1btxbZfujQoXrnnXc0bdo0ZWRkaObMmbroooskSQcOHFCvXr3UqVMnbdq0SR9//LEOHTqk22677ULtDoBKxNQCAIDP2Lhxo95++2316dNHknT69GnNnz9fF198cZHtd+3apUWLFmnFihXq27evJKlly5au9TNmzFCXLl30/PPPu5bNmTNH4eHh2rVrl9q0aVOJewOgsnFFFgBQpT766CNddNFFstvt6t69u3r27KlXXnlFkhQREVFsiJWkrVu3yt/fX7169Spy/ebNm7Vq1SpddNFFrkfbtm0lSXv27Kn4nQFwQXFFFgBQpXr37q0ZM2YoMDBQYWFhCgwMdK0LDg4ucdugoKAS1+fl5emmm27SP//5z0LrmjZtWraCAfgMgiwAoEoFBwerVatWZdq2Q4cOysvL05o1a1xTCwrq0qWLFi9erMjISAUE8CMPqG6YWgAAsKzIyEgNGzZMI0aM0NKlS7V3716tXr1aixYtkiTdf//9+vXXX3XHHXdo48aN+v777/XJJ59oxIgRys3NreLqAZQXQRYAYGkzZszQLbfcotGjR6tt27YaOXKk6wMVwsLCtG7dOuXm5srhcCgqKkoPPfSQQkJC5OfHj0DA6gzTNM2qLgIAAADwFr+OAgAAwJIIsgAAALAkgiwAAAAsiSALAAAASyLIAgAAwJIIsgAAALAkgiwAAAAsiSALAAAASyLIAgAAwJIIsgAAALAkgiwAAAAs6f8DT+EE6U1KZZ8AAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(y=df['Cpu brand'],x=df['Price'])\n",
    "plt.show()"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "72b87062",
   "metadata": {},
   "source": [
    "#### Boxplot of Price wrt. differnt GPU Brand"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "41b88588",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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Q1YYAABANAk6NHXs2LHMsi5duiglJUUvvPCC+vfvH5LCAAAAoknILgS/7LLLlJubG6ruAAAAokrQR5oKCwv9HhtjtH//fk2cOFGXXnppyAoDAACIJkGHpgsuuKDMheDGGKWlpWnBggUhKwwAACCaBB2aVqxY4fc4JiZGF198sdq0aXPeP44LAABQUwWdcnr27BmOOgAAAKJapQ4N7dixQzNmzND27dvlOI7atWunESNGqF27dqGuDwAAICoE/em5v/zlL8rIyNCGDRvUsWNHdejQQRs3blT79u31xhtvhKNGAACAiAv6SNPjjz+ucePG6emnn/ZbPmHCBD3xxBMaMGBAyIoDAACIFkEfaTpw4IDuv//+MsuzsrJ04MCBkBQFAAAQbYIOTTfeeKNWrVpVZvnq1at1/fXXh6QoAACAaBP06bk77rhDTzzxhDZs2KDu3btLktavX6833nhDTz31lJYsWeLXFgAAoDZwjDEmmCfExNgdnHIcR8XFxZUqqiYqLCxUYmKiCgoK1Lhx45D3b4yR1+uVJLnd7jJfMFpZJ0+elMfjkSS9ctMRuWPP/xxvsfTgiguDes75+snJyVFCQkLlOqpG4XodAACREcz7d9BHmkpKSipdGCrPcZwaESpqO14HAKi7QvYHewEAAGoz6yNNJ0+e1PLly3X77bdLksaNG6eioiLf+tjYWD3zzDNyu92hrxIAACDCrEPT66+/rqVLl/pC00svvaQrr7zSd6riiy++UEpKikaNGhWeSgEAACLI+vRcdna2hg0b5rds/vz5WrFihVasWKEXXnhBCxcuDHmBAAAA0cA6NH355Ze67LLLfI/dbrffJ+m6deumbdu2hbY6AACAKGF9eq6goEBxcf9s/o9//MNvfUlJid81TgAAALWJ9ZGm1NRUbd26tcL1mzdvVmpqakiKAgAAiDbWoem2227Tk08+6ftiv9JOnjypp556Sn379g1pcQAAANHC+vTc+PHjtXDhQrVt21YjRozQZZddJsdx9MUXX+ill17SmTNnNH78+HDWCgAAEDHWoSkpKUlr167Vww8/rLFjx+rsX19xHEe33nqrZs6cqaSkpLAVCgAAEElB/RmVVq1a6f3339cPP/ygr7/+WpLUpk0bNWnSJCzFAQAARIug//acJDVp0kTdunULdS0AAABRi789BwAAYIHQBAAAYIHQBAAA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G264QR6PR+PHj/dbXq9ePd1zzz2aP3++pJ9OzQ0cOFBxceXnvWAuujzr3//937Vo0SI9++yzWrVqlfLy8tS+fXudOnUq+A0BgEpKTU1VZmam743AcRxlZmaqefPm5a7LyspSVlZWue2rMmZWVpbfsrMq039lBZqLSIvm2gKh7qqLmtAk/XSd0DvvvKO1a9f6Lc/MzNT777+vzz//XCtWrFBmZmaFfVxxxRVav36937JzH59r1apVGjp0qO6++261b99eycnJ2r17d6W3AwAqKysrSxdddJEkqWnTpn7/35W3LlD7qoxZellMTEyV+q+sUGxbuERzbYFQd9VEVWjq0KGDMjMzNWPGDL/lPXv2VFJSkjIzM9WyZUt17969wj6GDx/u+zTcjh07NH/+fM2dOzfguG3atNHixYuVl5enzz77TL/4xS/8DncDQHVxu90aM2aMkpKSNHr0aL9r18pbF6h9VcYsvSwrK6tK/VdWKLYtXKK5tkCou2qi5pqms5555hktXLjQb5njOBo0aJBeeOEFPfnkkwGf36JFCy1atEijRo3SzJkz1a1bN02aNEnDhg2r8DnTp0/XsGHDdM0116hp06Z64oknatRXCACoXa699lpde+211usCta/KmKWXPfjgg1Xqv7JCsW3hEs21BULdleeYylwEhDIKCwuVmJiogoICNW7cONLlBHTy5Enfl+Xl5ORE9ILi0rUU310cvhh/Rop9Mzb844RTqW2I9OuGwKLpZwxAYMG8f0fV6TkAAIBoRWgCAACwQGgCAACwQGgCAACwQGgCAACwQGgCAACwQGgCAACwQGgCAACwQGgCAACwQGgCAACwQGgCAACwQGgCAACwQGgCAACwQGgCAACwQGgCAACwQGgCAACwQGgCAACwQGgCAACwEBfpAlD93G63cnJyfPcBhBY/Y0DtRGiqgxzHUUJCQqTLAGotfsaA2onTcwAAABYITQAAABYITQAAABYITQAAABYITQAAABYITQAAABYITQAAABYITQAAABYITQAAABYITQAAABYITQAAABYITQAAABYITQAAABYITQAAABYITQAAABYITQAAABYITQAAABYITQAAABYITQAAABbiIl0A4HOmmvoO5zjhVFPrBoBagtCEqBH7TmytGgcAULtweg4AAMACR5oQUW63Wzk5OWEfxxijoqIiSZLL5ZLj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U1N9y9l/Kp6b8tSlfadevXpq06aNunTposmTJ6tjx476/e9/zz4TRoSmalCvXj117txZy5Yt81u+bNkyXXPNNRGqKvSKioq0fft2NWvWTK1atVJycrLfNp86dUoff/yxb5s7d+6s+Ph4vzb79+/X1q1bfW169OihgoICffrpp742f/vb31RQUODXZuvWrdq/f7+vzQcffCCXy6XOnTuHdZttRNtc9OjRQ5988onfR4I/+OADpaSkqGXLlqGfgErIz8/Xt99+q2bNmkmq3fNjjNGIESO0ePFiffTRR2rVqpXf+rq8/5xvbspTl/adcxljVFRUVKf3mbAL+6XmMMb88ysHZs+ebbZt22ZGjhxpGjRoYHbv3h3p0iptzJgxZuXKleabb74x69evN7fffrtp1KiRb5uee+45k5iYaBYvXmy2bNliBg0aVO5HXlNTU82HH35oNm7caG6++eZyP/LaoUMHs27dOrNu3TrTvn37cj/yesstt5iNGzeaDz/80KSmplbrVw4cO3bMbNq0yWzatMlIMtOmTTObNm3yfaVENM3F0aNHTVJSkhk0aJDZsmWLWbx4sWncuHFYP/4baH6OHTtmxowZY9auXWt27dplVqxYYXr06GGaN29eJ+bn4YcfNomJiWblypV+H5s/ceKEr01d3X/ONzd1ed8ZN26c+eSTT8yuXbvM5s2bzfjx401MTIz54IMPjDF1d58JN0JTNfrDH/5g0tPTTb169cxVV13l97HZmujs937Ex8eblJQU079/f/P555/71peUlJgJEyaY5ORk43K5zA033GC2bNni18fJkyfNiBEjTJMmTUxCQoK5/fbbzd69e/3a5Ofnm8zMTNOoUSPTqFEjk5mZaY4cOeLXZs+ePaZv374mISHBNGnSxIwYMcLv463htmLFCiOpzG3IkCHGmOibi82bN5vrr7/euFwuk5ycbCZOnBjWj/4Gmp8TJ06Y3r17m4svvtjEx8ebFi1amCFDhpTZ9to6P+XNiyTz6quv+trU1f3nfHNTl/edYcOG+d5PLr74YnPLLbf4ApMxdXefCTfHmJr4lZwAAADVi2uaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaAAAALBCaACCAG2+8USNHjox0GQCiAKEJQJ0xdOhQOY4jx3EUHx+v1q1b6ze/+Y2OHz9e4XMWL16sZ555phqrBBCt4iJdAABUpz59+ujVV1/V6dOntWrVKj344IM6fvy4Zs2a5dfu9OnTio+PV5MmTSJUKYBow5EmAHWKy+VScnKy0tLS9Itf/EKZmZl66623NHHiRHXq1Elz5sxR69at5XK5ZIwpc3quqKhIjz/+uNLS0uRyuXTppZdq9uzZvvXbtm3TbbfdpoYNGyopKUmDBw/W4cOHI7ClAEKN0ASgTktISNDp06clSV9//bUWLlyoRYsWKS8vr9z2999/vxYsWKAXX3xR27dv18svv6yGDRtKkvbv36+ePXuqU6dO+vvf/673339fBw8e1L333ltdmwMgjDg9B6DO+vTTTzV//nzdcsstkqRTp07pf//3f3XxxReX2/7LL7/UwoULtWzZMvXq1UuS1Lp1a9/6WbNm6aqrrtKkSZN8y+bMmaO0tDR9+eWXuuyyy8K4NQDCjSNNAOqUpUuXqmHDhnK73erRo4duuOEGzZgxQ5KUnp5eYWCSpLy8PMXGxqpnz57lrt+wYYNWrFihhg0b+m7t2rWTJO3cuTP0GwOgWnGkCUCdctNNN2nWrFmKj49XSkqK4uPjfesaNGgQ8LkJCQkB15eUlKhfv356/vnny6xr1qxZ5QoGEDUITQDqlAYNGqhNmzaVem779u1VUlKijz/+2Hd6rrSrrrpKixYtUsuWLRUXx3+vQG3D6TkAsNSyZUsNGTJEw4YN01tvvaVdu3Zp5cqVWrhwoSTpkUce0Q8//KBBgwbp008/1TfffKMPPvhAw4YNU3FxcYSrB1BVhCYACMKsWbN0zz336Fe/+pXatWunhx56yPflmCkpKVqzZo2Ki4vl8XiUkZGhxx57TImJiYqJ4b9boKZzjDEm0kUAAABEO371AQAAsEBoAgAAsEBoAgAAsEBoAgAAsEBoAgAAsEBoAgAAsEBoAgAAsEBoAgAAsEBoAgAAsEBoAgAAsEBoAgAAsPD/AKldXJoPhDgkAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(y=df['Gpu brand'],x=df['Price'])\n",
    "plt.show()"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "3449d509",
   "metadata": {},
   "source": [
    "#### Distplot for Price"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "e3194213",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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Wxf6ev369fJ6vaH5yspKvf3220pKSmq04gAAaMsuKqTvuOMOSZLD4dDkyZPD2txut5KSkvTcc881WnEAALRlFxXSwWBQkpScnKwdO3aoc+fOTVIUWrfy8vI6+zidTrlcF/XrCQCtToM+ky4oKGiWgA4EAvrVr36l5ORkxcTEqFevXpo3b17onwVJMsYoMzNTfr9fMTExSktL0/79+5u8Nly8YGVAckYpLi5OHo+n1ql7jyQFAoFIlwwAEdXgXZW3335bb7/9toqKisJCU5JeffXVSy5Mkp555hm9+OKLWr58ufr27audO3fqX//1X+X1ejVjxgxJ0rPPPqv58+dr2bJl6t27t/793/9dI0eO1MGDBxUXF9codaCRGCMFK3XnglxFRUfX2C0YqNDqGSOq/F4BQFvToJD+zW9+o3nz5mngwIHq2rWrHA5HY9clSdq+fbt+9KMf6bbbbpMkJSUl6Q9/+IN27twp6eu96JycHM2dO1fjxo2TJC1fvlw+n08rVqzQlClTql1vWVmZysrKQvOlpaVNUj+q53S5FeVyR7oMALBeg0L6xRdf1LJlyzRp0qTGrifMTTfdpBdffFEfffSRevfurb///e/atm2bcnJyJH192L2wsFDp6emh13g8Hg0dOlR5eXk1hnR2drZ+85vfNGntAABcqgaFdHl5uYYMGdLYtVTxi1/8QiUlJbr66qsVFRWlyspKPfXUU7rnnnskSYWFhZIkn88X9jqfz6fDhw/XuN45c+Zo5syZofnS0lIlJiY2wQgAAGi4Bp049sADD2jFihWNXUsVf/zjH/X6669rxYoV2rVrl5YvX67f/va3Wr58eVi/bx9uN8bUegje4/GoQ4cOYRMAALZp0J70+fPn9dJLL2njxo265ppr5HaHf744f/78Rinuscce0+OPP667775bktSvXz8dPnxY2dnZmjx5shISEiR9vUfdtWvX0OuKioqq7F0DANDSNCik9+zZo2uvvVaStG/fvrC2xjyJ7OzZs3I6w3f2o6Kiwq7XTkhIUG5urq677jpJXx+K37Jli5555plGqwMAgEhoUEhv2rSpseuo1tixY/XUU0+pR48e6tu3rz744APNnz9f9913n6Sv/yHIyMhQVlaWUlJSlJKSoqysLLVv314TJkxolhoBAGgqVt/SaeHChXriiSc0depUFRUVye/3a8qUKfr1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oXELt0xbGqvEeFuztjRWqW2NtzWNta5zMlp8SHfu3FlRUVEqLCwMW15UVCSfz1ftazwejzweT9iyyy+/vM7v1aFDhxb/C1FfbWmsEuNtzdrSWKW2Nd62MNYW/xSs6OhoDRgwQLm5uWHLc3NzNWTIkAhVBQDApWvxe9KSNHPmTE2aNEkDBw7U4MGD9dJLL+nIkSN66KGHIl0aAAAN1ipC+q677tLJkyc1b948nThxQqmpqXrzzTfVs2fPRlm/x+PRk08+WeUQeWvUlsYqMd7WrC2NVWpb421LY3UY0wruEAAAQCvU4j+TBgCgtSKkAQCwFCENAIClCGkAACxFSNdh8eLFSk5OVrt27TRgwAC9++67kS4pTGZmphwOR9iUkJAQajfGKDMzU36/XzExMUpLS9P+/fvD1lFWVqbp06erc+fOio2N1e23365jx46F9SkuLtakSZPk9Xrl9Xo1adIkffXVV2F9jhw5orFjxyo2NladO3fWI488UudjCOuydetWjR07Vn6/Xw6HQ2vXrg1rt218e/fu1dChQxUTE6Nu3bpp3rx59X56U11jvffee6ts6+9///stcqySlJ2drRtuuEFxcXHq0qWL7rjjDh08eDCsT2vZvvUZa2vavkuWLNE111wTutnI4MGD9Ze//CXU3lq2a7O4pBtnt3IrV640brfbvPzyy+bAgQNmxowZJjY21hw+fDjSpYU8+eSTpm/fvubEiROhqaioKNT+9NNPm7i4OLNq1Sqzd+9ec9ddd5muXbua0tLSUJ+HHnrIdOvWzeTm5ppdu3aZYcOGmf79+5tAIBDqc+utt5rU1FSTl5dn8vLyTGpqqhkzZkyoPRAImNTUVDNs2DCza9cuk5uba/x+v5k2bdolje/NN980c+fONatWrTKSzJo1a8LabRpfSUmJ8fl85u677zZ79+41q1atMnFxcea3v/1to4x18uTJ5tZbbw3b1idPngzr01LGaowxo0aNMkuXLjX79u0zu3fvNrfddpvp0aOHOX36dKhPa9m+9Rlra9q+69atM3/+85/NwYMHzcGDB80vf/lL43a7zb59+4wxrWe7NgdCuhbf+973zEMPPRS27OqrrzaPP/54hCqq6sknnzT9+/evti0YDJqEhATz9NNPh5adP3/eeL1e8+KLLxpjjPnqq6+M2+02K1euDPU5fvy4cTqd5q233jLG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q+3/05/+VCtXrtTvfvc7ffjhh3rxxRd12WWXSfr6OcBDhw7Vtddeq507d+qtt97S559/rvHjxzfXcIAWi8PdAMK8//77WrFihYYPHy5JKi8v12uvvaYrrrii2v4fffSR3njjDeXm5mrEiBGSpF69eoXalyxZouuvv15ZWVmhZa+++qoSExP10UcfqXfv3k04GqBlY08agP70pz/psssuU7t27TR48GDdfPPNWrhwoSSpZ8+eNQa0JO3evVtRUVEaOnRote35+fnatGmTLrvsstB09dVXS5L+93//t/EHA7Qi7EkD0LBhw7RkyRK53W75/X653e5QW2xsbK2vjYmJqbU9GAxq7NixeuaZZ6q0de3atWEFA20EIQ1AsbGxuvLKKxv02n79+ikYDGrLli2hw93fdP3112vVqlVKSkqSy8VbDnAxONwN4JIkJSVp8uTJuu+++7R27VoVFBRo8+bNeuONNyRJDz/8sL788kvdc889ev/99/Xpp59qw4YNuu+++1RZWRnh6gG7EdIALtmSJUv04x//WFOnTtXVV1+tBx98MHQzFL/fr7/+9a+qrKzUqFGjlJqaqhkzZsjr9crp5C0IqI3DGGMiXQQAAKiKf2MBALAUIQ0AgKUIaQAALEVIAwBgKUIaAABLEdIAAFiKkAYAwFKENAAAliKkAQCwFCENAIClCGkAACz1/wC5ISpjg3LmmgAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 500x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.displot(df['Price'])\n",
    "plt.show()"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "0af1789e",
   "metadata": {},
   "source": [
    "### Correlation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "22d63ccb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 640x480 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "corr = df.corr()\n",
    "sns.heatmap(corr,annot=True,cmap='RdBu')\n",
    "plt.show()"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "ba91d097",
   "metadata": {},
   "source": [
    "#### Inference\n",
    "1) RAM and Price are positively affecting the Price. They have high corr with Price."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "70ddd411",
   "metadata": {},
   "source": [
    "### Outlier Treatment"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "8ac92bd6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['Ram', 'Weight', 'Price', 'Touchscreen', 'Ips', 'HDD', 'SSD'], dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print(num_cols)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "f4df54e7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAggAAAHFCAYAAACXYgGUAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAg1klEQVR4nO3deXRU5f3H8c9A9hBigGwYDFhkl6XEhYAQGkkJSFVqBcFKissBQQX8oaJHgapA8UiFIougVCprFRDhgGAhoAVt2ATRCi2yWDYbUSCQEJLn9wfNlOGbsDXJQPJ+nZNzmHvvzPPMIyZv7p3JeJxzTgAAAGep4u8JAACAKw+BAAAADAIBAAAYBAIAADAIBAAAYBAIAADAIBAAAIBBIAAAAINAAAAABoEAnOOPf/yjPB6Pz1d0dLRSUlK0ZMkSf0/Pq27dusrIyLjk+504cUIjRoxQZmbmRd9n8+bN6tChgyIjI+XxePTaa69d8riX4tz1r169upKTkzVnzpwyHRfAfwX4ewLAlWrGjBlq1KiRnHM6ePCgJk6cqG7dumnx4sXq1q2bv6d32U6cOKGRI0dKklJSUi7qPn379lVOTo7mzp2rqKgo1a1bt+wm+B/33HOPnnzySTnn9M0332jUqFHq1auXnHPq1atXmY8PVHYEAlCCZs2aKSkpyXu7c+fOioqK0pw5c67qQLgcX3zxhR5++GGlp6eXyuPl5+fL4/EoIKDkb0GxsbG69dZbJUlt2rRR27ZtVbduXU2dOpVAAMoBlxiAixQSEqKgoCAFBgb6bP/+++/16KOP6tprr1VQUJCuv/56Pffcc8rLy5Mk5ebmqlWrVqpfv75+/PFH7/0OHjyouLg4paSkqKCgQJKUkZGhatWqafv27UpNTVV4eLiio6M1cOBAnThx4oJz3Lt3r+6//37FxMQoODhYjRs31quvvqrCwkJJ0u7duxUdHS1JGjlypPcUfkmXKoout5w+fVqTJ0/2Hl/kiy++0J133qmoqCiFhISoZcuWevvtt30eIzMzUx6PR3/605/05JNP6tprr1VwcLD+8Y9/XPD5nC0xMVHR0dE6dOiQz/Z58+YpLS1N8fHxCg0NVePGjfXMM88oJyfH57iitf373/+un//85woPD1d8fLzGjBkjSfr000/Vrl07hYeHq0GDBuZ5AJUNgQCUoKCgQKdPn1Z+fr6+/fZbDRo0SDk5OT7/es3NzVXHjh01c+ZMDRkyREuXLtX999+vsWPHqnv37pLOhMX8+fN1+PBh9e3bV5JUWFio3r17yzmnOXPmqGrVqt7HzM/PV5cuXZSamqpFixZp4MCBmjp1qnr06HHe+X733XdKTk7WihUr9OKLL2rx4sW6/fbb9X//938aOHCgJCk+Pl7Lly+XJD344INav3691q9fr+eff77Yx+zatavWr18v6cwp/6LjJenrr79WcnKytm/frgkTJmjBggVq0qSJMjIyNHbsWPNYw4YN0969ezVlyhR98MEHiomJuaj/DkV+/PFHff/992rQoIHP9p07d6pLly568803tXz5cg0aNEjz588v9ixPfn6+unfvrq5du+r9999Xenq6hg0bpmeffVZ9+vRR3759tXDhQjVs2FAZGRnauHHjJc0RqFAcAB8zZsxwksxXcHCwmzRpks+xU6ZMcZLc/Pnzfbb/7ne/c5LcihUrvNvmzZvnJLnXXnvNvfDCC65KlSo++51zrk+fPk6SGz9+vM/2l19+2Ulyn3zyiXdbYmKi69Onj/f2M8884yS5zz77zOe+/fv3dx6Px3399dfOOee+++47J8kNHz78otdEkhswYIDPtp49e7rg4GC3d+9en+3p6ekuLCzM/fDDD84551avXu0kufbt21/SeI8++qjLz893p06dcjt27HC/+MUvXEREhNuwYUOJ9yssLHT5+fluzZo1TpL7/PPPvfuK1va9997zbsvPz3fR0dFOktu0aZN3e3Z2tqtataobMmTIRc8ZqGg4gwCUYObMmcrKylJWVpaWLVumPn36aMCAAZo4caL3mFWrVik8PFz33HOPz32LTtn/5S9/8W6799571b9/fw0dOlQvvfSSnn32WXXq1KnYsXv37u1zu+isxerVq0uc76pVq9SkSRPdfPPNZi7OOa1aterCT/oSrFq1SqmpqapTp44Z78SJE94zDUV++ctfXtLjT5o0SYGBgQoKClKDBg20bNkyzZkzR61bt/Y5bteuXerVq5fi4uJUtWpVBQYGqkOHDpKkr776yudYj8ejLl26eG8HBASofv36io+PV6tWrbzba9SooZiYGO3Zs+eS5gxUJAQCUILGjRsrKSlJSUlJ6ty5s6ZOnaq0tDQ99dRT+uGHHyRJ2dnZiouL87kuL0kxMTEKCAhQdna2z/a+ffsqPz9fAQEBevzxx4sdNyAgQDVr1vTZFhcX5x2vJNnZ2YqPjzfba9eufcH7Xo5LHa+4Y8/n3nvvVVZWltatW6epU6cqIiJCPXv21M6dO73HHD9+XLfddps+++wzvfTSS8rMzFRWVpYWLFggSTp58qTPY4aFhSkkJMRnW1BQkGrUqGHGDwoKUm5u7iXNGahICATgEjRv3lwnT57Ujh07JEk1a9bUoUOH5JzzOe7w4cM6ffq0atWq5d2Wk5OjX//612rQoIFCQ0P10EMPFTvG6dOnzQ/XgwcPescrSc2aNXXgwAGzff/+/ZLkM5fScKnjnRtRFxIdHa2kpCS1adNGjzzyiBYtWqScnBwNHjzYe8yqVau0f/9+vfXWW3rooYfUvn17JSUlKSIi4jKeEYCzEQjAJdiyZYsked8JkJqaquPHj2vRokU+x82cOdO7v0i/fv20d+9eLViwQG+++aYWL16s3//+98WOM2vWLJ/bs2fPlnT+31uQmpqqL7/8Ups2bTJz8Xg86tixoyQpODhYkv3X9aVKTU31/oA+d7ywsDDvWxRLy2233aYHHnhAS5cu9V6+KIqOoudUZOrUqaU6NlAZ8XsQgBJ88cUXOn36tKQzp8sXLFiglStX6u6771a9evUkSQ888IBef/119enTR7t379aNN96oTz75RKNGjVKXLl10++23S5KmT5+ud955RzNmzFDTpk3VtGlTDRw4UE8//bTatm3r87qBoKAgvfrqqzp+/LhuuukmrVu3Ti+99JLS09PVrl27Euc7ePBgzZw5U127dtVvf/tbJSYmaunSpZo0aZL69+/vffV/RESEEhMT9f777ys1NVU1atRQrVq1LvmXHw0fPlxLlixRx44d9cILL6hGjRqaNWuWli5dqrFjxyoyMvKSHu9ivPjii5o3b56ef/55ffTRR0pOTlZUVJT69eun4cOHKzAwULNmzdLnn39e6mMDlY6/XyUJXGmKexdDZGSka9mypRs3bpzLzc31OT47O9v169fPxcfHu4CAAJeYmOiGDRvmPW7r1q0uNDTU5x0HzjmXm5vrWrdu7erWreuOHDninDvzSvvw8HC3detWl5KS4kJDQ12NGjVc//793fHjx33uf+67GJxzbs+ePa5Xr16uZs2aLjAw0DVs2NC98sorrqCgwOe4jz76yLVq1coFBwc7SeZxzqVi3sXgnHPbtm1z3bp1c5GRkS4oKMi1aNHCzZgxw+eYoncx/PnPfz7vGBcznnPODR061Elya9ascc45t27dOtemTRsXFhbmoqOj3UMPPeQ2bdrkJPnMpWhtz9WhQwfXtGlTsz0xMdF17dr1oucMVDQe5865eArAbzIyMvTuu+/q+PHj/p4KgEqO1yAAAACDQAAAAAaXGAAAgMEZBAAAYBAIAADAIBAAAIBx2b8oqbCwUPv371dERMQl/wpVAADgH845HTt2TLVr11aVKiWfJ7jsQNi/f7/5FDcAAHB12LdvnxISEkrcf9mBUPRhKPv27VP16tUv92EAAEA5Onr0qOrUqXPBDzW77EAouqxQvXp1AgEAgKvMhV4ewIsUAQCAQSAAAACDQAAAAAaBAAAADAIBAAAYBAIAADAIBAAAYBAIAADAIBAAAIBBIAAAAINAAAAABoEAAAAMAgEAABgEAgAAMAgEAABgEAgAAMAgEAAAgEEgAAAAg0AAAAAGgQAAAAwCAQAAGAQCAAAwCAQAAGAQCAAAwCAQAACAQSAAAACDQAAAAAaBAAAADAIBAAAYBAIAADAIBAAAYBAIAADACPD3BEqLc065ubnlPmZeXp4kKTIyUlWq0FsAgIqhwgRCbm6u0tPT/Tb+woULFRUV5bfxAQAoTfyTFwAAGBXmDMLZjre8T65K2T81T36uqm37c5mPAwBAeauQgeCqBEhVA8t+nIL8Mh8DAAB/4BIDAAAwCAQAAGAQCAAAwCAQAACAQSAAAACDQAAAAAaBAAAADAIBAAAYBAIAADAIBAAAYBAIAADAIBAAAIBBIAAAAINAAAAABoEAAAAMAgEAABgEAgAAMAgEAABgEAgAAMAgEAAAgEEgAAAAg0AAAAAGgQAAAAwCAQAAGAQCAAAwCAQAAGAQCAAAwCAQAACAQSAAAACDQAAAAAaBAAAADAIBAAAYBAIAADAIBAAAYBAIAADAIBAAAIBBIAAAAINAAAAABoEAAAAMAgEAABgEAgAAMAgEAABgEAgAAMAgEAAAgEEgAAAAg0AAAAAGgQAAAAwCAQAAGAQCAAAwCAQAAGAQCAAAwCAQAACAQSAAAACDQAAAAAaBAAAADAIBAAAYBAIAADAIBAAAYBAIAADAIBAAAIBBIAAAAINAAAAABoEAAAAMAgEAABgEAgAAMAgEAABgEAgAAMAgEAAAgEEgAAAAI8DfEzibc065ubmSpJCQEHk8Hj/P6MrDGgEAysMVdQYhNzdX6enpSk9P9/4QhC/WCABQHq6oQAAAAFcGAgEAABgEAgAAMAgEAABgEAgAAMAgEAAAgEEgAAAAg0AAAAAGgQAAAAwCAQAAGAQCAAAwCAQAAGAQCAAAwCAQAACAQSAAAACDQAAAAAaBAAAADAIBAAAYBAIAADAIBAAAYBAIAADAIBAAAIBBIAAAAINAAAAABoEAAAAMAgEAABgEAgAAMAgEAABgEAgAAMAgEAAAgEEgAAAAg0AAAAAGgQAAAAwCAQAAGAQCAAAwCAQAAGAQCAAAwCAQAACAQSAAAACDQAAAAAaBAAAADAIBAAAYBAIAADAIBAAAYBAIAADAIBAAAIBBIAAAAINAAAAABoEAAAAMAgEAABgEAgAAMAgEAABgEAgAAMAgEAAAgEEgAAAAg0AAAAAGgQAAAAwCAQAAGAQCAAAwCAQAAGAQCAAAwCAQAACAQSAAAACDQAAAAAaBAAAADAIBAAAYBAIAADAIBAAAYBAIAADAIBBwUVJSUrxfFdmIESOUkpKiESNG+HsqZa6y/DcFrkbr1q1Tjx49tG7dOr/NgUDABZ37A6Si/kA5dOiQMjMzJUmZmZk6dOiQfydUhqZNm3be2wD8Jzc3V+PGjdOhQ4c0btw45ebm+mUeBALwHwMHDvS5/dhjj/lpJmVv1qxZ570NwH9mzZql7OxsSVJ2drZmz57tl3kE+GXUEjjnvH++1GLyOf6sxylTZw2Tm5urkydPlvmQZz9PVw7Ps6SzBSkpKd5/bVcEy5cv13fffeez7fDhw1q+fLk6d+7sp1mVjTvuuKPE7UuWLCnn2QA427fffqvZs2d7v7875zR79mylpaUpISGhXOdy0YGQl5envLw87+2jR4+W+mTOfvy777778h+o8LSkoP99Qhc1zhn33Xdf2Y93jry8PIWFhZXZ41/oUkJFiYSCggK98sorxe575ZVX1KlTJ1WtWrWcZ1U2jhw5ouPHjxe77/jx4zpy5IiioqLKeVYApDMxMH78+BK3jx07Vh6Pp9zmc9GXGEaPHq3IyEjvV506dcpyXkC5WbJkiQoKCordV1BQUKH+Vd2zZ8//aT+AsrN3715lZWWZ70cFBQXKysrS3r17y3U+F30GYdiwYRoyZIj39tGjR0s9EoKDg71/XrhwoUJCQi76vrm5uf8961ClnK6cnDXOnDlzdM0115T5kGc/z7PXC5fvjjvu0IQJE4qNhICAgBJPyV+N5s6de96zc3Pnzi3H2QA423XXXaebbrpJmzZt8vl+VLVqVbVu3VrXXXdduc7non+SBgcHl/kPpLNPnYSEhCg0NPRyH6iUZnShcf77x/9pvpc7fBk/z8zMzPNeZqgIlxekM//zDR06VGPGjDH7nnrqqQpzeUGSoqKiVK1atWIvM1SrVo3LC4AfeTwePfHEE+rTp0+x28vz8oLEuxhwASVFQEWJgyKdO3dWdHS0z7aYmBilpaX5aUZlp6RLJhXpUgpwtUpISFCvXr28MeDxeNSrVy9de+215T4XAgH4j4kTJ/rc/sMf/uCnmZS93r17n/c2AP/p3bu3atasKUmqVauWevXq5Zd5EAi4oHPPFlS0swdFYmNjvZdUUlJSFBsb698JlaGHH374vLcB+E9ISIiGDBmi2NhYDR48+JJej1earqjfg4ArV0WNgnNVhl+xXKSy/DcFrkbJyclKTk726xw4gwAAAAwCAQAAGAQCAAAwCAQAAGAQCAAAwCAQAACAQSAAAACDQAAAAAaBAAAADAIBAAAYBAIAADAIBAAAYBAIAADAIBAAAIBBIAAAAINAAAAABoEAAAAMAgEAABgEAgAAMAgEAABgEAgAAMAgEAAAgEEgAAAAg0AAAAAGgQAAAAwCAQAAGAQCAAAwCAQAAGAQCAAAwCAQAACAQSAAAACDQAAAAAaBAAAADAIBAAAYBAIAADAIBAAAYBAIAADAIBAAAIBBIAAAAINAAAAABoEAAAAMAgEAABgEAgAAMAgEAABgEAgAAMAgEAAAgEEgAAAAg0AAAAAGgQAAAAwCAQAAGAQCAAAwCAQAAGAQCAAAwCAQAACAQSAAAACDQAAAAAaBAAAADAIBAAAYBAIAADAIBAAAYBAIAADAIBAAAIBBIAAAAINAAAAABoEAAAAMAgEAABgEAgAAMAgEAABgBPh7AmcLCQnRsmXLvH+GxRoBAMrDFRUIHo9HoaGh/p7GFY01AgCUBy4xAAAAg0AAAAAGgQAAAAwCAQAAGAQCAAAwCAQAAGAQCAAAwCAQAACAQSAAAACDQAAAAAaBAAAADAIBAAAYBAIAADAIBAAAYBAIAADAIBAAAIBBIAAAAINAAAAABoEAAAAMAgEAABgEAgAAMAgEAABgEAgAAMAgEAAAgEEgAAAAg0AAAAAGgQAAAAwCAQAAGAQCAAAwCAQAAGAQCAAAwCAQAACAQSAAAACDQAAAAAaBAAAADAIBAAAYBAIAADAIBAAAYBAIAADAIBAAAIBBIAAAAINAAAAABoEAAAAMAgEAABgEAgAAMAgEAABgEAgAAMAgEAAAgEEgAAAAg0AAAAAGgQAAAAwCAQAAGAQCAAAwCAQAAGAQCAAAwCAQAACAQSAAAACDQAAAAAaBAAAADAIBAAAYBAIAADAIBAAAYBAIAADAIBAAAIBBIAAAAINAAAAABoEAAAAMAgEAABgEAgAAMAL8PYGy4Ck8LVcu4xSUwygAAJS/ChkI1bbM8fcUAAC4qnGJAQAAGBXmDEJISIiWLVtWrmM655SXlydJioyMLNexAQAoSxUmEDwej0JDQ8t93LCwsHIfEwCAssYlBgAAYBAIAADAIBAAAIBBIAAAAINAAAAABoEAAAAMAgEAABgEAgAAMAgEAABgEAgAAMAgEAAAgEEgAAAAg0AAAAAGgQAAAAwCAQAAGAQCAAAwCAQAAGAQCAAAwCAQAACAQSAAAACDQAAAAAaBAAAADAIBAAAYBAIAADAIBAAAYBAIAADAIBAAAIBBIAAAAINAAAAABoEAAAAMAgEAABgEAgAAMAgEAABgBFzuHZ1zkqSjR4+W2mQAAEDZKvq5XfRzvCSXHQjHjh2TJNWpU+dyHwIAAPjJsWPHFBkZWeJ+j7tQQpSgsLBQ+/fvV0REhDwej9l/9OhR1alTR/v27VP16tUvZ4gKjzU6P9bnwlijC2ONzo/1ubCKtkbOOR07dky1a9dWlSolv9Lgss8gVKlSRQkJCRc8rnr16hViQcsSa3R+rM+FsUYXxhqdH+tzYRVpjc535qAIL1IEAAAGgQAAAIwyC4Tg4GANHz5cwcHBZTXEVY81Oj/W58JYowtjjc6P9bmwyrpGl/0iRQAAUHFxiQEAABgEAgAAMAgEAABgEAgAAMAok0CYNGmS6tWrp5CQELVu3Voff/xxWQxzVVi7dq26deum2rVry+PxaNGiRT77nXMaMWKEateurdDQUKWkpGj79u3+mawfjB49WjfddJMiIiIUExOju+66S19//bXPMZV9jSZPnqzmzZt7f0lLmzZttGzZMu/+yr4+xRk9erQ8Ho8GDRrk3VbZ12nEiBHyeDw+X3Fxcd79lX19JOlf//qX7r//ftWsWVNhYWFq2bKlNm7c6N1f2dao1ANh3rx5GjRokJ577jlt3rxZt912m9LT07V3797SHuqqkJOToxYtWmjixInF7h87dqzGjRuniRMnKisrS3FxcerUqZP3sy4qujVr1mjAgAH69NNPtXLlSp0+fVppaWnKycnxHlPZ1yghIUFjxozRhg0btGHDBv3sZz/TnXfe6f3GVNnX51xZWVl644031Lx5c5/trJPUtGlTHThwwPu1bds2777Kvj5HjhxR27ZtFRgYqGXLlunLL7/Uq6++qmuuucZ7TKVbI1fKbr75ZtevXz+fbY0aNXLPPPNMaQ911ZHkFi5c6L1dWFjo4uLi3JgxY7zbcnNzXWRkpJsyZYofZuh/hw8fdpLcmjVrnHOsUUmioqLc9OnTWZ9zHDt2zN1www1u5cqVrkOHDu6JJ55wzvH3yDnnhg8f7lq0aFHsPtbHuaefftq1a9euxP2VcY1K9QzCqVOntHHjRqWlpflsT0tL07p160pzqArhm2++0cGDB33WKzg4WB06dKi06/Xjjz9KkmrUqCGJNTpXQUGB5s6dq5ycHLVp04b1OceAAQPUtWtX3X777T7bWaczdu7cqdq1a6tevXrq2bOndu3aJYn1kaTFixcrKSlJv/rVrxQTE6NWrVpp2rRp3v2VcY1KNRD+/e9/q6CgQLGxsT7bY2NjdfDgwdIcqkIoWhPW6wznnIYMGaJ27dqpWbNmklijItu2bVO1atUUHBysfv36aeHChWrSpAnrc5a5c+dq48aNGj16tNnHOkm33HKLZs6cqQ8//FDTpk3TwYMHlZycrOzsbNZH0q5duzR58mTdcMMN+vDDD9WvXz89/vjjmjlzpqTK+Xfosj/N8XzO/fhn51yxHwmNM1ivMwYOHKitW7fqk08+Mfsq+xo1bNhQW7Zs0Q8//KD33ntPffr00Zo1a7z7K/v67Nu3T0888YRWrFihkJCQEo+rzOuUnp7u/fONN96oNm3a6Cc/+Ynefvtt3XrrrZIq9/oUFhYqKSlJo0aNkiS1atVK27dv1+TJk/XAAw94j6tMa1SqZxBq1aqlqlWrmpo6fPiwqS7I+wpi1kt67LHHtHjxYq1evdrnY8RZozOCgoJUv359JSUlafTo0WrRooXGjx/P+vzHxo0bdfjwYbVu3VoBAQEKCAjQmjVrNGHCBAUEBHjXorKv09nCw8N14403aufOnfw9khQfH68mTZr4bGvcuLH3BfaVcY1KNRCCgoLUunVrrVy50mf7ypUrlZycXJpDVQj16tVTXFycz3qdOnVKa9asqTTr5ZzTwIEDtWDBAq1atUr16tXz2c8aFc85p7y8PNbnP1JTU7Vt2zZt2bLF+5WUlKTevXtry5Ytuv7661mnc+Tl5emrr75SfHw8f48ktW3b1rzFeseOHUpMTJRUSb8XlfarHufOnesCAwPdm2++6b788ks3aNAgFx4e7nbv3l3aQ10Vjh075jZv3uw2b97sJLlx48a5zZs3uz179jjnnBszZoyLjIx0CxYscNu2bXP33Xefi4+Pd0ePHvXzzMtH//79XWRkpMvMzHQHDhzwfp04ccJ7TGVfo2HDhrm1a9e6b775xm3dutU9++yzrkqVKm7FihXOOdanJGe/i8E51unJJ590mZmZbteuXe7TTz91d9xxh4uIiPB+b67s6/O3v/3NBQQEuJdfftnt3LnTzZo1y4WFhbl33nnHe0xlW6NSDwTnnHv99dddYmKiCwoKcj/96U+9b1mrjFavXu0kma8+ffo45868dWb48OEuLi7OBQcHu/bt27tt27b5d9LlqLi1keRmzJjhPaayr1Hfvn29/z9FR0e71NRUbxw4x/qU5NxAqOzr1KNHDxcfH+8CAwNd7dq1Xffu3d327du9+yv7+jjn3AcffOCaNWvmgoODXaNGjdwbb7zhs7+yrREf9wwAAAw+iwEAABgEAgAAMAgEAABgEAgAAMAgEAAAgEEgAAAAg0AAAAAGgQAAAAwCAajAMjIy5PF45PF4FBAQoOuuu079+/fXkSNH/D01AFc4AgGo4Dp37qwDBw5o9+7dmj59uj744AM9+uij/p4WgCscgQBUcMHBwYqLi1NCQoLS0tLUo0cPrVixQpJUUFCgBx98UPXq1VNoaKgaNmyo8ePH+9w/IyNDd911l0aNGqXY2Fhdc801GjlypE6fPq2hQ4eqRo0aSkhI0FtvveWPpwegjAT4ewIAys+uXbu0fPlyBQYGSpIKCwuVkJCg+fPnq1atWlq3bp0eeeQRxcfH69577/Xeb9WqVUpISNDatWv117/+VQ8++KDWr1+v9u3b67PPPtO8efPUr18/derUSXXq1PHX0wNQiviwJqACy8jI0DvvvKOQkBAVFBQoNzdXkjRu3DgNHjy42PsMGDBAhw4d0rvvvut9jMzMTO3atUtVqpw56dioUSPFxMRo7dq1ks6ciYiMjNT06dPVs2fPcnhmAMoaZxCACq5jx46aPHmyTpw4oenTp2vHjh167LHHvPunTJmi6dOna8+ePTp58qROnTqlli1b+jxG06ZNvXEgSbGxsWrWrJn3dtWqVVWzZk0dPny4zJ8PgPLBaxCACi48PFz169dX8+bNNWHCBOXl5WnkyJGSpPnz52vw4MHq27evVqxYoS1btug3v/mNTp065fMYRZcking8nmK3FRYWlu2TAVBuOIMAVDLDhw9Xenq6+vfvr48//ljJyck+72r45z//6cfZAbhScAYBqGRSUlLUtGlTjRo1SvXr19eGDRv04YcfaseOHXr++eeVlZXl7ykCuAIQCEAlNGTIEE2bNk133XWXunfvrh49euiWW25RdnY2vyMBgCTexQAAAIrBGQQAAGAQCAAAwCAQAACAQSAAAACDQAAAAAaBAAAADAIBAAAYBAIAADAIBAAAYBAIAADAIBAAAIBBIAAAAOP/Acc+4+EZdQB/AAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAg0AAAHFCAYAAABxS8rQAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAAApCklEQVR4nO3de3hU1aH+8XdyJyEJEHLjToGEIqBcRHgqZkIsEoWClnqBCtF6jqTgtYhgTxGsHotFtK0KYjkolov1ArUgFCwZBAk0ARTRitgDhHMEIhEkEBJIsn5/8MucTDJJ1oSEZOL38zx5HmbttdZeay/IfrMvwWGMMQIAAKhDQFMPAAAA+AdCAwAAsEJoAAAAVggNAADACqEBAABYITQAAAArhAYAAGCF0AAAAKwQGgAAgBVCA77TXn31VTkcDo+v2NhYOZ1OrV27tqmH59atWzdlZGT43K6oqEhz5syRy+WybrNnzx6lpKQoOjpaDodDzz//vM/7tVFWVqY2bdooPT292rbnnntODodDd9xxR7Vtv/71r+VwOLR3717rfblcLjkcDp+OQ4VDhw7J4XBo/vz5ddZ97733NGfOHJ/3AfgLQgMgaenSpcrOztb27du1ePFiBQYGasyYMfrrX//a1EO7JEVFRZo7d65PJ8u7775bR48e1apVq5Sdna3bb7+9UcYWGBio4cOHa9u2bSotLfXY5nK5FBERoaysrGrtXC6XYmJi1K9fP+t9DRw4UNnZ2Ro4cOAlj7s27733nubOnduo+wCaEqEBkNS3b18NHTpUw4YN080336y1a9cqNDRUK1eubOqhXXb79u3T9ddfr/T0dA0dOlQJCQmX1N+FCxeqhYIKqampOnPmjHJzc91l5eXl2rp1qzIzM3X8+HH985//dG87f/68srOz5XQ65XA4rMcQFRWloUOHKioqqv4TAUBoALwJCwtTSEiIgoODPcq/+eYb/fznP1fHjh0VEhKi733ve/rlL3+pkpISSVJxcbEGDBignj176ttvv3W3O3bsmBISEuR0OlVWViZJysjIUOvWrfXpp58qLS1NERERio2N1bRp01RUVFTnGPPy8vTTn/5UcXFxCg0N1fe//309++yzKi8vl3TxsnpsbKwkae7cue7bLzXd5qi4VVNaWqqFCxe661fYt2+fxo4dq7Zt2yosLExXXXWVXnvtNY8+Km4DvP766/rFL36hjh07KjQ0VF9++aXXfaamprrbVfj444918uRJ/fu//7sSExM9rjbs3LlT586dc7eTpNzcXP3oRz9Su3btFBYWpgEDBujPf/6z13FVveLyyiuvKCkpSaGhoerTp49WrFihjIwMdevWzet4FyxYoO7du6t169YaNmyYduzY4d6WkZGhF198UZI8bncdOnTIa1+AXzLAd9jSpUuNJLNjxw5z4cIFc/78eXPkyBFz//33m4CAALNhwwZ33XPnzpn+/fubiIgIM3/+fLNx40bzq1/9ygQFBZkbb7zRXe+LL74wkZGR5pZbbjHGGFNWVmZGjBhh4uLizFdffeWuN3nyZBMSEmK6dOlinnrqKbNx40YzZ84cExQUZEaPHu0xzq5du5rJkye7P+fn55uOHTua2NhYs2jRIrNhwwYzbdo0I8lkZmYaY4wpLi42GzZsMJLMz372M5OdnW2ys7PNl19+6fVY5Ofnm+zsbCPJjB8/3l3fGGM+//xzExkZaXr06GGWLVtm1q1bZ+644w4jycybN8/dR1ZWlpFkOnbsaMaPH2/effdds3btWlNQUOB1n2VlZaZt27Zm5MiR7rJnn33WJCYmGmOMue2228xPfvIT97a5c+caSebTTz81xhizefNmExISYoYPH27eeOMNs2HDBpORkWEkmaVLl1YbV1ZWlrvs5ZdfNpLMj3/8Y7N27VqzfPlyk5SUZLp27Wq6du3qrnfw4EEjyXTr1s2MGjXKrFmzxqxZs8b069fPtG3b1pw6dcoYY8yXX35pxo8fbyS5j112drYpLi72OnfAHxEa8J1WERqqfoWGhpqXXnrJo+6iRYuMJPPnP//Zo3zevHlGktm4caO77I033jCSzPPPP29mz55tAgICPLYbczE0SDK/+93vPMqfeuopI8ls27bNXVY1NMycOdNIMjt37vRom5mZaRwOh9m/f78xxpivv/7aSDKPP/649TGRZKZOnepRdvvtt5vQ0FCTl5fnUZ6enm7Cw8PdJ86Kk/N1111nvb9x48aZiIgIc+HCBWOMMWPGjDG33367McaYl156ycTGxpry8nJjjDGpqakmLi7O3bZ3795mwIAB7rYVRo8ebRITE01ZWZnHuCpCQ1lZmUlISDDXXHONR7vDhw+b4OBgr6GhX79+prS01F3+j3/8w0gyK1eudJdNnTrV8LMYWjJu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37qUl5fXOP6oqCitWbNGAQHeL36XlZVp5MiRNY43MDDQ67bAwEBt3LhRgYGBki6Gg+uvv75e46/NunXrFB4e7vW4eluTusbx/vvvKyjo4s/0Na2XzVr74vTp04qOjq7z/H1JtyeefvppRUdHu786d+58Kd0BAGqwc+fOWgODdPHkmpOTU+u98by8POXk5PgUGCTV2W9dahv/6dOntXPnzhrbrl27ttbx1rStrKxMa9eudX+u6WrKpfq3f/u3Go+rtzWpaxyVt/vS7+VwSbcnZs2apYcfftj9ueJKQ0MKDQ11/3n16tUKCwtr0P7hqbi4+P+u7AQ0+7tX/q3S8eXvNqqq/G8xNDRU11xzjaKiouq80jBo0CB16dKlxjpdunTR1Vdf7fOVhiFDhtTab11qG390dLSuueaaGtuOHj1av//9772O1+FwKCAgwOu2oKAgjR492v150qRJjRIcXnnlFYWHh3s9rt7WpK5xTJo0yf3nmtbLZq0bwyWdFUJDQz1O6o2h8mWXsLAwtWrVqlH3h0oa4JIXasHfbViqODHOnj1b06dPr7XeAw88UOvl6oo6kydPtt5/UFBQnf3WpbbxP/744zXempAuniAfeeQR/eY3v6m2bdasWSovL/e6bcaMGe5bE9LFedx77716+eWX6zmL6nr06KGIiAhJ8npcva1JbePIzMx035qo3N6m38uBtycAwE8MHjxY/fr187rN4XBowoQJ6tixY539dOrUSRMmTHCfcBwOhyZNmuRxsqpPv3XxNv7+/ftr4MCBdbYdNWqUYmNjPcri4uI0cuTIWrdVdccddyg83PNZraCgoBpPvuHh4brzzjtr3F75d014O641HTtv4wgPD9dtt91Wra4v/TY2QgMA+JFf//rX7p/KAwIC1K5dO0lS+/btNWHCBOt+Jk6cqJiYGI+2CxcurFbP137rUnX8TzzxhHXbF154wePzH/7wB6ttVS1atMjj88KFC93Hom3bttXqVj5WlT366KPVyrwdV9txVP1c334bE6EBAPxImzZtNHHiRAUEBGjixImaPn264uPj9dBDD/n0XExYWJgefvhhj7a9evVy3yNv3759vfr1dfxt2rSxbhsfHy+n0ylJcjqdio+Pt9pWVZcuXdS3b19JUt++fdWrVy/3sXjkkUc8tnXp0sXjWFX8tB8QEKD09PRqfXs7rrbjqO35BF/6bUyX9MplVbavbPji3Llz7oVZv349930bWeXjfdlfQWwKTfnKZaV983cbVfG9D5fTZXnlEgAAfHcQGgAAgBVCAwAAsEJoAAAAVggNAADACqEBAABYITQAAAArhAYAAGCF0AAAAKwQGgAAgBVCAwAAsEJoAAAAVggNAADACqEBAABYITQAAAArhAYAAGCF0AAAAKwQGgAAgBVCAwAAsEJoAAAAVggNAADACqEBAABYITQAAAArhAYAAGCF0AAAAKwQGgAAgBVCAwAAsEJoAAAAVggNAADACqEBAABYITQAAAArhAYAAGCF0AAAAKwQGgAAgBVCAwAAsEJoAAAAVggNAADACqEBAABYITQAAAArhAYAAGCF0AAAAKwQGgAAgBVCAwAAsEJoAAAAVggNAADACqEBAABYITQAAAArhAYAAGCF0AAAAKwQGgAAgBVCAwAAsEJoAAAAVggNAADACqEBAABYITQAAAArhAYAAGCF0AAAAKwQGgAAgBVCAwAAsEJoAAAAVggNAADACqEBAABYITQAAAArhAYAAGCF0AAAAKwQGgAAgBVCAwAAsEJoAAAAVoKaegB1CQsL0/r1691/BoDvAr73oTlq9qHB4XCoVatWTT0MALis+N6H5ojbEwAAwAqhAQAAWCE0AAAAK4QGAABghdAAAACsEBoAAIAVQgMAALBCaAAAAFYIDQAAwAqhAQAAWCE0AAAAK4QGAABghdAAAACsEBoAAIAVQgMAALBCaAAAAFYIDQAAwAqhAQAAWCE0AAAAK4QGAABghdAAAACsEBoAAIAVQgMAALBCaAAAAFYIDQAAwAqhAQAAWCE0AAAAK4QGAABghdAAAACsEBoAAIAVQgMAALBCaAAAAFYIDQAAwAqhAQAAWCE0AAAAK4QGAABghdAAAACsEBoAAIAVQgMAALBCaAAAAFYIDQAAwAqhAQAAWCE0AAAAK4QGAABghdAAAACsEBoAAIAVQgMAALBCaAAAAFYIDQAAwAqhAQAAWCE0AAAAK4QGAABghdAAAACsEBoAAIAVQgMAALBCaAAAAFYIDQAAwAqhAQAAWCE0AAAAK4QGAABghdAAAACsEBoAAIAVQgMAALBCaAAAAFYIDQAAwAqhAQAAWCE0AAAAK4QGAABghdAAAACsBDX1ANB8OcpLZZp6EI2t7IL3P18GjvLSy7o/ALhUhAbUqPVHK5t6CJdV5MermnoIANCscXsCAABY4UoDPISFhWn9+vVNPYzLxhijkpISSVJoaKgcDkeTjCMsLKxJ9gsAviA0wIPD4VCrVq2aehiXVXh4eFMPAQD8ArcnAACAFUIDAACwQmgAAABWCA0AAMAKoQEAAFghNAAAACuEBgAAYIXQAAAArBAaAACAFUIDAACwQmgAAABWCA0AAMAKoQEAAFghNAAAACuEBgAAYIXQAAAArBAaAACAFUIDAACwQmgAAABWCA0AAMAKoQEAAFghNAAAACuEBgAAYIXQAAAArBAaAACAFUIDAACwQmgAAABWCA0AAMAKoQEAAFghNAAAACuEBgAAYIXQAAAArBAaAACAlaCG7MwYI0k6ffp0Q3YLAAAaUcV5u+I8XpMGDQ2FhYWSpM6dOzdktwAA4DIoLCxUdHR0jdsdpq5Y4YPy8nLt379fffr00ZEjRxQVFdVQXTcbp0+fVufOnVvs/KSWP0fm59+Yn/9r6XP0x/kZY1RYWKgOHTooIKDmJxca9EpDQECAOnbsKEmKiorym4NVHy19flLLnyPz82/Mz/+19Dn62/xqu8JQgQchAQCAFUIDAACw0uChITQ0VI8//rhCQ0MbuutmoaXPT2r5c2R+/o35+b+WPseWPL8GfRASAAC0XNyeAAAAVggNAADACqEBAABYITQAAAAr9QoNL730krp3766wsDANGjRIW7durbGuy+WSw+Go9vX555/Xe9CN6YMPPtCYMWPUoUMHORwOrVmzps42W7Zs0aBBgxQWFqbvfe97WrRoUeMPtJ58nZ+/rd/TTz+tq6++WpGRkYqLi9O4ceO0f//+Otv5yxrWZ37+tIYLFy5U//793b8UZ9iwYVq/fn2tbfxl7STf5+dPa+fN008/LYfDoQcffLDWev60hpXZzM/f17Aqn0PDG2+8oQcffFC//OUvtWfPHg0fPlzp6enKy8urtd3+/ft19OhR91evXr3qPejGdPbsWV155ZV64YUXrOofPHhQN954o4YPH649e/boscce0/3336+33367kUdaP77Or4K/rN+WLVs0depU7dixQ5s2bVJpaalGjhyps2fP1tjGn9awPvOr4A9r2KlTJ/3mN79Rbm6ucnNzNWLECI0dO1affvqp1/r+tHaS7/Or4A9rV1VOTo4WL16s/v3711rP39awgu38KvjjGnplfDRkyBAzZcoUj7LevXubmTNneq2flZVlJJmTJ0/6uqsmJ8msXr261jozZswwvXv39ii79957zdChQxtxZA3DZn7+vH7GGJOfn28kmS1bttRYx5/X0GZ+/r6Gbdu2NX/84x+9bvPntatQ2/z8de0KCwtNr169zKZNm0xKSop54IEHaqzrj2voy/z8dQ1r4tOVhvPnz2vXrl0aOXKkR/nIkSO1ffv2WtsOGDBAiYmJSktLU1ZWli+7bdays7OrHY8bbrhBubm5unDhQhONquH56/p9++23kqR27drVWMef19BmfhX8bQ3Lysq0atUqnT17VsOGDfNax5/XzmZ+Ffxt7aZOnaqbbrpJ119/fZ11/XENfZlfBX9bw5r49B9WnThxQmVlZYqPj/coj4+P17Fjx7y2SUxM1OLFizVo0CCVlJTo9ddfV1pamlwul6677rr6j7yZOHbsmNfjUVpaqhMnTigxMbGJRtYw/Hn9jDF6+OGHde2116pv37411vPXNbSdn7+t4SeffKJhw4apuLhYrVu31urVq9WnTx+vdf1x7XyZn7+tnSStWrVKu3btUm5urlV9f1tDX+fnj2tYm3r9L5cOh8PjszGmWlmF5ORkJScnuz8PGzZMR44c0fz58/3ygHnj7Xh4K/dH/rx+06ZN0969e7Vt27Y66/rjGtrOz9/WMDk5WR999JFOnTqlt99+W5MnT9aWLVtqPLH629r5Mj9/W7sjR47ogQce0MaNGxUWFmbdzl/WsD7z87c1rItPtyfat2+vwMDAalcV8vPzqyXF2gwdOlQHDhzwZdfNVkJCgtfjERQUpJiYmCYaVePyh/W777779O677yorK0udOnWqta4/rqEv8/OmOa9hSEiIevbsqcGDB+vpp5/WlVdeqd/97nde6/rj2vkyP2+a89rt2rVL+fn5GjRokIKCghQUFKQtW7bo97//vYKCglRWVlatjT+tYX3m501zXsO6+HSlISQkRIMGDdKmTZt08803u8s3bdqksWPHWvezZ8+eZnfJqb6GDRumv/71rx5lGzdu1ODBgxUcHNxEo2pczXn9jDG67777tHr1arlcLnXv3r3ONv60hvWZnzfNeQ2rMsaopKTE6zZ/Wrua1DY/b5rz2qWlpemTTz7xKLvrrrvUu3dvPfroowoMDKzWxp/WsD7z86Y5r2GdfH1yctWqVSY4ONgs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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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deutt9Y7b4cOHdS9e/eg29LS0iTJuV5tpaWlGjBggHN7enp6g+c2R2lpqXr16tXo+eobG861116rn/3sZ/J4PEpOTtagQYOCXoppynU/++wzSVKfPn1CjiktLVVVVZWeeOIJPfHEE/WO+fzzzxu5euDMQSAAjTB06FCtXbtW77//vi666CJ1795db731lswsKBIOHTqkqqoq9ejRI3DbiRMnNHnyZA0ePFgHDx7UDTfcoD/+8Y/OHFVVVSotLQ2KhJrX1OuGQ23du3fX/v37ndv37dsnSUFrOR2aOl/diGpISkpKUKCF0pjr1nyPxaeffhpyTNeuXRUbG6vJkyfr5ptvrnfMwIEDG5wLONPwEgPQCNu2bZP0ry84OTk5On78uF544YWgcU8//XTgeI1p06appKREq1at0uLFi/Xiiy/qP/7jP+qdZ+nSpUGfL1u2TJKUlZUVcm05OTnauXOntmzZ4qzF4/EoOztbkuT1eiVJX375ZZh72rCcnBxt2LAhEAS15+vYsWNUvc1w8ODBGjRokJ566qnAu0vq6tixo7Kzs7V161YNHTpUo0aNcn6FCzTgTMUzCEAdO3bsUFVVlaSvnn5etWqV1q9fr6uvvjrwf5I/+tGPNH/+fOXn52vPnj0aMmSI3njjDT300EO64oor9N3vfleS9Lvf/U7PPvuslixZovPPP1/nn3++CgoK9POf/1zf/va3g75vID4+XnPnztXx48d14YUXBt7FkJubq0suuSTkeu+44w49/fTTGj9+vGbPnq3+/ftr9erVWrBggaZPn67BgwdLkpKTk9W/f3/98Y9/VE5Ojrp166YePXrU+/JEODNnztRLL72k7Oxs3XffferWrZuWLl2q1atX65FHHpHP52vS9SJt/vz5ysvL08UXX6w77rhD/fr1U0lJidauXRsIsscee0yXXHKJvvOd72j69OkaMGCAjh07pg8//FB/+tOfTvv3cQBtQmt/lyQQLep7F4PP57Phw4fbvHnzrLy8PGh8aWmpTZs2zXr16mUdOnSw/v372z333BMYt337dktMTAx6x4GZWXl5uY0cOdIGDBhghw8fNrOv3sWQlJRk27dvt6ysLEtMTLRu3brZ9OnT7fjx40Hn130Xg5nZ3r17beLEida9e3eLi4uzb37zm/ab3/zGqqurg8a98sordsEFF5jX6zVJznXqUj3v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goKCltmIf/rzn/9sv/jFL2zlypUmyZ5//vmg49G0H0eOHLGePXvahAkTrLi42FauXGnJycn229/+tlX2Jj8/38aNGxf0WCotLQ0ac6buzdixY23JkiW2Y8cO27Ztm40fP9769etnx48fD4xpz4+dxuxPe338vPjii7Z69WrbtWuX7dq1y+69916Li4uzHTt2mFn7ftxESsQC4aKLLrJp06YF3XbOOefY3XffHakpI2rmzJk2bNiweo/5/X5LS0uzhx9+OHBbeXm5+Xw+W7RokZmZlZWVWVxcnC1fvjww5h//+IfFxMTYyy+/bGZmO3fuNEn25ptvBsYUFRWZJPv73/9uZl998YmJibF//OMfgTHPPfeceb1eO3LkyGm7v01R94tgtO3HggULzOfzWXl5eWDMnDlzLD093fx+/2ncCVeoQPje974X8pz2sjdmZocOHTJJ9uqrr5oZj5266u6PGY+f2rp27Wq/+93veNxESEReYjh16pTeeecdXX755UG3X3755SosLIzElC3igw8+UHp6ugYOHKgJEybo448/liTt3r1bBw4cCLq/Xq9XY8aMCdzfd955R5WVlUFj0tPTlZGRERhTVFQkn8+nb33rW4ExF198sXw+X9CYjIwMpaenB8aMHTtWFRUVeueddyJ355sg2vajqKhIY8aMCfrHT8aOHat9+/Zpz549p38DGmHTpk1KTU3V4MGDdeONN+rQoUOBY+1pb44cOSJJ6tatmyQeO3XV3Z8a7f3xU11dreXLl+vEiRPKzMzkcRMhEQmEzz//XNXV1erZs2fQ7T179tSBAwciMWXEfetb39LTTz+ttWvX6sknn9SBAwc0evRolZaWBu5TuPt74MABxcfHq2vXrmHHpKamOnOnpqYGjak7T9euXRUfHx81extt+1HfmJrPW2PPcnNztXTpUm3YsEFz587V5s2bddlll6mioiKwpvawN2amO++8U5dccokyMjKC5uSxU//+SO378VNcXKxOnTrJ6/Vq2rRpev7553XeeefxuImQZv80x8ao+2OgzSzkj4aOdrm5uYGPhwwZoszMTA0aNEi///3vA98g1Jz7W3dMfeObMyYaRNN+1LeWUOdG2nXXXRf4OCMjQ6NGjVL//v21evVqff/73w953pm2NwUFBdq+fbveeOMN5xiPndD7054fP9/85je1bds2lZWVaeXKlcrPz9err74adi3t7XFzOkXkGYQePXooNjbWKaVDhw45VdVWJSUlaciQIfrggw8C72YId3/T0tJ06tQpHT58OOyYgwcPOnN99tlnQWPqznP48GFVVlZGzd5G237UN6bmKdlo2LNevXqpf//++uCDDyS1j7255ZZb9OKLL2rjxo1BPzaex85XQu1PfdrT4yc+Pl5nn322Ro0apTlz5mjYsGF67LHHeNxESEQCIT4+XiNHjtT69euDbl+/fr1Gjx4diSlbXEVFhd577z316tVLAwcOVFpaWtD9PXXqlF599dXA/R05cqTi4uKCxuzfv187duwIjMnMzNSRI0f09ttvB8a89dZbOnLkSNCYHTt2aP/+/YEx69atk9fr1ciRIyN6nxsr2vYjMzNTr732WtDbkNatW6f09HQNGDDg9G9AE5WWluqTTz5Rr169JJ3Ze2NmKigo0KpVq7RhwwYNHDgw6Hh7f+w0tD/1aU+Pn7rMTBUVFe3+cRMxkfrux5q3OS5evNh27txpt99+uyUlJdmePXsiNWVEzZgxwzZt2mQff/yxvfnmm3bllVdacnJy4P48/PDD5vP5bNWqVVZcXGzXX399vW+x6dOnj73yyiu2ZcsWu+yyy+p9i83QoUOtqKjIioqKbMiQIfW+xSYnJ8e2bNlir7zyivXp06fF3+Z47Ngx27p1q23dutUk2bx582zr1q2Bt7FG036UlZVZz5497frrr7fi4mJbtWqVde7cOWJvOQq3N8eOHbMZM2ZYYWGh7d692zZu3GiZmZnWu3fvdrE306dPN5/PZ5s2bQp6m97JkycDY9rzY6eh/WnPj5977rnHXnvtNdu9e7dt377d7r33XouJibF169aZWft+3ERKxALBzGz+/PnWv39/i4+PtxEjRgS9VaetqXlPbVxcnKWnp9v3v/99e/fddwPH/X6/zZw509LS0szr9dqll15qxcXFQdf48ssvraCgwLp162aJiYl25ZVXWklJSdCY0tJSmzRpkiUnJ1tycrJNmjTJDh8+HDRm7969Nn78eEtMTLRu3bpZQUFB0NtpWsLGjRtNkvMrPz/fzKJvP7Zv327f+c53zOv1Wlpams2aNStibzcKtzcnT560yy+/3FJSUiwuLs769etn+fn5zv0+U/emvn2RZEuWLAmMac+PnYb2pz0/fqZOnRr4epKSkmI5OTmBODBr34+bSOHHPQMAAAc/iwEAADgIBAAA4CAQAACAg0AAAAAOAgEAADgIBAAA4CAQAACAg0AAEJCVlaXbb7+9tZcBIAoQCMAZasqUKfJ4PPJ4PIqLi9NZZ52ln/70pzpx4kTIc1atWqUHHnigBVcJIFpF9Mc9A2hd48aN05IlS1RZWanXX39dN9xwg06cOKGFCxcGjausrFRcXJy6devWSisFEG14BgE4g3m9XqWlpalv376aOHGiJk2apBdeeEGzZs3S8OHD9dRTT+mss86S1+uVmTkvMVRUVOiuu+5S37595fV69Y1vfEOLFy8OHN+5c6euuOIKderUST179tTkyZP1+eeft8I9BXC6EQhAO5KYmKjKykpJ0ocffqgVK1Zo5cqV2rZtW73jf/SjH2n58uV6/PHH9d5772nRokXq1KmTpK9+VO6YMWM0fPhw/e1vf9PLL7+sgwcP6tprr22puwMggniJAWgn3n77bS1btkw5OTmSpFOnTumZZ55RSkpKvePff/99rVixQuvXr9d3v/tdSdJZZ50VOL5w4UKNGDFCDz30UOC2p556Sn379tX777+vwYMHR/DeAIg0nkEAzmAvvfSSOnXqpISEBGVmZurSSy/VE088IUnq379/yDiQpG3btik2NlZjxoyp9/g777yjjRs3qlOnToFf55xzjiTpo48+Ov13BkCL4hkE4AyWnZ2thQsXKi4uTunp6YqLiwscS0pKCntuYmJi2ON+v195eXn69a9/7Rzr1atX8xYMIGoQCMAZLCkpSWeffXazzh0yZIj8fr9effXVwEsMtY0YMUIrV67UgAED1KEDf5UAZxpeYgBQrwEDBig/P19Tp07VCy+8oN27d2vTpk1asWKFJOnmm2/WF198oeuvv15vv/22Pv74Y61bt05Tp05VdXV1K68ewNdFIAAIaeHChbrmmmt000036ZxzztGNN94Y+IeW0tPT9de//lXV1dUaO3asMjIydNttt8nn8ykmhr9agLbOY2bW2osAAADRhcwHAAAOAgEAADgIBAAA4CAQAACAg0AAAAAOAgEAADgIBAAA4CAQAACAg0AAAAAOAgEAADgIBAAA4CAQAACA4/8BK61ybwi0crEAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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UK84goBGY+PGjZL+9Tr8nJwcHTp0SK+88krAerNmzfLfXmnEiBHauXOn5s+fr6effloLFizQH/7whyq3M3v27IDrc+bMkXTy9y3IycnR5s2b9f777ztj8Xg8/vcRCA8Pl6SAv3prIycnRytWrPAHwbHbi4yMrJOXJXbv3l0RERF67rnnApbv3r3b/5RHpdTUVG3ZsiXgLPzCwkLnlQn9+vVTaWmpZs6cedrHe84552jUqFHq06eP/9+lR48eiouL07Rp02RmNX7Mn/3sZyosLNTRo0f9R7iOvaSlpUmSLr/8cnm9Xm3btq3K9Y59CS/QUHEEAQ3SRx99pPLycknf71jmz5+vZcuW6eqrr9a5554rSbrpppv05JNPKjc3Vzt27NBPfvITrVmzRg8++KD69++v3r17S5JmzJih5557TgUFBerYsaM6duyoUaNG6e6771bPnj0DzhsICwvT5MmTdejQIf30pz/V2rVrNXHiRPXr10+XXHLJCcf761//WrNmzdKVV16p+++/XykpKXr11Vc1depUjRw5Uueff76k7//CTElJ0d/+9jfl5OSoadOmatasWY3f/Cg/P18LFy5Udna28vLy1LRpU82ePVuvvvqqHn74YcXFxdXo8arj7LPP1n333ad77rlHN910k66//noVFhZqwoQJ8vl8ys/P969744036qmnntIvfvELDR8+XIWFhXr44YedQ/bXX3+9CgoKNGLECH3yySfKzs5WRUWF3nnnHaWnp+u6666r9vi++eYbZWdna8iQIWrfvr1iYmK0fv16LV68WNdcc40kKTo6WpMnT9att96q3r17a/jw4WrRooW2bt2q//u//ws4x6Uq1113nWbPnq3+/ftrzJgxysjIUGhoqHbv3q2VK1dq4MCBuvrqq5Wamqr7779f9957r7Zv3+5/H48vv/xSf//73xUVFeV/wyygwarnkySBAFW9iiEuLs66dOlijz32mJWWlgasX1hYaCNGjLDExETzer2WkpJi48aN86/3wQcfWERERMArDsy+f8lh165dLTU11b7++msz+/5s8qioKPvggw8sKyvLIiIirGnTpjZy5Eg7dOhQwP2PfxWDmdnnn39uQ4YMsfj4eAsNDbW0tDR75JFH7OjRowHrLV++3C644AILDw83Sc7jHE9VvIrBzOzDDz+0AQMGWFxcnIWFhVnnzp2t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Nc8nO3JQiZMUAQCAg0AAAACOBhcI4eHhys/PV3h4eH0P5YzHXAcH8xwczHNwMM/B0RDmudYnKQIAgDNXgzuCAAAA6h+BAAAAHAQCAABwEAgAAMBRL4EwdepUnXvuufL5fOratatWr1590vXfeOMNde3aVT6fT23atNG0adOCNNLGrSbzPH/+fPXp00cJCQmKjY1V9+7dtWTJkiCOtnGr6c90pbfeekter1ddunSp2wGeIWo6z0eOHNG9996rlJQUhYeHq23btnrmmWeCNNrGq6bzPHv2bHXu3FmRkZFKTEzUzTffrMLCwiCNtnF68803NWDAALVq1Uoej0evvPLKKe8T9H2hBdnzzz9voaGhNn36dNu8ebONGTPGoqKi7PPPP69y/e3bt1tkZKSNGTPGNm/ebNOnT7fQ0FB78cUXgzzyxqWm8zxmzBh76KGH7O9//7tt2bLFxo0bZ6Ghofb+++8HeeSNT03nutLBgwetTZs21rdvX+vcuXNwBtuI1Waef/7zn9tFF11ky5Yts88++8zeeecde+utt4I46sanpvO8evVqCwkJsccff9y2b99uq1evto4dO9pVV10V5JE3LosWLbJ7773XXnrpJZNkL7/88knXr499YdADISMjw0aMGBGwrH379jZ27Ngq17/rrrusffv2Act++ctf2sUXX1xnYzwT1HSeq9KhQwebMGHC6R7aGae2cz148GD73e9+Z/n5+QRCNdR0nl977TWLi4uzwsLCYAzvjFHTeX7kkUesTZs2Acv++Mc/WlJSUp2N8UxTnUCoj31hUJ9i+O677/Tee++pb9++Acv79u2rtWvXVnmfdevWOetffvnlevfdd1VWVlZnY23MajPPx6uoqFBxcbGaNm1aF0M8Y9R2rgsKCrRt2zbl5+fX9RDPCLWZ5wULFqhbt256+OGH1bp1a51//vn67W9/q8OHDwdjyI1Sbea5R48e2r17txYtWiQz05dffqkXX3xRV155ZTCG/KNRH/vCWn9YU20cOHBAR48eVYsWLQKWt2jRQnv37q3yPnv37q1y/fLych04cECJiYl1Nt7GqjbzfLzJkyfr22+/1bXXXlsXQzxj1GauP/30U40dO1arV6+W1xvU/4KNVm3mefv27VqzZo18Pp9efvllHThwQLfddpu++uorzkM4gdrMc48ePTR79mwNHjxYpaWlKi8v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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAggAAAHFCAYAAACXYgGUAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAb8klEQVR4nO3de5CV9X348c+BhV1EIIAgIHQJKXirVygRbCIWNV5qGqfmMloD9RIxoVhNtBAdkdbWCY6XmEjsJJZERWI0mlovqTaoxWhtiDBo6GgqwcsQMGBBECEu+/39kR9blw8ou3HPYfH1mtk/zrPPOc9nv648b85zDqdSSikBAPAOXWo9AACw+xEIAEAiEACARCAAAIlAAAASgQAAJAIBAEgEAgCQCAQAIBEI0Abf/e53o1KptPoaMGBATJgwIe6///5aj9di+PDhMXny5Dbfb9OmTXHllVfGY489tsv3Wbx4cRxzzDHRp0+fqFQqccMNN7T5uG1RqVRi6tSpHXoMIKKu1gNAZzR37tw44IADopQSq1atim9+85tx6qmnxn333Rennnpqrcdrt02bNsWsWbMiImLChAm7dJ+zzz473nzzzfj+978fffv2jeHDh3fcgEDVCARohz/6oz+KMWPGtNw+8cQTo2/fvjF//vxOHQjt8dxzz8V5550XJ5100vvyeG+//XZUKpWoq/PHE9SSSwzwPmhoaIju3btHt27dWm1//fXX44tf/GLst99+0b179xgxYkRcdtllsWXLloiI2Lx5cxxxxBHxh3/4h7F+/fqW+61atSoGDRoUEyZMiK1bt0ZExOTJk2PvvfeOX/ziFzFx4sTo2bNnDBgwIKZOnRqbNm16zxlffvnl+Mu//MsYOHBg1NfXx4EHHhjXXnttNDc3R0TEihUrYsCAARERMWvWrJZLKDu7VLHtcktTU1N861vfatl/m+eeey7+/M//PPr27RsNDQ1x+OGHx/e+971Wj/HYY49FpVKJ2267Lb785S/HfvvtF/X19fE///M/7/nzbP8Yt99+e1x88cUxaNCg6NGjRxxzzDGxePHiVvsuX748Pve5z8WQIUOivr4+9t1335g4cWIsWbJkl48HHxQSHdph69at0dTUFKWUWL16dVxzzTXx5ptvxhlnnNGyz+bNm+PYY4+NF198MWbNmhWHHnpoLFy4MK6++upYsmRJPPDAA9HQ0BA/+MEPYvTo0XH22WfHD3/4w2hubo4zzzwzSikxf/786Nq1a8tjvv3223HyySfH+eefH9OnT48nn3wyrrrqqnjppZfiX//1X3c6729+85sYP358/Pa3v42///u/j+HDh8f9998fX/nKV+LFF1+MOXPmxODBg+PHP/5xnHjiiXHOOefEueeeGxHREg3bO+WUU+Kpp56KcePGxemnnx5f/vKXW773/PPPx/jx42PgwIFx4403Rv/+/eP222+PyZMnx+rVq+PSSy9t9VgzZsyIcePGxc033xxdunSJgQMHtvm/yVe/+tU48sgj4zvf+U6sX78+rrzyypgwYUIsXrw4RowYERERJ598cmzdujVmz54df/AHfxBr1qyJJ598MtatW9fm48EerwC7bO7cuSUi0ld9fX2ZM2dOq31vvvnmEhHlBz/4QavtX/va10pElIcffrhl25133lkiotxwww3liiuuKF26dGn1/VJKmTRpUomI8vWvf73V9n/4h38oEVGeeOKJlm2NjY1l0qRJLbenT59eIqI8/fTTre57wQUXlEqlUp5//vlSSim/+c1vSkSUmTNn7vKaRET50pe+1Grb5z73uVJfX19efvnlVttPOumkstdee5V169aVUkp59NFHS0SUj3/84+0+3rbHOPLII0tzc3PL9hUrVpRu3bqVc889t5RSypo1a1rWGHhvLjFAO9x6663xs5/9LH72s5/FQw89FJMmTYovfelL8c1vfrNlnwULFkTPnj3j9NNPb3XfbU/Z/+QnP2nZ9pnPfCYuuOCCuOSSS+Kqq66Kr371q3H88cfv8Nhnnnlmq9vbnrV49NFHdzrvggUL4qCDDoqxY8emWUopsWDBgvf+odtgwYIFMXHixBg2bFg63qZNm+Kpp55qtf0v/uIvfu9jnnHGGa0ucTQ2Nsb48eNb1qVfv37xkY98JK655pq47rrrYvHixS2XV4BMIEA7HHjggTFmzJgYM2ZMnHjiifFP//RPccIJJ8Sll17a8nT12rVrY9CgQa1OWhERAwcOjLq6uli7dm2r7WeffXa8/fbbUVdXF9OmTdvhcevq6qJ///6ttg0aNKjleDuzdu3aGDx4cNo+ZMiQ97xve7T1eDvat622rcP227Ydq1KpxE9+8pP4xCc+EbNnz44jjzwyBgwYENOmTYsNGzb83seHPY1AgPfJoYceGm+99Va88MILERHRv3//WL16dZRSWu332muvRVNTU+yzzz4t2958880466yzYtSoUdGjR4+W6//ba2pqSifXVatWtRxvZ/r37x+//vWv0/aVK1dGRLSa5f3Q1uNtH1HtsW0dtt/2znVpbGyMW265JVatWhXPP/98XHTRRTFnzpy45JJLfu/jw55GIMD7ZNsr4be9qG/ixImxcePG+NGPftRqv1tvvbXl+9tMmTIlXn755bjnnnvilltuifvuuy+uv/76HR5n3rx5rW7fcccdEfHu/27BxIkTY9myZfHMM8+kWSqVShx77LEREVFfXx8REW+99da7/KTvbeLEibFgwYKWIHjn8fbaa6846qijfq/H35H58+e3irGXXnopnnzyyZ2uy6hRo+Lyyy+PQw45JK0L4F0M0C7PPfdcNDU1RcTvni6/55574pFHHonTTjstPvzhD0dExOc///m46aabYtKkSbFixYo45JBD4oknnoh//Md/jJNPPjmOO+64iIj4zne+E7fffnvMnTs3Dj744Dj44INj6tSp8bd/+7dx9NFHt3rdQPfu3ePaa6+NjRs3xh//8R+3vIvhpJNOij/5kz/Z6bwXXXRR3HrrrXHKKafE3/3d30VjY2M88MADMWfOnLjgggti1KhRERHRq1evaGxsjH/5l3+JiRMnRr9+/WKfffZp8z9+NHPmzLj//vvj2GOPjSuuuCL69esX8+bNiwceeCBmz54dffr0adPj7YrXXnstTjvttDjvvPNi/fr1MXPmzGhoaIgZM2ZERMTSpUtj6tSp8elPfzpGjhwZ3bt3jwULFsTSpUtj+vTp7/s80OnV+EWS0Kns6F0Mffr0KYcffni57rrryubNm1vtv3bt2jJlypQyePDgUldXVxobG8uMGTNa9lu6dGnp0aNHq3cclFLK5s2by+jRo8vw4cPL//7v/5ZSfvcuhp49e5alS5eWCRMmlB49epR+/fqVCy64oGzcuLHV/bd/F0Mppbz00kvljDPOKP379y/dunUr+++/f7nmmmvK1q1bW+337//+7+WII44o9fX1JSLS42wvdvAuhlJKefbZZ8upp55a+vTpU7p3714OO+ywMnfu3Fb7bHsHwl133fWux3i34217jNtuu61MmzatDBgwoNTX15ePfexjZdGiRS37rV69ukyePLkccMABpWfPnmXvvfcuhx56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21m1Z503bdoUXbq0PpV07do1Iv7vb7j8/mpyLuywlz/uxLa30Nxyyy1l2bJl5W/+5m9Kz549y4oVK0oppUyfPr2cddZZLftve2vHRRddVJYtW1ZuueUWb3PcBW1d5zvuuKPU1dWVm266qfz6179u+Vq3bl2tfoROo61rvT3vYtg1bV3nDRs2lKFDh5bTTz+9/OIXvyiPP/54GTlyZDn33HNr9SN0Cm1d57lz55a6uroyZ86c8uKLL5YnnniijBkzpowdO7ZWP0KnsGHDhrJ48eKyePHiEhHluuuuK4sXL255O+nucC6seiCUUspNN91UGhsbS/fu3cuRRx5ZHn/88ZbvTZo0qRxzzDGt9n/sscfKEUccUbp3716GDx9evvWtb1V54s6pLet8zDHHlIhIX5MmTar+4J1QW3+n30kg7Lq2rvN///d/l+OOO6706NGjDB06tFx88cVl06ZNVZ6682nrOt94443loIMOKj169CiDBw8uZ555Znn11VerPHXn8uijj77rn7m7w7nQxz0DAInPYgAAEoEAACQCAQBIBAIAkAgEACARCABAIhAAgEQgAACJQIAPoMmTJ8enPvWpWo8B7MYEAgCQCAT4gJswYUJMnTo1pk6dGh/60Ieif//+cfnll7f6JL45c+bEyJEjo6GhIfbdd984/fTTazgxUA11tR4AqL3vfe97cc4558TTTz8dixYtii984QvR2NgY5513XixatCimTZsWt912W4wfPz5ef/31WLhwYa1HBjqYQABi2LBhcf3110elUon9998/nn322bj++uvjvPPOi5dffjl69uwZf/Znfxa9evWKxsbGOOKII2o9MtDBXGIA4qijjopKpdJye9y4cfHLX/4ytm7dGscff3w0NjbGiBEj4qyzzop58+bFpk2bajgtUA0CAXhXvXr1imeeeSbmz58fgwcPjiuuuCIOO+ywWLduXa1HAzqQQADiP//zP9PtkSNHRteuXSMioq6uLo477riYPXt2LF26NFasWBELFiyoxahAlXgNAhCvvPJKXHzxxXH++efHM888E9/4xjfi2muvjYiI+++/P5YvXx4f//jHo2/fvvHggw9Gc3Nz7L///jWeGuhIAgGIz3/+8/HWW2/F2LFjo2vXrvHXf/3X8YUvfCEiIj70oQ/FPffcE1deeWVs3rw5Ro4cGfPnz4+DDz64xlMDHalS3vlmZ+ADZ8KECXH44YfHDTfcUOtRgN2I1yAAAIlAAAASlxgAgMQzCABAIhAAgEQgAACJQAAAEoEAACQCAQBIBAIAkAgEACARCABA8v8AUhZVs+bi9REAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAggAAAHFCAYAAACXYgGUAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAgVklEQVR4nO3dfZRU9X348c8gsLsibkDYLCsKxNSoQFAxidJUURLqRsT4TEUDNeEcqZhYTXyox6CtjRGP1rTGh54o1cRGTQ5alULFACZGNBwfIqBBc4KgBcRQeRJ23WW/vz/6Y8L45bmLM+Drdc6cs3Pn3jvfL3fGeXtnZreQUkoBALCZDuUeAABQeQQCAJARCABARiAAABmBAABkBAIAkBEIAEBGIAAAGYEAAGQEAnzIv/3bv0WhUCi59OzZM4YOHRpPPPFEuYdX1Ldv3xg7duxOb7d+/fq47rrrYvbs2Tu8zUsvvRQnnHBC1NbWRqFQiNtuu22n73dnFAqFmDBhwhZv+/nPfx6FQqFk/Nddd13J8dp3332jd+/e8Zd/+ZfxL//yL7F27dpsP2PHji3ZpkuXLtG3b98YOXJkTJ48OZqbm3fX9GCP0LHcA4BKNXny5DjssMMipRTLly+P22+/PU499dR47LHH4tRTTy338HbZ+vXr4/rrr4+IiKFDh+7QNhdeeGG8//778eCDD0a3bt2ib9++u2+A/wfTp0+P2tra+OCDD2Lp0qXxi1/8Iq644oq4+eab4/HHH49BgwaVrF9TUxMzZ86MiIgNGzbEW2+9FdOmTYtx48bFLbfcEtOnT4/evXuXYypQdgIBtmLAgAFxzDHHFK+ffPLJ0a1bt/jpT3+6RwfCrpg/f36MGzcuGhsb22V/LS0tUSgUomPH9v1P0ODBg6NHjx7F66NGjYoJEybECSecECNHjozXX389qqqqird36NAhjj322JJ9fO1rX4u//uu/jhEjRsRZZ50Vzz33XLuOEfYU3mKAHVRdXR2dO3eOTp06lSz/n//5n/ibv/mbOPDAA6Nz587xqU99Kq655priKeqmpqY46qij4tOf/nSsXr26uN3y5cujvr4+hg4dGhs3boyI/z3tvd9++8WCBQti2LBh0aVLl+jZs2dMmDAh1q9fv90xLlmyJM4///yoq6uLqqqqOPzww+OWW26Jtra2iIh48803o2fPnhERcf311xdPr2/trYpNb7e0trbGnXfeWVx/k/nz58dpp50W3bp1i+rq6jjyyCPjvvvuK9nH7Nmzo1AoxI9//OO4/PLL48ADD4yqqqr4/e9/v935tIdBgwbFNddcE0uWLImHHnpoh7YZPnx4jBs3Lp5//vn45S9/uZtHCJVJIMBWbNy4MVpbW6OlpSXefvvtuPTSS+P999+P8847r7hOU1NTnHjiiXH//ffHZZddFlOnTo3zzz8/Jk2aFGeccUZE/G9YPPzww7FixYq48MILIyKira0tRo8eHSml+OlPfxr77LNPcZ8tLS3xla98JYYNGxaPPvpoTJgwIe6+++4499xztzned999N4YMGRJPPvlk/MM//EM89thj8aUvfSm+/e1vF9/P79WrV0yfPj0iIr7+9a/HnDlzYs6cOXHttdducZ+nnHJKzJkzJyIizjrrrOL6ERELFy6MIUOGxIIFC+Kf//mfY8qUKXHEEUfE2LFjY9KkSdm+rr766liyZEncdddd8fjjj0ddXd0255NSitbW1uyyKXZ2xsiRIyMidurFfle2gb1KAkpMnjw5RUR2qaqqSnfccUfJunfddVeKiPTwww+XLL/ppptSRKQnn3yyuOyhhx5KEZFuu+229N3vfjd16NCh5PaUUhozZkyKiPSDH/ygZPk//uM/pohIzzzzTHFZnz590pgxY4rXr7rqqhQR6fnnny/Zdvz48alQKKSFCxemlFJ69913U0SkiRMn7vC/SUSkiy++uGTZqFGjUlVVVVqyZEnJ8sbGxrTvvvumVatWpZRSmjVrVoqIdPzxx+/U/W3vMmvWrOL6EydOTBGR3n333S3ub8OGDSkiUmNjY3HZmDFjUpcuXbY6htdeey1FRBo/fvwOjxv2Js4gwFbcf//9MXfu3Jg7d25MmzYtxowZExdffHHcfvvtxXVmzpwZXbp0ibPOOqtk202n7H/xi18Ul51zzjkxfvz4+M53vhM33HBD/N3f/V18+ctf3uJ9jx49uuT6prMWs2bN2up4Z86cGUcccUR8/vOfz8aSUip+GK+9zJw5M4YNGxYHHXRQdn/r168vnmnY5Mwzz9yp/Z9zzjnFf//NLzfddNNOjzWl9JFsA3sTH1KErTj88MOzDykuXrw4rrjiijj//PPjE5/4RKxcuTLq6+tL3pePiKirq4uOHTvGypUrS5ZfeOGFceedd0bnzp3jm9/85hbvt2PHjnHAAQeULKuvr4+IyPa3uZUrV27x2wUNDQ3b3XZXrFy5Mnr16rXD97eldbelZ8+eJf/+m7z55ps7tZ+IiMWLF5eMbXdtA3sTZxBgJ3z2s5+NDRs2xOuvvx4REQcccEC888472f9trlixIlpbW0s+Uf/+++/HBRdcEIceemjU1NTEN77xjS3eR2tra/biunz58uL9bc0BBxwQy5Yty5YvXbo0IqJkLO1hZ+/vwxH1UXrsscciYse/1rmr28DeRCDATnj55ZcjIorfBBg2bFisW7cuHn300ZL17r///uLtm1x00UWxZMmSmDJlStxzzz3x2GOPxT/90z9t8X4eeOCBkuv//u//HhHbfrEaNmxYvPrqq/Hiiy9mYykUCnHiiSdGRBS/5rdhw4ZtzHT7hg0bFjNnziwGweb3t++++2ZfHyyX3/72t/G9730v+vbtG+ecc84ObTNjxoz40Y9+FEOGDIkvfvGLu3mEUJm8xQBbMX/+/GhtbY2I/z1dPmXKlJgxY0acfvrp0a9fv4j43+/M//CHP4wxY8bEm2++GQMHDoxnnnkmvve978VXvvKV+NKXvhQRET/60Y/iJz/5SUyePDn69+8f/fv3jwkTJsSVV14Zf/7nf17yuYHOnTvHLbfcEuvWrYvPfe5z8eyzz8YNN9wQjY2N23yx+tu//du4//7745RTTom///u/jz59+sTUqVPjjjvuiPHjx8ehhx4aERFdu3aNPn36xH/8x3/EsGHDonv37tGjR4+d/uVHEydOjCeeeCJOPPHE+O53vxvdu3ePBx54IKZOnRqTJk2K2trandpfe3jhhReitrY2Wlpair8o6cc//nHU1dXF448/Hp07dy5Zv62trfh7Dpqbm2PJkiUxbdq0ePjhh+Pwww+Phx9++COfA1SM8n5GEirPlr7FUFtbm4488sh06623pqamppL1V65cmS666KLUq1ev1LFjx9SnT5909dVXF9d75ZVXUk1NTck3DlJKqampKQ0ePDj17ds3vffeeymlP32y/pVXXklDhw5NNTU1qXv37mn8+PFp3bp1Jdt/+FsMKaW0ePHidN5556UDDjggderUKX3mM59JN998c9q4cWPJek899VQ66qijUlVVVYqIbD8fFlv4FkNKKc2bNy+deuqpqba2NnXu3DkNGjQoTZ48uWSdTd9i+NnP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MgIBAMgIBAAgIxAAgIxAAAAyAgEAyAgEACAjEACAjEAAADICAQDICAQAICMQAICMQAAAMgIBAMgIBAAgIxAAgIxAAAAyAgEAyAgEACAjEACAjEAAADICAQDICAQAICMQAICMQAAAMgIBAMgIBAAgIxAAgIxAAAAyAgEAyAgEACAjEACAjEAAADICAQDICAQAICMQAICMQAAAMgIBAMgIBAAgIxAAgIxAAAAyAgEAyAgEACDTsdwD2JpC28ZIG1vKPQz42Cm0tZZ7CEAFqNhA2G/ez8o9BAD42PIWAwCQqagzCLW1tfHII49ERERVVVUUCoUyjwg+3qqrq8s9BKBMKioQOnToEN26dSv3MADgY89bDABARiAAABmBAABkBAIAkBEIAEBGIAAAGYEAAGQEAgCQEQgAQEYgAAAZgQAAZAQCAJARCABARiAAABmBAABkBAIAkBEIAEBGIAAAGYEAAGQEAgCQEQgAQEYgAAAZgQAAZAQCAJARCABARiAAABmBAABkBAIAkBEIAEBGIAAAGYEAAGQEAgCQEQgAQKbjrm6YUoqIiDVr1rTbYACA3WvT6/am1/Gt2eVAWLt2bUREHHTQQbu6CwCgTNauXRu1tbVbvb2QtpcQW9HW1hZLly6Nrl27RqFQ2OUBftiaNWvioIMOirfeeiv233//dttvJdnb52h+e769fY57+/wi9v45mt+uSynF2rVro6GhITp02PonDXb5DEKHDh2id+/eu7r5du2///575UHf3N4+R/Pb8+3tc9zb5xex98/R/HbNts4cbOJDigBARiAAAJmKC4SqqqqYOHFiVFVVlXsou83ePkfz2/Pt7XPc2+cXsffP0fx2v13+kCIAsPequDMIAED5CQQAICMQAICMQAAAMhUXCHfccUf069cvqqurY/DgwfGrX/2q3EParhtvvDE+97nPRdeuXaOuri6++tWvxsKFC0vWGTt2bBQKhZLLscceW7JOc3NzXHLJJdGjR4/o0qVLjBw5Mt5+++2Pcipbdd1112Xjr6+vL96eUorrrrsuGhoaoqamJoYOHRoLFiwo2Uclz69v377Z/AqFQlx88cURsWcev1/+8pdx6qmnRkNDQxQKhXj00UdLbm+vY/bee+/FBRdcELW1tVFbWxsXXHBBrFq1ajfPbtvza2lpiSuvvDIGDhwYXbp0iYaGhvja174WS5cu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T6UXX3wxnXTSSWnQoEGptbW1XFMruvzyy9Ps2bPTH/7wh/Tcc8+lESNGpK5duxaPzfe///1UW1ubpkyZkubNm5f+6q/+KvXq1WuPmV9KKW3cuDEdfPDB6corryxZvqcev7Vr16aXXnopvfTSSyki0q233ppeeuml4qf42+uYnXzyyemzn/1smjNnTpozZ04aOHBgGjFiRFnn19LSkkaOHJl69+6dXn755ZLnZXNzc0oppd///vfp+uuvT3Pnzk2LFi1KU6dOTYcddlg66qijKn5+7fmYLNf8tjfHTVavXp323XffdOedd2bbV/ox3N5rQ0qV/TysqEBIKaUf/vCHqU+fPqlz587p6KOPLvmqYKWKiC1eJk+enFJKaf369Wn48OGpZ8+eqVOnTunggw9OY8aMSUuWLCnZz4YNG9KECRNS9+7dU01NTRoxYkS2Trmce+65qVevXqlTp06poaEhnXHGGWnBggXF29va2tLEiRNTfX19qqqqSscff3yaN29eyT4qeX4ppfRf//VfKSLSwoULS5bvqcdv1qxZW3xcjhkzJqXUfsds5cqVafTo0alr166pa9euafTo0em9994r6/wWLVq01eflrFmzUkopLVmyJB1//PGpe/fuqXPnzumQQw5J3/zmN9PKlSsrfn7t+Zgs1/y2N8dN7r777lRTU5NWrVqVbV/px3B7rw0pVfbz0J97BgAyFfMZBACgcggEACAjEACAjEAAADICAQDICAQAICMQAICMQAAAMgIB9mJjx46Nr371q9ny2bNnR6FQiFWrVhV/LhQK0aFDh6itrY2jjjoqrrjiili2bFnJdtddd11x3Y4dO0aPHj3i+OOPj9tuuy2am5s/olkBHwWBAERExMKFC2Pp0qUxd+7cuPLKK+Opp56KAQMGxLx580rW69+/fyxbtiyWLFkSs2bNirPPPjtuvPHGGDJkSKxdu7ZMowfam0AAIiKirq4u6uvr49BDD41Ro0bFr3/96+jZs2eMHz++ZL2OHTtGfX19NDQ0xMCBA+OSSy6Jp59+OubPnx833XRTmUYPtDeBAGxRTU1NXHTRRfHrX/86VqxYsc11DzvssGhsbIwpU6Z8RKMDdreO5R4AsHs98cQTsd9++5Us27hx4w5te9hhh0VExJtvvhl1dXXbXffJJ5/ctUECFUcgwF7uxBNPjDvvvLNk2fPPPx/nn3/+drfd9MdeC4XCDq27I+sBewaBAHu5Ll26xKc//emSZW+//fYObfvaa69FRETfvn13aN1+/frt9PiAyuQzCMAWbdiwIf71X/81jj/++OjZs+c21/3d734X06dPjzPPPPMjGh2wuzmDAERExIoVK6KpqSnWrl0bL7zwQkyaNCn++Mc/Zh88bG1tjeXLl0dbW1usXLkyZs+eHTfccEMceeSR8Z3vfKdMowfam0AAIiLiM5/5TBQKhdhvv/3iU5/6VAwfPjwuu+yyqK+vL1lvwYIF0atXr9hnn32itrY2jjjiiLj66qtj/PjxUVVVVabRA+2tkDZ9CgkA4P/zGQQAICMQAICMQAAAMgIBAMgIBAAgIxAAgIxAAAAyAgEAyAgEACAjEACAjEAAADICAQDI/D9ma8INIw36aAAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAggAAAHFCAYAAACXYgGUAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAh7UlEQVR4nO3dd3SUZf6/8feEJJOEhKETerEs0pGgiHwpGxYEBAsi0gRZ9wgLSltFcFfUFUE8IHosWCMoRVHEAOIKUlYOCEiRtisWICAlgPSQkHL//vCXWcZPQgkJE8j1OifnMM9zz8w99+SQK88zM/E455wAAADOEhLsCQAAgMKHQAAAAAaBAAAADAIBAAAYBAIAADAIBAAAYBAIAADAIBAAAIBBIAAAAINAAHLx3nvvyePxBHyVK1dOrVu31vz584M9Pb8aNWqoX79+F329lJQUPfXUU1q2bNkFX2fDhg1q1aqVfD6fPB6PJk+efNH3ezEOHz6sUaNGqU6dOipevLh8Pp9q166tPn36aNOmTQFjV69erbvuukvVqlWT1+tVhQoVdMstt2jEiBEB41q3bu1/PkNCQhQTE6Nrr71W3bp108cff6ysrKwCfUzAlSI02BMACruEhATVrl1bzjnt379fr7zyijp37qzExER17tw52NPLs5SUFD399NOSfvuheSH69++vU6dOadasWSpVqpRq1KhRYPM7efKkmjVrppMnT+rRRx9Vw4YNdfr0aW3fvl1z5szRxo0b1aBBA0nSggUL1KVLF7Vu3VoTJkxQxYoVtW/fPn377beaNWuWJk6cGHDbtWrV0vTp0yVJp06d0o4dOzR37lx169ZN//d//6d58+bJ5/MV2GMDrggOQI4SEhKcJLd27dqA7SkpKc7r9boePXoEaWaBqlev7vr27XvR1zt48KCT5MaMGXPB1wkNDXUDBw686PvKzZkzZ1x6enqO+959910nyS1ZsiTH/ZmZmf5/t2zZ0l1zzTU53tbZ45xzrlWrVq5u3brnvM977733Qh8CcNXiFANwkSIiIhQeHq6wsLCA7b/++qv++te/qnLlygoPD1etWrX0xBNPKC0tTZKUmpqqxo0b69prr9WxY8f819u/f79iY2PVunVrZWZmSpL69eun6Ohobd26VfHx8SpevLjKlSunwYMHKyUl5bxzTEpKUu/evVW+fHl5vV7dcMMNmjhxov/w+c6dO1WuXDlJ0tNPP+0/5J7bqYrs0y0ZGRl6/fXX/eOzbdmyRXfccYdKlSqliIgINWrUSFOnTg24jWXLlsnj8ej999/XiBEjVLlyZXm9Xv3444853ufhw4clSRUrVsxxf0hISMDYsmXLKjTUHhQ9e9z5PPDAA+rYsaNmz56tXbt2XfD1gKsRgQCcR2ZmpjIyMpSenq49e/Zo6NChOnXqlHr27Okfk5qaqjZt2mjatGkaPny4FixYoN69e2vChAm6++67Jf0WFh999JGSk5PVv39/SVJWVpZ69eol55xmzpypYsWK+W8zPT1dHTt2VHx8vObOnavBgwfrjTfeUPfu3c8534MHD6p58+b68ssv9c9//lOJiYlq27at/va3v2nw4MGSfvuh+8UXX0iS/vznP2vVqlVatWqV/vGPf+R4m506ddKqVaskSffcc49/vCR9//33at68ubZu3aqXX35Zc+bMUZ06ddSvXz9NmDDB3NaoUaOUlJSkKVOmaN68eSpfvnyO93nLLbdIku6//37NnTvXHwy5jV29erUeeeQRrV69Wunp6edco3Pp0qWLnHP6+uuv83wbwFUh2IcwgMIq+xTD77+8Xq977bXXAsZOmTLFSXIfffRRwPbnn3/eSXJffvmlf9uHH37oJLnJkye7J5980oWEhATsd865vn37OknupZdeCtg+duxYJ8mtWLHCv+33pxgef/xxJ8mtXr064LoDBw50Ho/Hff/99865vJ1ikOQGDRoUsO2+++5zXq/XJSUlBWzv0KGDi4qKckePHnXOObd06VInybVs2fKC7++ZZ55x4eHh/rWvWbOmGzBggPvuu+8Cxh06dMi1aNHCPy4sLMw1b97cjRs3zp04cSJg7LlOMTjn3MKFC50k9/zzz1/wPIGrEUcQgPOYNm2a1q5dq7Vr12rhwoXq27evBg0apFdeecU/ZsmSJSpevLjuueeegOtmH7L/6quv/NvuvfdeDRw4UI8++qieffZZjR49Wn/6059yvO9evXoFXM4+arF06dJc57tkyRLVqVNHN910k5mLc05Lliw5/4O+CEuWLFF8fLyqVq1q7i8lJcV/pCFb165dL/i2//GPfygpKUnvvvuuHnroIUVHR2vKlClq0qSJZs6c6R9XpkwZff3111q7dq3Gjx+vO+64Q9u3b9eoUaNUv359HTp06ILv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FWrt27d3CQkJbsuWLW7jxo2uU6dOrlq1au7kyZP+MePHj3cxMTHuk08+cZs3b3bdu3d3FStWdMePH/ePGTBggKtcubJbtGiRW79+vWvTpo1r2LChy8jICMbDKpTWrFnjatSo4Ro0aOCGDBni38765t2vv/7qqlev7vr16+dWr17tduzY4RYvXux+/PFH/xjWN++effZZV6ZMGTd//ny3Y8cON3v2bBcdHe0mT57sH8P6XpzPP//cPfHEE+6TTz5xktynn34asD+/1vO2225z9erVcytXrnQrV6509erVc7fffvvlepiuUAXCTTfd5AYMGBCwrXbt2u7xxx8P0oyuTMnJyU6SW758uXPOuaysLBcbG+vGjx/vH5Oamup8Pp+bMmWKc865o0ePurCwMDdr1iz/mF9++cWFhIS4L7744vI+gELqxIkT7rrrrnOLFi1yrVq18gcC63tpRo4c6Vq0aJHrftb30nTq1Mn1798/YNvdd9/tevfu7ZxjfS/V7wMhv9Zz27ZtTpL75ptv/GNWrVrlJLn//ve/BfyoflNoTjGcOXNG69atU7t27QK2t2vXTitXrgzSrK5Mx44dkySVLl1akrRjxw7t378/YG29Xq9atWrlX9t169YpPT09YEylSpVUr1491v//GzRokDp16qS2bdsGbGd9L01iYqLi4uLUrVs3lS9fXo0bN9Zbb73l38/6XpoWLVroq6++0vbt2yVJ3333nVasWKGOHTtKYn3zW36t56pVq+Tz+XTzzTf7xzRr1kw+n++yrXme/1hTfjt06JAyMzNVoUKFgO0VKlTQ/v37gzSrK49zTsOHD1eLFi1Ur149SfKvX05ru2vXLv+Y8PBwlSpVyoxh/aVZs2Zp3bp1+vbbb80+1vfS/Pzzz3r99dc1fPhwjR49WmvWrNEjjzwir9er+++/n/W9RCNHjtSxY8dUu3ZtFStWTJmZmRo7dqx69Oghie/f/JZf67l//36VL1/e3H758uUv25oXmkDI9vs/He2cy9c/J321Gzx4sDZt2qQVK1aYfXlZW9Zf2r17t4YMGaIvv/xSERERuY5jffMmKytLcXFxeu655yRJjRs31tatW/X666/r/vvv949jffPmww8/1AcffKAZM2aobt262rhxo4YOHapKlSqpb9++/nGsb/7Kj/XMafzlXPNCc4qhbNmyKlasmCmj5ORk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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "for i in num_cols:\n",
    "    sns.boxplot(x=df[i])\n",
    "    plt.title(f'Boxplot for {i}')\n",
    "    plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "4ef8df3a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(46, 12)\n",
      "(1272, 12)\n",
      "0.036163522012578615\n"
     ]
    }
   ],
   "source": [
    "print(df[df['Weight']>3.5].shape)\n",
    "print(df.shape)\n",
    "print(46/1272)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "b4b65368",
   "metadata": {},
   "source": [
    "#### Applying Outlier Treatment on Weight"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "a5119ba8",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Dell\\anaconda3\\lib\\site-packages\\seaborn\\_decorators.py:36: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAggAAAHFCAYAAACXYgGUAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAhHUlEQVR4nO3deXTV5Z348c9lSYJsAgUSEMFCE+uOtRZO1STSqrjUpdba2gq1nqlU6xxbx1FnRouj4zB16xmrVOugdqy2KlrHrdiS4BYsVJSqFWsH0TOCVNTKLoHn94e/XAlPkE24QV6vc3JO7vd+l+c+fs198733JoWUUgoAgLV0KPUAAID2RyAAABmBAABkBAIAkBEIAEBGIAAAGYEAAGQEAgCQEQgAQEYgsMO4+eabo1AotPrq27dv1NXVxf3331/q4RUNGTIkxo4du8nbLVu2LH74wx9GY2PjRm8za9asqK2tjZ49e0ahUIhrrrlmk4+7MVavXh0777xzjB49Orvv6quvjkKhEF/72tey+/71X/81CoVCzJ49e6OP1djYGIVCYZPmocUrr7wShUIhrrjiig2u++CDD8YPf/jDTT4GbC8EAjucSZMmRVNTUzz55JNxww03RMeOHeOYY46J//mf/yn10LbIsmXLYvz48Zv0xHjaaafF/Pnz44477oimpqY4+eSTt8rYOnbsGAcffHA8/vjj0dzc3Oq+xsbG6Nq1azQ0NGTbNTY2Rp8+fWLvvffe6GPtv//+0dTUFPvvv/8Wj/vDPPjggzF+/PitegwoJYHADmevvfaKESNGxMiRI+P444+P+++/P8rLy+P2228v9dC2ueeeey6+8IUvxOjRo2PEiBFRWVm5RftbtWpVFgAt6uvrY8mSJTFz5szisjVr1sRjjz0W48aNizfeeCP+9Kc/Fe977733oqmpKerq6qJQKGz0GHr06BEjRoyIHj16bP4DAQQCVFRURFlZWXTu3LnV8rfeeiu++93vxsCBA6OsrCw++clPxj/90z/FypUrIyJixYoVMXz48Bg2bFj87W9/K263YMGCqKysjLq6uli9enVERIwdOza6desWzz//fIwaNSq6du0affv2jbPOOiuWLVu2wTG++uqr8Y1vfCP69esX5eXl8elPfzquvPLKWLNmTUS8f2m8b9++ERExfvz44kso63upouXllubm5rj++uuL67d47rnn4thjj41evXpFRUVF7LfffnHLLbe02kfLpfyf//zn8YMf/CAGDhwY5eXl8fLLL7d5zPr6+uJ2LZ599tl4++234+/+7u+iqqqq1VWEp556KpYvX17cLiJi5syZ8aUvfSl69+4dFRUVMXz48PjVr37V5rjWvZJy4403RnV1dZSXl8cee+wRv/jFL2Ls2LExZMiQNsd71VVXxW677RbdunWLkSNHxvTp04v3jR07Nn7yk59ERLR6yeqVV15pc1+wXUqwg5g0aVKKiDR9+vS0atWq9N5776XXXnstnX322alDhw7p4YcfLq67fPnytM8++6SuXbumK664Ik2ZMiX9y7/8S+rUqVM68sgji+u99NJLqXv37umEE05IKaW0evXqdOihh6Z+/fql119/vbjemDFjUllZWdp1113TZZddlqZMmZJ++MMfpk6dOqWjjz661TgHDx6cxowZU7y9cOHCNHDgwNS3b980ceLE9PDDD6ezzjorRUQaN25cSimlFStWpIcffjhFRPr2t7+dmpqaUlNTU3r55ZfbnIuFCxempqamFBHpxBNPLK6fUkovvvhi6t69exo6dGi69dZb0wMPPJC+9rWvpYhIEyZMKO6joaEhRUQaOHBgOvHEE9N9992X7r///rRo0aI2j7l69erUq1evdNhhhxWXXXnllamqqiqllNJXv/rV9JWvfKV43/jx41NEpOeffz6llNLUqVNTWVlZOvjgg9Mvf/nL9PDDD6exY8emiEiTJk3KxtXQ0FBc9tOf/jRFRPryl7+c7r///nTbbbel6urqNHjw4DR48ODienPnzk0RkYYMGZKOOOKIdO+996Z777037b333qlXr17pnXfeSSml9PLLL6cTTzwxRURx7pqamtKKFSvafOywPRII7DBaAmHdr/Ly8nTddde1WnfixIkpItKvfvWrVssnTJiQIiJNmTKluOyXv/xlioh0zTXXpIsuuih16NCh1f0pvR8IEZF+/OMft1p+2WWXpYhIjz/+eHHZuoFw/vnnp4hITz31VKttx40blwqFQpozZ05KKaW//vWvKSLSxRdfvNFzEhHpzDPPbLXs5JNPTuXl5enVV19ttXz06NFpp512Kj5JtjwRH3LIIRt9vOOOOy517do1rVq1KqWU0jHHHJNOPvnklFJK1113Xerbt29as2ZNSiml+vr61K9fv+K2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BAAgIxAAgIxAAAAyAgEAyAgEACAjEACAjEAAADICAQDICAQAICMQAICMQAAAMgIBAMgIBAAgIxAAgIxAAAAyAgEAyAgEACAjEACAjEAAADICAQDICAQAICMQAICMQAAAMgIBAMgIBAAgIxAAgIxAAAAyAgEAyAgEACAjEACAjEAAADICAQDICAQAICMQAICMQAAAMgIBAMgIBAAgIxAAgIxAAAAyAgEAyAgEACAjEACAjEAAADICAQDICAQAICMQAICMQAAAMp1KPYC1pZSK369YsaKEI6GUWv23X+ucYAfj5wE7qLXP91TCn4EbHQgrV66MlStXFm+/++67H/lg1t7/8ccf/5Hvn+3QmuaIKCv1KCiFNc3Fb/08YEe1cuXK2GmnnUpy7I1+ieHyyy+Pnj17Fr8GDRq0NccFAJTQRl9BuOCCC+L73/9+8fa77777kUdCeXl58ft77rknKioqPtL9s31YsWLFB/9i7NCuXgVjW1rrv72fB+xI1v4ZuPbz4ra20T99y8vLt/pAC4VC8fuKioro0qXLVj0e24G1zgl2MH4eQKvnxW3NpxgAgIxAAAAyAgEAyAgEACAjEACAjEAAADICAQDICAQAICMQAICMQAAAMgIBAMgIBAAgIxAAgIxAAAAyAgEAyAgEACAjEACAjEAAADICAQDICAQAICMQAICMQAAAMgIBAMgIBAAgIxAAgIxAAAAyAgEAyAgEACAjEACAjEAAADICAQDICAQAICMQAICMQAAAMgIBAMgIBAAgIxAAgIxAAAAyAgEAyAgEACAjEACAjEAAADICAQDICAQAICMQAICMQAAAMgIBAMgIBAAgIxAAgIxAAAAyAgEAyAgEACAjEACAjEAAADICAQDICAQAICMQAICMQAAAMgIBAMgIBAAgIxAAgIxAAAAyAgEAyAgEACAjEACAjEAAADICAQDICAQAICMQAICMQAAAMgIBAMgIBAAg06nUA1hbRUVFPPTQQ8XvAWBH016eC9tVIBQKhejSpUuphwEAJdNengu9xAAAZAQCAJARCABARiAAABmBAABkBAIAkBEIAEBGIAAAGYEAAGQEAgCQEQgAQEYgAAAZgQAAZAQCAJARCABARiAAABmBAABkBAIAkBEIAEBGIAAAGYEAAGQEAgCQEQgAQEYgAAAZgQAAZAQCAJARCABARiAAABmBAABkBAIA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trbVNo2NjWn48OGprKwsDRkyJF1//fXbfuDtxKbO34QJE9LQoUNTRUVF6tWrVzrooIPSAw88UJrBtwNtzV1EpEmTJhXXcQ6u3+bMn3PwA6eddloaPHhwKisrS3379k2jRo0qPrml5NzbkE2dv1Kde/7cMwCQ8R4EACAjEACAjEAAADICAQDICAQAICMQAICMQAAAMgIBKLr55ptj55133qRtxo4dG8cdd9xWGQ9QOgIBtlMTJ06M7t27R3Nzc3HZkiVLonPnznHwwQe3Wvexxx6LQqEQL7300ofu86tf/eoG19kcQ4YMiWuuueYj3y+w9QgE2E7V19fHkiVLYubMmcVljz32WFRWVsaMGTNi2bJlxeWNjY0xYMCAqK6u/tB9dunSJfr167fVxgxsPwQCbKdqampiwIAB0djYWFzW2NgYxx57bAwdOjSefPLJVsvr6+vjvffei/POOy8GDhwYXbt2jc997nOttm/rJYZLL700+vXrF927d4/TTz89zj///Nhvv/2y8VxxxRVRVVUVffr0iTPPPDNWrVoVERF1dXUxb968OOecc6JQKEShUPgopwHYSgQCbMfq6uqioaGheLuhoSHq6uqitra2uPy9996LpqamqK+vj29961vxxBNPxB133BGzZ8+Or3zlK3HEEUes9+/K33bbbXHZZZfFhAkT4g9/+EPsuuuucf3112frNTQ0xF/+8pdoaGiIW265JW6++ea4+eabIyJi8uTJscsuu8Qll1wS8+fPj/nz53/0EwF85AQCbMfq6uriiSeeiObm5li8eHHMmjUrDjnkkKitrS1eGZg+fXosX7486urq4vbbb48777wzDj744Bg6dGice+65cdBBB8WkSZPa3P9//ud/xre//e341re+FdXV1XHRRRfF3nvvna3Xq1evuPbaa2P33XePo48+Oo466qj43e9+FxERvXv3jo4dO0b37t2jsrIyKisrt9p8AB8dgQDbsfr6+li6dGnMmDEjHnvssaiuro5+/fpFbW1tzJgxI5YuXRqNjY2x6667xtNPPx0ppaiuro5u3boVv6ZNmxZ/+ctf2tz/nDlz4sADD2y1bN3bERF77rlndOzYsXi7qqoqFi5c+NE+WGCb6lTqAQCbb9iwYbHLLrtEQ0NDvP3221FbWxsREZWVlbHbbrvFE088EQ0NDXHooYfGmjVromPHjvGHP/yh1ZN5RES3bt3We4x13zPQ1l+I79y5c7bNmjVrNvdhAe2AKwiwnauvr4/GxsZobGyMurq64vLa2tr4zW9+E9OnT4/6+voYPnx4rF69OhYuXBjDhg1r9bW+y/41NTXx+9//vtWytT81sbHKyspi9erVm7wdUDoCAbZz9fX18fjjj8czzzxTvIIQ8X4g3HjjjbFixYqor6+P6urqOOWUU+LUU0+NyZMnx9y5c2PGjBkxYcKEePDBB9vc9/e+97246aab4pZbbok///nPcemll8bs2bM3+ZMIQ4YMiUcffTT+7//+L958880terzAtiEQYDtXX18fy5cvj2HDhkX//v2Ly2tra2Px4sUxdOjQGDRoUERETJo0KU499dT4wQ9+EDU1NfGlL30pnnrqqeL96zrllFPiggsuiHPPPTf233//mDt3bowdOzYqKio2aYyXXHJJvPLKKzF06NDo27fv5j9YYJsppLZeUARYjy9+8YtRWVkZP//5z0s9FGAr8iZFYL2WLVsWEydOjMMPPzw6duwYt99+e/z2t7+NRx55pNRDA7YyVxCA9Vq+fHkcc8wx8fTTT8fKlSujpqYm/vmf/zlOOOGEUg8N2MoEAgCQ8SZFACAjEACAjEAAADICAQDICAQAICMQAICMQAAAMgIBAMgIBAAg8/8AQER6F1Tc/w0AAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Outlier Clipping or Outlier capping\n",
    "df['Weight'] = np.where(df['Weight']>3.5,3.5,df['Weight'])\n",
    "sns.boxplot(x=df['Weight'])\n",
    "plt.title('Boxplot for Weight')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "57a474be",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8     613\n",
       "4     364\n",
       "16    198\n",
       "6      35\n",
       "12     25\n",
       "32     17\n",
       "2      16\n",
       "24      3\n",
       "64      1\n",
       "Name: Ram, dtype: int64"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Ram'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "ac4218c0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# df[df['Price']>150000].head(30)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "73ba1d8a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# df['SSD'].value_counts()"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "7b14d1f9",
   "metadata": {},
   "source": [
    "#### Select the dependent and independent features"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "7f6f003e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "<class 'pandas.core.series.Series'>\n",
      "(1272, 11)\n",
      "(1272,)\n"
     ]
    }
   ],
   "source": [
    "x = df.drop('Price',axis=1)\n",
    "y = df['Price']\n",
    "print(type(x))\n",
    "print(type(y))\n",
    "print(x.shape)\n",
    "print(y.shape)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "eab6672b",
   "metadata": {},
   "source": [
    "#### Split data into train and test "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "23c6cdb5",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "7f59496f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(954, 11)\n",
      "(318, 11)\n",
      "(954,)\n",
      "(318,)\n"
     ]
    }
   ],
   "source": [
    "x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25,random_state=42)\n",
    "print(x_train.shape)\n",
    "print(x_test.shape)\n",
    "print(y_train.shape)\n",
    "print(y_test.shape)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "ea2ac1e4",
   "metadata": {},
   "source": [
    "#### Creating Function to evaluate the performance of Regression Models"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "1c8e077a",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import mean_squared_error, mean_absolute_error,r2_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "id": "fa82e820",
   "metadata": {},
   "outputs": [],
   "source": [
    "def eval_model(ytest,ypred):\n",
    "    mae= mean_absolute_error(ytest,ypred)\n",
    "    mse = mean_squared_error(ytest,ypred)\n",
    "    rmse= np.sqrt(mse)\n",
    "    r2s = r2_score(ytest,ypred)\n",
    "    print(\"MAE\",mae)\n",
    "    print(\"MSE\",mse)\n",
    "    print(\"RMSE\",rmse)\n",
    "    print('R2_Score',r2s)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "e4a35a4a",
   "metadata": {},
   "source": [
    "### Import the ML models"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "ac35709a",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LinearRegression,Ridge,Lasso\n",
    "from sklearn.neighbors import KNeighborsRegressor\n",
    "from sklearn.tree import DecisionTreeRegressor\n",
    "from sklearn.ensemble import RandomForestRegressor"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "77e0a046",
   "metadata": {},
   "source": [
    "#### Import the sklearn libraries for Transformation - ColumnTransformer and Pipeline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "4864b908",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import OneHotEncoder\n",
    "from sklearn.compose import ColumnTransformer\n",
    "from sklearn.pipeline import Pipeline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "be92edf3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['Company', 'TypeName', 'Ram', 'Weight', 'Price', 'Touchscreen', 'Ips',\n",
      "       'Cpu brand', 'HDD', 'SSD', 'Gpu brand', 'os'],\n",
      "      dtype='object')\n",
      "Index(['Company', 'TypeName', 'Cpu brand', 'Gpu brand', 'os'], dtype='object')\n",
      "Index(['Company', 'TypeName', 'Ram', 'Weight', 'Touchscreen', 'Ips',\n",
      "       'Cpu brand', 'HDD', 'SSD', 'Gpu brand', 'os'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print(df.columns)\n",
    "print(cat_cols)  # [0,1,6,9,10]\n",
    "print(x_train.columns)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "61cba7a7",
   "metadata": {},
   "source": [
    "### 1) Linear Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "add9df41",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MAE 13940.9013091491\n",
      "MSE 409547387.3004308\n",
      "RMSE 20237.27717111249\n",
      "R2_Score 0.7020504611099125\n"
     ]
    }
   ],
   "source": [
    "step1 = ColumnTransformer(transformers=\n",
    "                          [('encoder',OneHotEncoder(drop='first',sparse=False),[0,1,6,9,10])],\n",
    "                         remainder='passthrough')\n",
    "step2 = LinearRegression()\n",
    "\n",
    "pipe_lr = Pipeline([('step1',step1),('step2',step2)])\n",
    "\n",
    "pipe_lr.fit(x_train,y_train)\n",
    "ypred_lr = pipe_lr.predict(x_test)\n",
    "eval_model(y_test,ypred_lr)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "edcaa59f",
   "metadata": {},
   "source": [
    "### 2) Ridge Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "fdb5efd2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MAE 13548.579736823453\n",
      "MSE 382774580.2996107\n",
      "RMSE 19564.625738807546\n",
      "R2_Score 0.7215279275717752\n"
     ]
    }
   ],
   "source": [
    "step1 = ColumnTransformer(transformers=\n",
    "                          [('encoder',OneHotEncoder(drop='first',sparse=False),[0,1,6,9,10])],\n",
    "                         remainder='passthrough')\n",
    "step2 = Ridge(alpha=4)\n",
    "\n",
    "pipe_rid = Pipeline([('step1',step1),('step2',step2)])\n",
    "\n",
    "pipe_rid.fit(x_train,y_train)\n",
    "ypred_rid = pipe_rid.predict(x_test)\n",
    "eval_model(y_test,ypred_rid)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "145735a3",
   "metadata": {},
   "source": [
    "### 3) Lasso Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "e5510ce6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MAE 13816.198359975677\n",
      "MSE 403232690.0685322\n",
      "RMSE 20080.65462251\n",
      "R2_Score 0.7066444621628224\n"
     ]
    }
   ],
   "source": [
    "step1 = ColumnTransformer(transformers=\n",
    "                          [('encoder',OneHotEncoder(drop='first',sparse=False),[0,1,6,9,10])],\n",
    "                         remainder='passthrough')\n",
    "step2 = Lasso(alpha=7)\n",
    "\n",
    "pipe_las = Pipeline([('step1',step1),('step2',step2)])\n",
    "\n",
    "pipe_las.fit(x_train,y_train)\n",
    "ypred_las = pipe_las.predict(x_test)\n",
    "eval_model(y_test,ypred_las)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "d2eac348",
   "metadata": {},
   "source": [
    "### 4) KNN Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "175043cb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MAE 13686.943381132074\n",
      "MSE 456737320.7553621\n",
      "RMSE 21371.41363493211\n",
      "R2_Score 0.6677193449823505\n"
     ]
    }
   ],
   "source": [
    "step1 = ColumnTransformer(transformers=\n",
    "                          [('encoder',OneHotEncoder(drop='first',sparse=False),[0,1,6,9,10])],\n",
    "                         remainder='passthrough')\n",
    "step2 = KNeighborsRegressor(n_neighbors=7)\n",
    "\n",
    "pipe_knn = Pipeline([('step1',step1),('step2',step2)])\n",
    "\n",
    "pipe_knn.fit(x_train,y_train)\n",
    "ypred_knn = pipe_knn.predict(x_test)\n",
    "eval_model(y_test,ypred_knn)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "d4745a9d",
   "metadata": {},
   "source": [
    "### 5) DT Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "9cd68ab8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MAE 11943.347423514673\n",
      "MSE 365393747.4887078\n",
      "RMSE 19115.275239679595\n",
      "R2_Score 0.7341726453312255\n"
     ]
    }
   ],
   "source": [
    "step1 = ColumnTransformer(transformers=\n",
    "                          [('encoder',OneHotEncoder(drop='first',sparse=False),[0,1,6,9,10])],\n",
    "                         remainder='passthrough')\n",
    "step2 = DecisionTreeRegressor(criterion='squared_error',max_depth=10,min_samples_split=15)\n",
    "\n",
    "pipe_dt = Pipeline([('step1',step1),('step2',step2)])\n",
    "\n",
    "pipe_dt.fit(x_train,y_train)\n",
    "ypred_dt = pipe_dt.predict(x_test)\n",
    "eval_model(y_test,ypred_dt)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "aa573a16",
   "metadata": {},
   "source": [
    "### 6) RF Regression"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "95852849",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MAE 11206.821979521825\n",
      "MSE 301252544.8152472\n",
      "RMSE 17356.628267473126\n",
      "R2_Score 0.780835967703721\n"
     ]
    }
   ],
   "source": [
    "step1 = ColumnTransformer(transformers=\n",
    "                          [('encoder',OneHotEncoder(drop='first',sparse=False),[0,1,6,9,10])],\n",
    "                         remainder='passthrough')\n",
    "step2 = RandomForestRegressor(n_estimators=100,criterion='squared_error',\n",
    "                              max_depth=10,min_samples_split=15,random_state=5)\n",
    "\n",
    "pipe_rf = Pipeline([('step1',step1),('step2',step2)])\n",
    "\n",
    "pipe_rf.fit(x_train,y_train)\n",
    "ypred_rf = pipe_rf.predict(x_test)\n",
    "eval_model(y_test,ypred_rf)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "6b9ceb31",
   "metadata": {},
   "source": [
    "### Inference\n",
    "1) RF Reg is the best model in terms of R2_Score and RMSE."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "id": "2972c0c1",
   "metadata": {},
   "source": [
    "### Save the model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "id": "73a5f8ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pickle"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "295a2d82",
   "metadata": {},
   "outputs": [],
   "source": [
    "pickle.dump(pipe_rf,open('rf.pkl','wb'))  # wb= write binary\n",
    "pickle.dump(df,open('df.pkl','wb'))  # wb= write binary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "8084cb62",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['Company', 'TypeName', 'Ram', 'Weight', 'Price', 'Touchscreen', 'Ips',\n",
       "       'Cpu brand', 'HDD', 'SSD', 'Gpu brand', 'os'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 83,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "id": "77110abf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 8, 16,  4,  2, 12,  6, 32, 24, 64], dtype=int64)"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Ram'].unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "id": "c49358a0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    1085\n",
       "1     187\n",
       "Name: Touchscreen, dtype: int64"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Touchscreen'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "7fae54fa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    916\n",
       "1    356\n",
       "Name: Ips, dtype: int64"
      ]
     },
     "execution_count": 87,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Ips'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "a8cb61c8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[   0  500 1000 2000   32  128]\n",
      "[ 128    0  256  512   32   64 1000 1024   16  768  180  240    8]\n"
     ]
    }
   ],
   "source": [
    "print(df['HDD'].unique())\n",
    "print(df['SSD'].unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e939653a",
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
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
