FROM python
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5010
CMD python ./caller.py
