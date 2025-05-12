#this does not includes ML keywords as well - so this is just tinyML++
#result in 78 so this is embedded systems as in plot/mercon doc
import os
import pandas as pd
import re

# root_folder = r'F:\Codes\joint attention\Nano-particle\2024_ICARC_Tute'
# root_folder = r'F:\Personal\Sanka\mercon\sicet_2025_proposal_analysis\all_conf'
root_folder = r'F:\Personal\Sanka\mercon\sicet_2025_proposal_analysis\all_conf_international'

# ml_keywords_loaded_real = pd.read_csv(r"E:\SLIIT RA 2024\SICET\conference_paper_analysis_gnn\ml_keywords.csv")
# ml_keywords_ = ml_keywords_loaded_real['Keyword'].tolist()

# nn_keywords_loaded_real = pd.read_csv(r"E:\SLIIT RA 2024\SICET\conference_paper_analysis_gnn\ml_keywords.csv")
# nn_keywords_ = nn_keywords_loaded_real['Keyword'].tolist()

ml_keywords_loaded = pd.read_csv(r"F:\Personal\Sanka\mercon\sicet_2025_proposal_analysis\TinyML\tinyml_keywords_plus_57.csv")
ml_keywords = ml_keywords_loaded['Keyword'].tolist()

ml_keywords = ml_keywords

# ml_keywords_ = nn_keywords_ + ml_keywords_


output_data = []
# tmp___ = ['results__.csv','gnn_keywords.csv','nn_keywords.csv','results__nn.csv','ml_keywords.csv','nn_specific_keywords.csv','results__specif.csv']
tmp___ = []
papers = 0
not_papers =0
for foldername, subfolders, filenames in os.walk(root_folder):
    for filename in filenames:
        if filename.endswith('.csv'):  # Check if the file is a CSV
            if filename in tmp___: 
                continue
            file_path = os.path.join(foldername, filename)
            

            df = pd.read_csv(file_path)
            print(f"Processing: {file_path}")
            
            doi_column = next((col for col in df.columns if "doi" in col.lower()), None)
            title_column = next((col for col in df.columns if "title" in col.lower()), None)
            assert title_column == 'Document Title'
            
            if doi_column and title_column:
                for _, row in df.iterrows():
                    if str(row['Authors'])=='nan':
                        not_papers+=1
                    papers+=1
                    row = row.to_frame().T
                    matched_columns = []
                    keyward_matched = []

                    for col in df.columns:
                        cell_content = str(row[col].values[0]).lower()  
                        
                        tmp=False
                        for kw_ in ml_keywords:
                            pattern = r'\b' + re.escape(kw_) + r'\b'
                            if re.search(pattern, cell_content):
                                tmp=True
                                matched_columns.append(col)
                                keyward_matched.append(kw_)
                        # for kw__ in ml_keywords_:
                        #     pattern_ = r'\b' + re.escape(kw__) + r'\b'
                        #     if re.search(pattern_, cell_content):
                        #         tmp_=True
                        #         matched_columns_.append(col)
                        #         keyward_matched_.append(kw__)
                                # matched_columns.append(True)
                        # if any(kw in cell_content for kw in gnn_keywords):
                        #     matched_columns.append(col)
                    
                    if matched_columns:
                        doi = row.get(doi_column, "N/A")
                        title = row.get(title_column, "N/A")
                        matched_keyword_columns = ", ".join(matched_columns)
                        matched_keyword_values = ", ".join(keyward_matched)
                        output_data.append({
                            "DOI": doi.values[0],
                            "Title": title.values[0],
                            "Matched Columns": matched_keyword_columns,
                            "Matched keywards": matched_keyword_values
                        })
                
output_df = pd.DataFrame(output_data)
output_csv_path = os.path.join(r'F:\Personal\Sanka\mercon\sicet_2025_proposal_analysis\tmp','results__tiny_ml_only.csv')
output_df.to_csv(output_csv_path, index=False)
print(f"Results saved to {output_csv_path}")
print(papers)
print(not_papers)



