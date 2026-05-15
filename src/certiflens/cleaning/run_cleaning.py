import pandas as pd
import time as t

from .cleaners import ComptiaCleaner, AWSCleaner, MicrosoftCleaner, FinalDataCleaner
from ..paths import (
    get_raw_file_path,
    get_raw_final_data_path,
    get_pre_predictions_data_path,
)

def run_cleaning(state=None, progress=None): #those are streamlit interface related arguments
    try:
        cleaners = [ComptiaCleaner(str(get_raw_file_path('CompTIA'))), AWSCleaner(str(get_raw_file_path('AWS'))),
                    MicrosoftCleaner(str(get_raw_file_path('Microsoft')))]
        certifs = []
        step = 1
        for cleaner in cleaners:
            if state is not None: state.text(f"Standardizing {cleaner.provider} columns...")
            cleaner.standardize_columns_names()
            if progress is not None:
                t.sleep(1)
                progress.progress(step/9)
                step+=1
            if state is not None: state.text(f"Adding Provider column for {cleaner.provider}...")
            cleaner.add_provider_column()
            if progress is not None:
                progress.progress(step/9)
                t.sleep(1)
                step+=1
            if state is not None: state.text(f"Saving {cleaner.provider} cleaned data...")
            data = cleaner.get_data()
            certifs.append(data)
            if progress is not None:
                t.sleep(1)
                progress.progress(step/ 9)
                step +=1

        if state is not None: state.text("Concatenating cleaned data...")
        raw_final = pd.concat(certifs, ignore_index= True, join= 'outer') # shape = (114,22)
        raw_final.to_json(str(get_raw_final_data_path()), orient = 'records', indent = 2)
        print('Before cleaning: ', raw_final.shape)

        if state is not None: state.text("Calling the final cleaner...")
        final_cleaner = FinalDataCleaner(str(get_raw_final_data_path()))
        final_data = (final_cleaner
                      .drop_missing_name_rows()
                      .drop_duplicate_certifications()
                      .reorder_columns()
                      .drop_empty_columns()
                      .clean_duration()
                      .clean_cost()
                      .clean_certification_name()
                      .standardize_columns_names()
                      .standardize_languages_column()
                      .standardize_Level_column()
                      .standardize_Domain_column()
                      .final_touches()
                      .get_data())

        final_data.to_csv(str(get_pre_predictions_data_path()), index= False)
        print(final_data.shape)
        if state is not None:
            state.empty()
            return True
    except Exception as e:
        print(f'error {e}')
        if state is not None:
            state.error("An error has occured while cleaning: {e}. Please try again!")
            return False


if __name__ == "__main__": 
    run_cleaning()















