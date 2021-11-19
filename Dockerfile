FROM python:3.8-slim
RUN apt update
RUN apt install -y \
    wget \
    unzip
WORKDIR /root/
COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt
COPY ./flask-autodoc-init.py /usr/local/lib/python3.8/site-packages/flask_autodoc/__init__.py

RUN chmod 755 startup.sh
CMD ["sh", "startup.sh"]
