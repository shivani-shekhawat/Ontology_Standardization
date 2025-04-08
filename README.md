# Ontology Standardization Pipeline

This project demonstrates how to clean and standardize diagnosis data using direct and fuzzy matching against ICD-10 codes.

## 📂 Files

- `Ontology_Standardization_Pipeline.ipynb`: Jupyter Notebook with step-by-step implementation
- `ontology_standardization_pipeline.py`: Reusable Python script version

## 🧾 What It Does

1. Cleans raw EMR diagnosis codes
2. Matches codes directly against ICD-10 reference table
3. Uses fuzzy string matching (via `fuzzywuzzy`) for free-text or inconsistent entries
4. Flags results with:
   - ✅ `Auto-Map`: High-confidence match
   - ⚠️ `Needs Manual Review`: Low-confidence match

## 🧪 Example Inputs

| Diagnosis         | Result                            |
|------------------|-----------------------------------|
| ` i10`           | ✅ Mapped to `I10` (Hypertension) |
| `type ii diabetes` | ✅ Mapped via fuzzy match        |
| `high bp`        | ⚠️ Needs review                   |

## 💻 Tech Used

- Python
- Pandas
- FuzzyWuzzy
- Jupyter

## 🚀 How to Run

1. Open the notebook (`.ipynb`) and run all cells
2. Or run the `.py` script to process inline datasets
3. Customize the pipeline to handle medications (RxNorm), labs (LOINC), etc.

---

Built by Shivani Shekhawat ✨
