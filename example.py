from LatexDoc import LaTeXDocument

# Create a new LaTeX document
doc = LaTeXDocument()

# Add a section to the document
doc.add_section("Introduction")

# Add some text to the document
doc.add_line("This is the introduction section of my document.")

# Add a subsection to the document
doc.add_subsection("Background")

# Add some text to the document
doc.add_line("In this section, we will discuss the background of the topic.")

# Add a subsection to the document
doc.add_subsection("Related Work")

# Add some text to the document
doc.add_line("In this subsection, we will review the related work.")

# Add a section to the document
doc.add_section("Methodology")

# Add some text to the document
doc.add_line("In this section, we will describe our methodology.")

# Add a subsection to the document
doc.add_subsection("Data Collection")

# Add some text to the document
doc.add_line("In this subsection, we will explain how we collected the data.")

# Add a subsection to the document
doc.add_subsection("Data Analysis")

# Add some text to the document
doc.add_line("In this subsection, we will analyze the collected data.")

# Generate the LaTeX document. The main doc flag tells the generator to include the preamble and end document tags. This allows for generation of seperate documents
# eg in a loop which can then all be compiled in a main document by using the include command.
doc.generate_tex(main_doc=True)

# Generate a PDF from the LaTeX document using pdflatex
doc.compile_pdf()
