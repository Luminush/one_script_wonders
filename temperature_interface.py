# TODO pass python script to cmake with following arguments
# excel_name, template_name, output_header_file
# for the moment we initialize them here
# TODO this script is too specific; try to extract
# reusable elements

import pandas   as pd
import json     as js 
from jinja2 import Environment, FileSystemLoader
from re import sub

excel_name          = 'Example_PDUR.ods'
template_name       = "PDUR_struct_template.h"
output_header_file  = "pdur_header.h"
pdur                = pd.read_excel(excel_name)

# automatically set naming convention (snake case) for fields in excel file
# TODO - python might already have identifiers for this type of situation
def snake_case(s):
    return '_'.join(
        sub('([A-Z][a-z]+)', r' \1',
        sub('([A-Z]+)', r' \1',
        s.replace('-', ' '))).split()).lower()

entries     = []
for entry in pdur.columns:
    entries.append(snake_case(entry))
pdur.columns    = entries

pdur            = pdur.sort_values(by="frame_id")
unique_frames   = pdur[["frame_id", "frame_name"]].drop_duplicates()

env         = Environment(loader = FileSystemLoader("templates/"))
template    = env.get_template(template_name)

filename    = output_header_file
context     = {
                "entries":  pdur.to_dict('records'),
                "frames":   unique_frames.to_dict('records')
                }

with open(filename, mode="w", encoding="utf-8") as output:
    output.write(template.render(context))

