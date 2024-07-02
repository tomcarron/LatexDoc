import os


class LaTeXDocument:

    def __init__(self, filename):
        self.filename = filename
        self.content = []

    def add_line(self, line):
        self.content.append(line)

    def add_section(self, title):
        self.add_line("\\clearpage")
        self.add_line("\\section{" + title + "}")

    def add_subsection(self, title):
        self.add_line("\\subsection{" + title + "}")

    def add_paragraph(self, title):
        self.add_line("\\paragraph{" + title + "}")

    def add_newpage(self):
        self.add_line("\\newpage")

    def add_single_plot(self, plot_filename, caption, short_caption=""):
        self.add_line("\\begin{figure}[h]")
        self.add_line("\\includegraphics[width=0.5\\linewidth]{" + plot_filename + "}")
        self.add_line("\\caption" + "{" + short_caption + "}" + "{" + caption + "}")
        self.add_line("\\end{figure}")

    def add_two_panel_plot(
        self, plot1_filename, plot2_filename, caption, short_caption=""
    ):
        self.add_line("\\begin{figure}[htbp]")
        self.add_line("\\begin{subfigure}")
        self.add_line("\\includegraphics[width=0.5\\linewidth]{" + plot1_filename + "}")
        self.add_line("\\end{subfigure}\\hfill")
        self.add_line("\\begin{subfigure}")
        self.add_line("\\includegraphics[width=0.5\\linewidth]{" + plot2_filename + "}")
        self.add_line("\\end{subfigure}")
        self.add_line("\\caption" + "{" + short_caption + "}" + "{" + caption + "}")
        self.add_line("\\end{figure}")

    def add_three_panel_plot(self, plot1, plot2, plot3, caption):
        self.add_line("\\begin{figure}[h]")
        self.add_line(
            "\\subfloat{\\includegraphics[width=0.45\\textwidth]{"
            + plot1
            + "} } \\qquad"
        )
        self.add_line(
            "\\subfloat{\\includegraphics[width=0.45\\textwidth]{"
            + plot2
            + "} } \\qquad"
        )
        self.add_line("\\centering")
        self.add_line(
            "\\subfloat{\\includegraphics[width=0.45\\textwidth]{"
            + plot3
            + "} } \\qquad"
        )
        self.add_line("\\caption[]" + "{" + caption + "}")
        self.add_line("\\end{figure}")

    def generate_tex(self, main_doc=True):
        if main_doc == True:
            with open(self.filename, "w") as tex_file:
                tex_file.write("\\documentclass{article}\n")
                tex_file.write(
                    "\\usepackage{graphicx, subcaption, booktabs, geometry, placeins, pdflscape}\n"
                )
                tex_file.write("\\geometry{margin=0.3in}\n")
                tex_file.write("\\begin{document}\n")
                for line in self.content:
                    tex_file.write(line + "\n")
                tex_file.write("\\end{document}")
        else:
            with open(self.filename, "w") as tex_file:
                for line in self.content:
                    tex_file.write(line + "\n")

    def compile_pdf(self):
        os.system("pdflatex " + self.filename)
        os.system("pdflatex " + self.filename)
