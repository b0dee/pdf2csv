import sys
import os
import camelot

def usage(err=None) -> int:
    if err:
        print(f"Error: {err}")
    print(f"Usage:\n{sys.argv[0]} <input-filename.pdf> [output-filename.csv]")
    return 69


def main() -> int:
    if len(sys.argv) <= 1:
        return usage("No input filename provided")
    if len(sys.argv) > 3:
        return usage("More than 2 filenames provided")
    if sys.argv[1][-3:] != "pdf":
        return usage("Input file should be a pdf")

    infile = sys.argv[1] 
    outfile = sys.argv[2] if len(sys.argv) > 2 else "output.csv"

    tables = camelot.read_pdf(infile, pages="all", flavor= "stream")
    if not tables:
        raise Exception(f"Failure opening or parsing input file {infile}")
    everything = ""
    for table in tables:
        everything += "\n".join(table.df.to_csv(index=False).split("\n")[2:])
    with open(outfile, "w") as out:
        out.write(everything)

    return 0

if __name__ == "__main__":
    exit(main())

