# Cluster and Cloud Computing 2023
# Assignment 2
# Team 46

# Kunal Patel : 1291822
# Mayank Yadav : 1403092
# Harsh Mangla : 1418017
# Sophie von Doussa : 1064884
# Maxson Stephen Mathew : 1428525

# City : Melbourne

FROM python:latest

WORKDIR /workdirectory

COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

RUN python3 -m spacy download en_core_web_sm

COPY . .






