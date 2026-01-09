# 1. Use a lightweight Python Linux image (The Base)
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the Requirements file
COPY requirements.txt .

# 4. Install dependencies
# --no-cache-dir keeps the container small
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your code
COPY . .

# 6. Define the command to run when the container starts
CMD ["python", "main.py"]