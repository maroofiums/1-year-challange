# Day 272

---

## ⚙️ Step 1: AWS Account Setup

1. Go to **[aws.amazon.com](https://aws.amazon.com)** → **Sign Up** or **Sign In**.
2. Add your **credit/debit card** (AWS free tier gives 750 hours/month EC2 + 5GB S3 free).
3. Verify your **identity (OTP)** and choose **Free Tier plan**.

---

## 🖥️ Step 2: Launch an EC2 Instance

This is basically your cloud server — a virtual Linux machine.

### 🔹 Step-by-step

1. Go to **EC2 Dashboard** → “**Launch Instance**”.
2. **Name:** `my-fastapi-server` (or whatever project you’re deploying)
3. **AMI (OS):** Select **Ubuntu 22.04 LTS**.
4. **Instance Type:** `t2.micro` (free-tier eligible).
5. **Key Pair:** Create new → Download `.pem` file → store it safe.
6. **Network settings:**

   * Allow **HTTP (80)**, **HTTPS (443)**, and **SSH (22)**.
7. **Storage:** 8GB default is fine for now.
8. **Launch Instance.**

---

## 💻 Step 3: Connect to EC2

Open your terminal (or VS Code terminal):

```bash
cd Downloads
chmod 400 my-key.pem
ssh -i "my-key.pem" ubuntu@<YOUR_PUBLIC_IP>
```

If you see something like:

```
ubuntu@ip-172-31-xx-xx:~$
```

Boom 💥 you’re in your remote Linux server.

---

## ⚒️ Step 4: Basic Environment Setup

Inside EC2 terminal, run these:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git nginx -y
```

(Optional) For virtualenv:

```bash
sudo apt install python3-venv -y
```

Then create a directory for your app:

```bash
mkdir ~/myapp && cd ~/myapp
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn
```

---

## ☁️ Step 5: AWS S3 Setup

You’ll use S3 for static files, ML models, images, or data storage.

### 🔹 Create an S3 Bucket

1. Go to **S3 Dashboard** → “**Create bucket**”.
2. **Bucket name:** `my-fastapi-files`
3. **Region:** Same as EC2 region.
4. **Uncheck** “Block all public access” (if you want public file access).
5. Leave everything else default → Create bucket.

---

### 🔹 Configure IAM for Access

You’ll need credentials to access S3 from EC2 or your app.

1. Go to **IAM → Users → Add user**.
2. Name: `ec2-s3-access`
3. Permissions → Attach policy: `AmazonS3FullAccess`
4. Create user → Download **Access Key + Secret Key**.

---

### 🔹 Install and Configure AWS CLI on EC2

```bash
sudo apt install awscli -y
aws configure
```

Then enter:

```
AWS Access Key ID [None]: YOUR_KEY
AWS Secret Access Key [None]: YOUR_SECRET
Default region name [None]: ap-south-1 (or your region)
Default output format [None]: json
```

Now test:

```bash
aws s3 ls
```

You should see your bucket listed ✅

---

## 🌍 Step 6: Deploy Your App

For FastAPI:

1. Install Gunicorn and Uvicorn workers:

   ```bash
   pip install gunicorn uvicorn
   ```
2. Test run:

   ```bash
   gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000
   ```
3. Edit Nginx config to route traffic:

   ```bash
   sudo nano /etc/nginx/sites-available/fastapi
   ```

   Add:

   ```
   server {
       listen 80;
       server_name <YOUR_PUBLIC_IP>;

       location / {
           proxy_pass http://127.0.0.1:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

   Then run:

   ```bash
   sudo ln -s /etc/nginx/sites-available/fastapi /etc/nginx/sites-enabled
   sudo systemctl restart nginx
   ```

Now your app is live on your EC2 public IP 🚀

---

## 🧠 Optional but Important

* Use **`.env`** files for AWS keys, don’t hardcode.
* Set up **CloudWatch** for logs.
* Add **Route53** if you want a domain.
* Set up **SSL (HTTPS)** using **Certbot**:

  ```bash
  sudo apt install certbot python3-certbot-nginx -y
  sudo certbot --nginx
  ```

---
