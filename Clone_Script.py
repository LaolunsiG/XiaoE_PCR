import requests
import matplotlib.pyplot as plt
from datetime import datetime
import os

# GitHub API 访问令牌和仓库信息
token = 'YOUR_ACCESS_TOKEN'
owner = 'OWNER'
repo = 'REPO'

# 获取克隆数据
url = f'https://api.github.com/repos/{owner}/{repo}/traffic/clones'
headers = {'Authorization': f'token {token}'}
response = requests.get(url, headers=headers)
data = response.json()

# 提取数据
timestamps = [datetime.strptime(item['timestamp'], '%Y-%m-%dT%H:%M:%SZ') for item in data['clones']]
counts = [item['count'] for item in data['clones']]

# 生成图表
plt.figure(figsize=(10, 5))
plt.plot(timestamps, counts, marker='o')
plt.xlabel('Date')
plt.ylabel('Clones')
plt.title('GitHub Repository Clones Over Time')
plt.grid(True)
plt.xticks(rotation=45)

# 保存图表
output_path = 'clones_growth.png'
plt.savefig(output_path)
plt.close()
