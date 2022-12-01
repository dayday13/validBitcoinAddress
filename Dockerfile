# For more information, please refer to https://aka.ms/vscode-docker-python
FROM nginx:1.10.1-alpine

COPY telegram /usr/share/nginx/telegram

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt


# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["nginx", "-g", "daemon off;"]
