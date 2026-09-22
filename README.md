# Kickstarter Crowdfunding Recommendation Engine 

### 👥 **Team Members**
| Name             | GitHub Handle | Contribution                                                             |
|------------------|---------------|--------------------------------------------------------------------------|
| Abigail Galung   | @bazzazy14    | Handle Missing Values                                                    |
| Ryan Amador      | @RyOnFire     | Acquire and load Kickstarter dataset; filter relevant campaign outcomes  |
| Zainab Akhtar    | @Zainu04      | Prepare U.S.-based campaign records                                      |
| Nanshu Singla    | @Nanshusingla | Encode and prepare categorical variables                                 |

---

## 🎯 **Project Highlights**

**Example:**

- Developed a machine learning model using `[model type/technique]` to address `[challenge project task]`.
- Achieved `[key metric or result]`, demonstrating `[value or impact]` for `[host company]`.
- Generated actionable insights to inform business decisions at `[host company or stakeholders]`.
- Implemented `[specific methodology]` to address industry constraints or expectations.

---

## 👩🏽‍💻 **Setup and Installation**

Follow the steps below to set up the project locally and run the notebooks.

### 1. Clone the Repository

Open your terminal and run the commands below:

```bash
git clone https://github.com/Break-Through-Tech/State-Street-1A-kickstarter-crowdfunding-recommendation-engine.git
cd State-Street-1A-kickstarter-crowdfunding-recommendation-engine
```

### 2. Set Up a Python Virtual Environment
#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows PowerShell

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
py -m venv venv
venv\Scripts\activate.bat
```

After activation, you should see `(venv)` at the beginning of your terminal prompt.

### 3. Install Dependencies

Install the required Python dependencies by running:

```bash
python -m pip install -r requirements.txt
```
### 4. Access the Dataset

This project uses the `DSI_kickstarterscrape_dataset.csv` Kickstarter dataset.

1. Download the dataset from Kaggle.
2. Extract the downloaded ZIP file.
3. Place the extracted CSV file inside the `data/` directory.

Your project should contain:

```text
data/
└── DSI_kickstarterscrape_dataset.csv
```

The notebooks expect the dataset at:

```text
data/DSI_kickstarterscrape_dataset.csv
```

### 5. Run the Notebooks
The project notebooks are located in the `notebooks/` directory. You can run them using either Jupyter Notebook or Visual Studio Code.

#### Option 1: Jupyter Notebook

From the project root directory, run:

```bash
jupyter notebook
```

Then navigate to the `notebooks/` directory and open the notebook you want to run.

#### Option 2: Visual Studio Code

1. Open the repository folder in Visual Studio Code.
2. Install the **Python** and **Jupyter** extensions if they are not already installed.
3. Open a `.ipynb` notebook from the `notebooks/` directory.
4. Select the Python virtual environment created during setup as the notebook kernel.
5. Run the notebook cells in order.

---

## 🏗️ **Project Overview**

This project is being conducted through the **Break Through Tech AI Program** as part of AI Studio. From August to December 2026, our team is collaborating on a Challenge Project presented by **State Street**, with the project concluding in a final presentation to company stakeholders.

The primary objective is to use a large-scale, publicly available Kickstarter dataset to predict whether a crowdfunding campaign is likely to **succeed or fail**. Using these predictions and insights from campaign features, our team aims to develop a recommendation engine that can support future campaign creators in making more informed decisions.

An effective recommendation engine could help creators better understand the factors associated with successful campaigns, set more realistic campaign goals, and identify characteristics that may improve their chances of success.

---

## 📊 **Data Exploration**

**You might consider describing the following (as applicable):**

* The dataset(s) used: origin, format, size, type of data
* Data exploration and preprocessing approaches
* Insights from your Exploratory Data Analysis (EDA)
* Challenges and assumptions when working with the dataset(s)

**Potential visualizations to include:**

* Plots, charts, heatmaps, feature visualizations, sample dataset images

---

## 🧠 **Model Development**

**You might consider describing the following (as applicable):**

* Model(s) used (e.g., CNN with transfer learning, regression models)
* Feature selection and Hyperparameter tuning strategies
* Training setup (e.g., % of data for training/validation, evaluation metric, baseline performance)


---

## 📈 **Results & Key Findings**

**You might consider describing the following (as applicable):**

* Performance metrics (e.g., Accuracy, F1 score, RMSE)
* How your model performed
* Insights from evaluating model fairness

**Potential visualizations to include:**

* Confusion matrix, precision-recall curve, feature importance plot, prediction distribution, outputs from fairness or explainability tools

---

## 🚀 **Next Steps**

**You might consider addressing the following (as applicable):**

* What are some of the limitations of your model?
* What would you do differently with more time/resources?
* What additional datasets or techniques would you explore?

---

## 📝 **License**

Specify how your project can be used by others. Choose an appropriate license and link it here (e.g., MIT, Apache 2.0). Make sure your Challenge Advisor approves of the selected license type. 

**Example:**
This project is licensed under the MIT License.

---

## 📄 **References** (Optional but encouraged)

Cite relevant papers, articles, or resources that supported your project.

---

## 🙏 **Acknowledgements** (Optional but encouraged)

Thank your Challenge Advisor, host company representatives, TA, and others who supported your project.
