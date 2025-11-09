
# 🧠 AI Project – GitHub Analyzer

This project analyzes the number of commits in a specified GitHub repository and visualizes the results using **Matplotlib**.  
It helps you understand commit activity and trends directly from your repository data.

## 📂 Project Structure

src/

└── github_analyzer.py   # Fetches GitHub commits and plots the data

## ⚙️ Setup Instructions

### 1. Clone the Repository
bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>

### 2. Create and Activate Virtual Environment (optional but recommended)

bash
python -m venv venv
source venv/bin/activate      # For macOS/Linux
venv\Scripts\activate         # For Windows

### 3. Install Dependencies

bash
pip install -r requirements.txt


### 4. Add GitHub Token

Create a `.env` file in the project root and add your GitHub Personal Access Token:


GITHUB_TOKEN=your_github_token_here


> **Note:** You can generate a personal access token from your GitHub account settings under
> **Developer settings → Personal access tokens → Tokens (classic)**.

---

## 🚀 Run the Analyzer

Run the following command:

bash
python src/github_analyzer.py


This script will:

* Fetch commit data from the specified GitHub repository.
* Store it in a DataFrame.
* Plot the number of commits using **Matplotlib**.


## 📊 Output Example

You’ll see a **Matplotlib chart** displaying the number of commits over time for the given repository.


## 🧰 Technologies Used

* **Python 3**
* **Matplotlib**
* **Pandas**
* **Requests**
* **dotenv**



## 🧑‍💻 Author

**Vani Agarwal**
AI Enthusiast

📧 vaniagarwal2000va@gmail.com

🔗 https://www.linkedin.com/in/vaniagarwal/

