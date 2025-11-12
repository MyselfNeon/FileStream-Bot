# ------- Base Image -------
FROM python:3.11

# ------- Working Directory -------
WORKDIR /app

# ------- Copy Project Files -------
COPY . /app

# ------- Install Dependencies -------
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# ------- Start Command -------
CMD ["python", "-m", "FileStream"]


# MyselfNeon
# Don't Remove Credit 🥺
# Telegram Channel @NeonFiles
