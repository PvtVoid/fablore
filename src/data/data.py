import re
import pandas as pd
from markdownTable import markdownTable


def create_md_file(file: str, sort: str):
    df = pd.read_csv(file, delimiter="|").sort_values(sort)
    m = markdownTable(df.to_dict(orient="records")).setParams(row_sep="markdown", quote=False)
    out = re.sub("csv", "md", file)
    f = open(out, "w")
    f.write(m.getMarkdown())
    f.close()


create_md_file("./src/data/characters.csv", "Character")
create_md_file("./src/data/locations.csv", "Name")
