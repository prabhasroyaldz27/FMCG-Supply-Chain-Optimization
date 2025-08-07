## 📊 Data Preprocessing

**Definition:**  
Data preprocessing is the process of **cleaning**, **transforming**, and **organizing** raw data to remove **incomplete**, **inconsistent**, **incorrect**, or **irrelevant** entries that can negatively affect model performance.

---

## 🛠️ Steps Performed Using Excel

### 🔁 1. Removed Duplicate Values
- **Tool Used**: Excel → `Data` tab → `Data Tools` → `Remove Duplicates`
- **Unique Identifier**: `Ware_house_ID`
- **Why**: To ensure each warehouse record is unique and prevent duplicate entries from biasing the model.

![Remove Duplicates](https://github.com/user-attachments/assets/462e620a-b666-4003-94e1-dcf26b4d0bec)

---

### ❌ 2. Handled Incomplete Data
- **Removed Column**: `wh_est_year`
- **Why**: This column had many missing values and was not essential for analysis.

![Incomplete Column](https://github.com/user-attachments/assets/2a68e492-0464-4cc9-a6f0-2813af382fda)

---

### 🔄 3. Converted Categorical to Numerical (Mismatched Data Types)
- **Column**: `WH_capacity_size`
- **Issue**: Categorical values (`Small`, `Mid`, `Large`) were not suitable for modeling.
- **Solution**: Replaced using `Find and Replace`:
  - `Small` → `25`
  - `Mid` → `50`
  - `Large` → `100`

**Before:**  
![Before Conversion](https://github.com/user-attachments/assets/f34bf659-ee54-4bf8-8fd7-7e0b57f83201)

**Using Find and Replace:**  
![Find and Replace](https://github.com/user-attachments/assets/801b4f4b-5dd6-4dc1-8dd9-1c4bb19b2441)

**After:**  
![After Conversion](https://github.com/user-attachments/assets/acc3df8b-9209-45c2-b3e2-6b252d0cc7ab)

---

### 🔢 4. Converted Warehouse IDs to Numeric Format
To improve model performance by reducing high-cardinality string values, the `Ware_house_ID` column (originally formatted as `WH_100000` to `WH_124999`) was converted into numeric IDs ranging from `1` to `25000`.

- **Tool Used**: Excel → `Home` tab → `Editing` group → `Fill` → `Series`
- **Method**: Selected `Series in: Columns`, `Step value: 1`, and `Stop value: 25000`

**Before:**  
<img width="77" height="310" alt="Before Series Fill" src="https://github.com/user-attachments/assets/6382cbeb-f8a6-4f66-b4c8-71693f4cc8c1" />

**Series Fill Settings:**  
<img width="212" height="190" alt="Series Dialog" src="https://github.com/user-attachments/assets/7d062367-bc72-45ef-b1df-d2b0d082a237" />

**After:**  
<img width="81" height="305" alt="After Series Fill" src="https://github.com/user-attachments/assets/017cc76a-544f-4fea-81f1-961af128fa25" />

---

### 🗑️ 5. Removed Unimportant Attributes
- **Removed Columns**: `wh_owner_type`, `govt_check_l3m`, `approved_wh_govt_certificate`, `WH_Manager_ID`
- **Why**: These columns were not relevant to solving the demand-supply mismatch problem and were removed to reduce noise and dimensionality.

---

## ✅ Final Outcome

- **Original Features**: 24 attributes  
- **After Preprocessing**: 19 attributes (cleaned, relevant, and model-ready)

📁 **Preprocessed Dataset**:  
[https://www.kaggle.com/datasets/prabhasroyal/fmcg-data-processed-csv](https://www.kaggle.com/datasets/prabhasroyal/fmcg-data-processed-csv)
