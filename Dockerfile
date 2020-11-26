FROM python:3.6.10-alpine3.10

RUN pip3 install pygithub==1.47

COPY check_pr_comments.py /check_pr_comments.py

RUN chmod +x /check_pr_comments.py

ENTRYPOINT ["/check_OCA.py"]