## 📊 Data Preprocessing

**Definition:**  
Data preprocessing is a technique that involves **cleaning**, **transformation**, and **organization** of raw data to remove **inconsistent**, **incomplete**, **incorrect**, and **unnecessary** data — in order to avoid negative effects on model performance.

---

## 🛠️ Steps Performed Using Excel

### 🔁 1. Removed Duplicate Values
- **Tool Used**: Excel → `Data` tab → `Data Tools` group → `Remove Duplicates`
- **Unique Identifier**: `WareHouse_ID`
- **Why**: To ensure each warehouse record is unique and no duplicates affect model learning.

![Remove Duplicates](https://github.com/user-attachments/assets/462e620a-b666-4003-94e1-dcf26b4d0bec)

---

### ❌ 2. Handled Incomplete Data
- **Column Removed**: `wh_est_year`
- **Why**: The column had missing values and was not necessary for the analysis.

![Incomplete Column](https://github.com/user-attachments/assets/2a68e492-0464-4cc9-a6f0-2813af382fda)

---

### 🔄 3. Handled Mismatched Data Types
- **Column**: `WH_capacity_size`
- **Issue**: Data was categorical (`Small`, `Mid`, `Large`) instead of numeric.
- **Solution**: Converted values using `Find and Replace`:
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

### 🗑️ 4. Removed Unimportant Attributes
- **Removed Columns**: `wh_owner_type`, `govt_check_l3m`, `approved_wh_govt_certificate`, `WH_Manager_ID`
- **Reason**: These features were not relevant to the demand and supply mismatch problem and were removed to reduce noise.

---

## ✅ Final Result

- **Original Columns**: 24 attributes  
- **After Preprocessing**: 19 attributes

📁 **Preprocessed Dataset**:  
[https://www.kaggle.com/datasets/prabhasroyal/fmcg-data-processed-csv](https://www.kaggle.com/datasets/prabhasroyal/fmcg-data-processed-csv)
