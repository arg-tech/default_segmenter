#FROM python:3.7.2
FROM python:3.8.2


RUN pip install --upgrade pip
RUN pip3 install tqdm
RUN pip3 install Cython


COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5005
CMD python ./main.py