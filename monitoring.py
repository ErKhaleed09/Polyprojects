{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "cf98c785-1cc5-4650-8d63-55a039b9cf38",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--- UBUNTU SERVER HEALTH REPORT ---\n",
      "Free Disk Space: 17.93 GB\n",
      "RAM Utilization: 57.2%\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import shutil\n",
    "import psutil  # You may need to run 'pip install psutil' in your terminal first\n",
    "\n",
    "def check_system_health():\n",
    "    # 1. Check Disk Space\n",
    "    total, used, free = shutil.disk_usage(\"/\")\n",
    "    free_gb = free / (2**30) # Convert bytes to GB\n",
    "    \n",
    "    # 2. Check RAM usage\n",
    "    ram_usage = psutil.virtual_memory().percent\n",
    "    \n",
    "    # 3. Output results\n",
    "    print(\"--- UBUNTU SERVER HEALTH REPORT ---\")\n",
    "    print(f\"Free Disk Space: {free_gb:.2f} GB\")\n",
    "    print(f\"RAM Utilization: {ram_usage}%\")\n",
    "    \n",
    "    # 4. Basic Alert Logic (Just like a Cloud Monitor)\n",
    "    if ram_usage > 80:\n",
    "        print(\"⚠️ ALERT: High RAM usage detected!\")\n",
    "    if free_gb < 10:\n",
    "        print(\"⚠️ ALERT: Low storage space!\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    check_system_health()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "299ed082-2bb6-4a30-83c6-a66a1fc2df25",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--- UBUNTU SERVER HEALTH REPORT ---\n",
      "Free Disk Space: 17.93 GB\n",
      "RAM Utilization: 57.4%\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import shutil\n",
    "import psutil  # You may need to run 'pip install psutil' in your terminal first\n",
    "\n",
    "def check_system_health():\n",
    "    # 1. Check Disk Space\n",
    "    total, used, free = shutil.disk_usage(\"/\")\n",
    "    free_gb = free / (2**30) # Convert bytes to GB\n",
    "    \n",
    "    # 2. Check RAM usage\n",
    "    ram_usage = psutil.virtual_memory().percent\n",
    "    \n",
    "    # 3. Output results\n",
    "    print(\"--- UBUNTU SERVER HEALTH REPORT ---\")\n",
    "    print(f\"Free Disk Space: {free_gb:.2f} GB\")\n",
    "    print(f\"RAM Utilization: {ram_usage}%\")\n",
    "    \n",
    "    # 4. Basic Alert Logic (Just like a Cloud Monitor)\n",
    "    if ram_usage > 80:\n",
    "        print(\"⚠️ ALERT: High RAM usage detected!\")\n",
    "    if free_gb < 10:\n",
    "        print(\"⚠️ ALERT: Low storage space!\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    check_system_health()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "29e7df54-16d3-4df2-90c1-8b1785354b85",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
