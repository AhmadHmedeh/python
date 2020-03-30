{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "script.py",
      "provenance": [],
      "authorship_tag": "ABX9TyNYRkTrMbk5R951vdoKvVi9",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "<a href=\"https://colab.research.google.com/github/AhmadHmedeh/python/blob/master/script.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jBx2sv40NaMR",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 252
        },
        "outputId": "6e106265-2ff7-4c97-9eb7-6afa0a5419a2"
      },
      "source": [
        "none = None # singleton null object\n",
        "boolean = bool(True)\n",
        "integer = 1\n",
        "Long = 3.14\n",
        "\n",
        "# float\n",
        "Float = 3.14\n",
        "Float_inf = float('inf')\n",
        "Float_nan = float('nan')\n",
        "\n",
        "# complex object type, note the usage of letter j\n",
        "Complex = 2+8j \n",
        "\n",
        "# string can be enclosed in single or double quote\n",
        "string = 'this is a string'\n",
        "me_also_string = \"also me\"\n",
        "\n",
        "List = [1, True, 'ML'] # Values can be changed\n",
        "\n",
        "Tuple = (1, True, 'ML') # Values can not be changed\n",
        "\n",
        "Set = set([1,2,2,2,3,4,5,5]) # Duplicates will not be stored\n",
        "\n",
        "# Use a dictionary when you have a set of unique keys that map to values\n",
        "Dictionary = {'a':'A', 2:'AA', True:1, False:0}\n",
        "\n",
        "# lets print the object type and the value\n",
        "print(type(none), none)\n",
        "print(type(boolean), boolean)\n",
        "print(type(integer), integer)\n",
        "print(type(Long), Long)\n",
        "print(type(Float), Float)\n",
        "print(type(Float_inf), Float_inf)\n",
        "print(type(Float_nan), Float_nan)\n",
        "print(type(Complex), Complex)\n",
        "print(type(string), string)\n",
        "print(type(me_also_string), me_also_string)\n",
        "print(type(Tuple), Tuple)\n",
        "print(type(List), List)\n",
        "print(type(Set), Set)\n",
        "print(type(Dictionary), Dictionary)"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "<class 'NoneType'> None\n",
            "<class 'bool'> True\n",
            "<class 'int'> 1\n",
            "<class 'float'> 3.14\n",
            "<class 'float'> 3.14\n",
            "<class 'float'> inf\n",
            "<class 'float'> nan\n",
            "<class 'complex'> (2+8j)\n",
            "<class 'str'> this is a string\n",
            "<class 'str'> also me\n",
            "<class 'tuple'> (1, True, 'ML')\n",
            "<class 'list'> [1, True, 'ML']\n",
            "<class 'set'> {1, 2, 3, 4, 5}\n",
            "<class 'dict'> {'a': 'A', 2: 'AA', True: 1, False: 0}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hVX1NwjJN1_6",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "b12fb0cc-9a45-48fc-864c-1188f369093a"
      },
      "source": [
        "# incorrect indentation, program will generate a syntax error\n",
        "# due to the wrong indentation in the else statement\n",
        "x = 1\n",
        "if x == 1:\n",
        "    print ('x has a value of 1')\n",
        "else:\n",
        " print ('x does NOT have a value of 1')"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "x has a value of 1\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "KA9BXe0vOJ2j",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 128
        },
        "outputId": "aeb2e26c-5aa7-44c7-ce4a-28c1d9db1e7b"
      },
      "source": [
        "# incorrect indentation, program will generate a syntax error \n",
        "# due to the space character inserted at the beginning of second line\n",
        "print (\"Programming is an important skill for Data Science\")\n",
        " print (\"Statistics is an important skill for Data Science\")\n",
        "print (\"Business domain knowledge is a important skill for Data Science\")"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "error",
          "ename": "IndentationError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-3-d7a0a093f887>\"\u001b[0;36m, line \u001b[0;32m2\u001b[0m\n\u001b[0;31m    print (\"Statistics is an important skill for Data Science\")\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m unexpected indent\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Az383UzJODn_",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 101
        },
        "outputId": "fee51146-5064-44e8-a040-3ecc6f19d4c4"
      },
      "source": [
        "# Correct indentation\n",
        "print (\"Programming is an important skill for Data Science\")\n",
        "print (\"Statistics is an imporant skill for Data Science\")\n",
        "print (\"Business domain knowledge is a important skill for Data Science\")\n",
        "\n",
        "# Correct indentation, note that if statement here is an example of suites\n",
        "x = 1\n",
        "if x == 1:\n",
        "    print ('x has a value of 1')\n",
        "else:\n",
        "    print ('x does NOT have a value of 1')"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Programming is an important skill for Data Science\n",
            "Statistics is an imporant skill for Data Science\n",
            "Business domain knowledge is a important skill for Data Science\n",
            "x has a value of 1\n",
            "ERROR! Session/line number was not unique in database. History logging moved to new session 59\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-sau5AVDOY6q",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 84
        },
        "outputId": "56fa4d01-2e4c-4c90-d35b-f8e069aacd3c"
      },
      "source": [
        "# Example of implicit line continuation\n",
        "x = ('1' + '2' + \n",
        "    '3' + '4')\n",
        "\n",
        "# Example of explicit line continuation\n",
        "y = '1' + '2' + \\\n",
        "    '11' + '12'\n",
        "    \n",
        "weekdays = ['Monday', 'Tuesday', 'Wednesday', \n",
        "            'Thursday', 'Friday']\n",
        "\n",
        "weekend = {'Saturday',\n",
        "           'Sunday'}\n",
        "\n",
        "print ('x has a value of', x)\n",
        "print ('y has a value of', y)\n",
        "print (weekdays)\n",
        "print (weekend)"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "x has a value of 1234\n",
            "y has a value of 121112\n",
            "['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']\n",
            "{'Sunday', 'Saturday'}\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Bz3O_sDmOls-",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 134
        },
        "outputId": "8345eeb4-c2bc-4593-d502-e432b0312b7d"
      },
      "source": [
        "# Variable x holds 10 and variable y holds 5\n",
        "x = 10\n",
        "y = 5\n",
        "\n",
        "# Addition\n",
        "print (\"Addition, x(10) + y(5) = \", x + y)\n",
        "\n",
        "# Subtraction\n",
        "print (\"Subtraction, x(10) - y(5) = \", x - y)\n",
        "\n",
        "# Multiplication\n",
        "print (\"Multiplication, x(10) * y(5) = \", x * y) \n",
        "\n",
        "# Division\n",
        "print (\"Division, x(10) / y(5) = \", x / y)\n",
        "\n",
        "# Modulus\n",
        "print (\"Modulus, x(10) % y(5) = \", x % y)\n",
        "\n",
        "# Exponent\n",
        "print (\"Exponent, x(10)**y(5) = \", x**y)\n",
        "\n",
        "# Integer division rounded towards minus infinity\n",
        "print (\"Floor Division, x(10)//y(5) = \", x//y)"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Addition, x(10) + y(5) =  15\n",
            "Subtraction, x(10) - y(5) =  5\n",
            "Multiplication, x(10) * y(5) =  50\n",
            "Division, x(10) / y(5) =  2.0\n",
            "Modulus, x(10) % y(5) =  0\n",
            "Exponent, x(10)**y(5) =  100000\n",
            "Floor Division, x(10)//y(5) =  2\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6s0kFs_rOvR_",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 118
        },
        "outputId": "a6ab76f8-44c5-4734-de16-1034769f4602"
      },
      "source": [
        "# Variable x holds 10 and variable b holds 5\n",
        "# Equal check operation\n",
        "print (\"Equal check, x(10) == y(5) \", x == y)\n",
        "\n",
        "# Not Equal check operation\n",
        "print (\"Not Equal check, x(10) != y(5) \", x != y)\n",
        "\n",
        "# Less than check operation\n",
        "print (\"Less than check, x(10) < y(5) \", x < y)\n",
        "\n",
        "# Greater check operation\n",
        "print (\"Greater than check, x(10) > y(5) \", x > y)\n",
        "\n",
        "# Less than or equal check operation\n",
        "print (\"Less than or equal to check, x(10) <= y(5) \", x <= y)\n",
        "\n",
        "# Greater than or equal to check operation\n",
        "print (\"Greater than or equal to check, x(10) >= y(5) \", x >= y)"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Equal check, x(10) == y(5)  False\n",
            "Not Equal check, x(10) != y(5)  True\n",
            "Less than check, x(10) < y(5)  False\n",
            "Greater than check, x(10) > y(5)  True\n",
            "Less than or equal to check, x(10) <= y(5)  False\n",
            "Greater than or equal to check, x(10) >= y(5)  True\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MUOGJjDIO4SD",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 118
        },
        "outputId": "244cfe32-8666-4c25-af69-ed249cfd01d9"
      },
      "source": [
        "# Variable x holds 10 and variable y holds 5\n",
        "x = 5\n",
        "y = 10\n",
        "\n",
        "x += y\n",
        "print (\"Value of a post x+=y is \", x)\n",
        "\n",
        "x *= y\n",
        "print (\"Value of a post x*=y is \", x) \n",
        "\n",
        "x /= y \n",
        "print (\"Value of a post x/=y is \", x)\n",
        "\n",
        "x %= y\n",
        "print (\"Value of a post x%=y is \", x)\n",
        "\n",
        "x **= y\n",
        "print (\"Value of x post x**=y is \", x)\n",
        "\n",
        "x //= y\n",
        "print (\"Value of a post x//=y is \", x)"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Value of a post x+=y is  15\n",
            "Value of a post x*=y is  150\n",
            "Value of a post x/=y is  15.0\n",
            "Value of a post x%=y is  5.0\n",
            "Value of x post x**=y is  9765625.0\n",
            "Value of a post x//=y is  976562.0\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7jv1oWWxPEWe",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 118
        },
        "outputId": "ff430035-af82-4deb-df80-69363c501471"
      },
      "source": [
        "# Basic six bitwise operations\n",
        "# Let x = 10 (0000 1010 in binary) and y = 4 (0000 0100 in binary)\n",
        "x = 10\n",
        "y = 4\n",
        "\n",
        "print (x >> y)  # Right Shift\n",
        "print (x << y)  # Left Shift\n",
        "print (x & y)   # Bitwise AND\n",
        "print (x | y)   # Bitwise OR\n",
        "print (x ^ y) # Bitwise XOR\n",
        "print (~x)    # Bitwise NOT"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "0\n",
            "160\n",
            "0\n",
            "14\n",
            "14\n",
            "-11\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yoHM_W2dPNg2",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 67
        },
        "outputId": "853c3e63-10c2-42f3-b7fd-e3bf9175707c"
      },
      "source": [
        "var1 = True\n",
        "var2 = False\n",
        "print('var1 and var2 is',var1 and var2)\n",
        "print('var1 or var2 is',var1 or var2)\n",
        "print('not var1 is',not var1)"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "var1 and var2 is False\n",
            "var1 or var2 is True\n",
            "not var1 is False\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8b9fh6-vPSC8",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 84
        },
        "outputId": "578168e8-07e0-4671-a20e-e62976f7c40c"
      },
      "source": [
        "var1 = 'Hello world'          # string\n",
        "var2 = {1:'a',2:'b'}          # dictionary\n",
        "print('H' in var1)\n",
        "print('hello' not in var1)\n",
        "print(1 in var2)\n",
        "print('a' in var2)"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "True\n",
            "True\n",
            "True\n",
            "False\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FdIkjmQZPfG_",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 67
        },
        "outputId": "b59c511f-de2a-44b4-c30d-8382e901a194"
      },
      "source": [
        "var1 = 5\n",
        "var1 = 5\n",
        "var2 = 'Hello'\n",
        "var2 = 'Hello'\n",
        "var3 = [1,2,3]\n",
        "var3 = [1,2,3]\n",
        "print(var1 is not var1)\n",
        "print(var2 is var2)\n",
        "print(var3 is var3)"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "False\n",
            "True\n",
            "True\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gQnPZsCgPwG9",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 67
        },
        "outputId": "8b2683f1-b933-45ef-bd58-ab10dff31d8b"
      },
      "source": [
        "var = -1\n",
        "if var < 0:\n",
        "    print (var)\n",
        "    print (\"the value of var is negative\")\n",
        "    \n",
        "# If the suite of an if clause consists only of a single line, it may go on the same line as the header statement\n",
        "if ( var  == -1 ) : print (\"the value of var is negative\")"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "-1\n",
            "the value of var is negative\n",
            "the value of var is negative\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "B1xFy648P_3n",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "3e3c5faa-4af4-4bf6-c8e3-3bea1397c56a"
      },
      "source": [
        "var = 1\n",
        "\n",
        "if var < 0:\n",
        "    print (\"the value of var is negative\")\n",
        "    print (var)\n",
        "else:\n",
        "    print (\"the value of var is positive\")\n",
        "    print (var)"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "the value of var is positive\n",
            "1\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eiP-P-mnQCM6",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "98d69dce-8fee-4566-8ec7-e8b879eda071"
      },
      "source": [
        "score = 95\n",
        "\n",
        "if score >= 99:\n",
        "    print('A')\n",
        "elif score >=75:\n",
        "    print('B')\n",
        "elif score >= 60:\n",
        "    print('C')\n",
        "elif score >= 35:\n",
        "    print('D')\n",
        "else:\n",
        "    print('F')"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "B\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CMYmn_Z6QG9c",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 370
        },
        "outputId": "0ffab6ab-251a-4374-941d-cd2298682c9f"
      },
      "source": [
        "# First Example\n",
        "print (\"First Example\")\n",
        "for item in [1,2,3,4,5]:    \n",
        "    print ('item :', item)\n",
        "\n",
        "# Second Example    \n",
        "print (\"Second Example\")\n",
        "letters = ['A', 'B', 'C']\n",
        "for letter in letters:        \n",
        "    print ('First loop letter :', letter)\n",
        "\n",
        "# Third Example - Iterating by sequency index\n",
        "print (\"Third Example\")\n",
        "for index in range(len(letters)):\n",
        "    print ('First loop letter :', letters[index])\n",
        "\n",
        "# Fourth Example - Using else statement\n",
        "print (\"Fourth Example\")\n",
        "for item in [1,2,3,4,5]:    \n",
        "    print ('item :', item)    \n",
        "else:\n",
        "    print ('looping over item complete!')"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "First Example\n",
            "item : 1\n",
            "item : 2\n",
            "item : 3\n",
            "item : 4\n",
            "item : 5\n",
            "Second Example\n",
            "First loop letter : A\n",
            "First loop letter : B\n",
            "First loop letter : C\n",
            "Third Example\n",
            "First loop letter : A\n",
            "First loop letter : B\n",
            "First loop letter : C\n",
            "Fourth Example\n",
            "item : 1\n",
            "item : 2\n",
            "item : 3\n",
            "item : 4\n",
            "item : 5\n",
            "looping over item complete!\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "FtiqhhW9Qg8L",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 101
        },
        "outputId": "704b4ecd-fb5c-45ef-edc5-5161c6fae585"
      },
      "source": [
        "count = 0\n",
        "while (count < 5):\n",
        "    print ('The count is:', count)\n",
        "    count = count + 1"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "The count is: 0\n",
            "The count is: 1\n",
            "The count is: 2\n",
            "The count is: 3\n",
            "The count is: 4\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "pOoueazVQodV",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 118
        },
        "outputId": "320f6589-473e-4831-e441-a469c7f265cc"
      },
      "source": [
        "count = 0\n",
        "while count < 5:\n",
        "    print (count, \" is  less than 5\")\n",
        "    count = count + 1\n",
        "else:\n",
        "    print (count, \" is not less than 5\")"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "0  is  less than 5\n",
            "1  is  less than 5\n",
            "2  is  less than 5\n",
            "3  is  less than 5\n",
            "4  is  less than 5\n",
            "5  is not less than 5\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "RxNtfkENQwNP",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "b476f3e1-1bd2-4c65-da9d-578c5512db84"
      },
      "source": [
        "# simple function to add two numbers\n",
        "def sum_two_numbers(a, b):\n",
        "    return a + b\n",
        "\n",
        "# after this line x will hold the value 3!\n",
        "x = sum_two_numbers(1,2)\n",
        "print (x)"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "3\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "enCEV7O1Q2jW",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "09a696c4-7b39-40e3-eb1c-9dd6858c2780"
      },
      "source": [
        "def sum_two_numbers(a, b = 10):\n",
        "    return a + b\n",
        "\n",
        "print (sum_two_numbers(10))\n",
        "print (sum_two_numbers(10, 5))"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "20\n",
            "15\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "1_0CwbsDQ5BZ",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 67
        },
        "outputId": "21571124-8c97-42d1-8105-b916a5219a3e"
      },
      "source": [
        "def foo(*args):\n",
        "    for a in args:\n",
        "        print (a)\n",
        "\n",
        "foo(1,2,3)  "
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "1\n",
            "2\n",
            "3\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "J08sLQxPRDC4",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 50
        },
        "outputId": "34f0ea86-199b-4954-b521-028b67c13acb"
      },
      "source": [
        "def bar(**kwargs):\n",
        "    for a in kwargs:\n",
        "        print (a, kwargs[a])\n",
        "        \n",
        "bar(name='one', age=27)"
      ],
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "name one\n",
            "age 27\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4me0vgPJRZYH",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 54
        },
        "outputId": "6df52691-5b4a-4d3e-b525-472b0825dfdd"
      },
      "source": [
        "import os\n",
        "\n",
        "content = dir(os)\n",
        "\n",
        "print (content)"
      ],
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "['CLD_CONTINUED', 'CLD_DUMPED', 'CLD_EXITED', 'CLD_TRAPPED', 'DirEntry', 'EX_CANTCREAT', 'EX_CONFIG', 'EX_DATAERR', 'EX_IOERR', 'EX_NOHOST', 'EX_NOINPUT', 'EX_NOPERM', 'EX_NOUSER', 'EX_OK', 'EX_OSERR', 'EX_OSFILE', 'EX_PROTOCOL', 'EX_SOFTWARE', 'EX_TEMPFAIL', 'EX_UNAVAILABLE', 'EX_USAGE', 'F_LOCK', 'F_OK', 'F_TEST', 'F_TLOCK', 'F_ULOCK', 'GRND_NONBLOCK', 'GRND_RANDOM', 'MutableMapping', 'NGROUPS_MAX', 'O_ACCMODE', 'O_APPEND', 'O_ASYNC', 'O_CLOEXEC', 'O_CREAT', 'O_DIRECT', 'O_DIRECTORY', 'O_DSYNC', 'O_EXCL', 'O_LARGEFILE', 'O_NDELAY', 'O_NOATIME', 'O_NOCTTY', 'O_NOFOLLOW', 'O_NONBLOCK', 'O_PATH', 'O_RDONLY', 'O_RDWR', 'O_RSYNC', 'O_SYNC', 'O_TMPFILE', 'O_TRUNC', 'O_WRONLY', 'POSIX_FADV_DONTNEED', 'POSIX_FADV_NOREUSE', 'POSIX_FADV_NORMAL', 'POSIX_FADV_RANDOM', 'POSIX_FADV_SEQUENTIAL', 'POSIX_FADV_WILLNEED', 'PRIO_PGRP', 'PRIO_PROCESS', 'PRIO_USER', 'P_ALL', 'P_NOWAIT', 'P_NOWAITO', 'P_PGID', 'P_PID', 'P_WAIT', 'PathLike', 'RTLD_DEEPBIND', 'RTLD_GLOBAL', 'RTLD_LAZY', 'RTLD_LOCAL', 'RTLD_NODELETE', 'RTLD_NOLOAD', 'RTLD_NOW', 'R_OK', 'SCHED_BATCH', 'SCHED_FIFO', 'SCHED_IDLE', 'SCHED_OTHER', 'SCHED_RESET_ON_FORK', 'SCHED_RR', 'SEEK_CUR', 'SEEK_DATA', 'SEEK_END', 'SEEK_HOLE', 'SEEK_SET', 'ST_APPEND', 'ST_MANDLOCK', 'ST_NOATIME', 'ST_NODEV', 'ST_NODIRATIME', 'ST_NOEXEC', 'ST_NOSUID', 'ST_RDONLY', 'ST_RELATIME', 'ST_SYNCHRONOUS', 'ST_WRITE', 'TMP_MAX', 'WCONTINUED', 'WCOREDUMP', 'WEXITED', 'WEXITSTATUS', 'WIFCONTINUED', 'WIFEXITED', 'WIFSIGNALED', 'WIFSTOPPED', 'WNOHANG', 'WNOWAIT', 'WSTOPPED', 'WSTOPSIG', 'WTERMSIG', 'WUNTRACED', 'W_OK', 'XATTR_CREATE', 'XATTR_REPLACE', 'XATTR_SIZE_MAX', 'X_OK', '_Environ', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_execvpe', '_exists', '_exit', '_fspath', '_fwalk', '_get_exports_list', '_putenv', '_spawnvef', '_unsetenv', '_wrap_close', 'abc', 'abort', 'access', 'altsep', 'chdir', 'chmod', 'chown', 'chroot', 'close', 'closerange', 'confstr', 'confstr_names', 'cpu_count', 'ctermid', 'curdir', 'defpath', 'device_encoding', 'devnull', 'dup', 'dup2', 'environ', 'environb', 'errno', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fchdir', 'fchmod', 'fchown', 'fdatasync', 'fdopen', 'fork', 'forkpty', 'fpathconf', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fstatvfs', 'fsync', 'ftruncate', 'fwalk', 'get_blocking', 'get_exec_path', 'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getegid', 'getenv', 'getenvb', 'geteuid', 'getgid', 'getgrouplist', 'getgroups', 'getloadavg', 'getlogin', 'getpgid', 'getpgrp', 'getpid', 'getppid', 'getpriority', 'getrandom', 'getresgid', 'getresuid', 'getsid', 'getuid', 'getxattr', 'initgroups', 'isatty', 'kill', 'killpg', 'lchown', 'linesep', 'link', 'listdir', 'listxattr', 'lockf', 'lseek', 'lstat', 'major', 'makedev', 'makedirs', 'minor', 'mkdir', 'mkfifo', 'mknod', 'name', 'nice', 'open', 'openpty', 'pardir', 'path', 'pathconf', 'pathconf_names', 'pathsep', 'pipe', 'pipe2', 'popen', 'posix_fadvise', 'posix_fallocate', 'pread', 'putenv', 'pwrite', 'read', 'readlink', 'readv', 'remove', 'removedirs', 'removexattr', 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sched_get_priority_max', 'sched_get_priority_min', 'sched_getaffinity', 'sched_getparam', 'sched_getscheduler', 'sched_param', 'sched_rr_get_interval', 'sched_setaffinity', 'sched_setparam', 'sched_setscheduler', 'sched_yield', 'sendfile', 'sep', 'set_blocking', 'set_inheritable', 'setegid', 'seteuid', 'setgid', 'setgroups', 'setpgid', 'setpgrp', 'setpriority', 'setregid', 'setresgid', 'setresuid', 'setreuid', 'setsid', 'setuid', 'setxattr', 'spawnl', 'spawnle', 'spawnlp', 'spawnlpe', 'spawnv', 'spawnve', 'spawnvp', 'spawnvpe', 'st', 'stat', 'stat_float_times', 'stat_result', 'statvfs', 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sync', 'sys', 'sysconf', 'sysconf_names', 'system', 'tcgetpgrp', 'tcsetpgrp', 'terminal_size', 'times', 'times_result', 'truncate', 'ttyname', 'umask', 'uname', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'wait', 'wait3', 'wait4', 'waitid', 'waitid_result', 'waitpid', 'walk', 'write', 'writev']\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}