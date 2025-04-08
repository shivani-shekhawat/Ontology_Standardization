
import pandas as pd
from fuzzywuzzy import process

# Load raw EMR data
raw_data = pd.DataFrame({
    'Patient_ID': [101, 102, 103, 104],
    'Diagnosis': [' i10', 'E11.9', 'type ii diabetes', 'high bp']
})

# Load ICD-10 reference data
icd10_lookup = pd.DataFrame({
    'ICD10_Code': ['I10', 'E11.9'],
    'Description': ['Essential (primary) hypertension', 'Type 2 diabetes without complications']
})

# Step 1: Clean raw diagnosis data
raw_data['Diagnosis_Clean'] = raw_data['Diagnosis'].str.strip().str.upper()

# Step 2: Direct match with ICD-10 codes
merged_df = raw_data.merge(icd10_lookup, how='left', left_on='Diagnosis_Clean', right_on='ICD10_Code')
merged_df['Mapping_Status'] = merged_df['Description'].notnull()

# Step 3: Fuzzy matching for unmapped cases
unmapped_rows = merged_df[merged_df['Mapping_Status'] == False].copy()

def fuzzy_match_with_score(diagnosis, descriptions):
    result = process.extractOne(diagnosis, descriptions)
    if result:
        match, score, _ = result
        return pd.Series([match, score])
    return pd.Series([None, 0])

unmapped_rows[['Fuzzy_Match', 'Match_Score']] = unmapped_rows['Diagnosis_Clean'].apply(
    lambda x: fuzzy_match_with_score(x, icd10_lookup['Description'])
)

# Step 4: Define action based on confidence threshold
threshold = 80
unmapped_rows['Action'] = unmapped_rows['Match_Score'].apply(
    lambda score: 'Auto-Map' if score >= threshold else 'Needs Manual Review'
)

# Final merged output
final_output = pd.concat([merged_df[merged_df['Mapping_Status']], unmapped_rows], ignore_index=True)
print(final_output[['Patient_ID', 'Diagnosis', 'Diagnosis_Clean', 'Fuzzy_Match', 'Match_Score', 'Action']])
