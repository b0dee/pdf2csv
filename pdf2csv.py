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
    if len(sys.argv) >= 3:
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
        table.to_csv("out.csv")
        try:
            with open("out.csv", "r") as f:
                # Strip first line 
                # In 1st page should be report title, 
                # in subsequent pages it should be the table headers.
                # That way csv output is unbroken
                everything += "\n".join(f.read().split("\n")[1:]) 
            os.remove("out.csv")
        except:
            raise Exception("Failure opening temporary output file")
    with open(outfile, "w") as out:
        out.write(everything)

if __name__ == "__main__":
    exit(main())

