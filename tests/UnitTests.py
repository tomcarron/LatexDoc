import unittest
from LatexDoc.LatexDoc import LaTeXDocument
import os



class TestLaTeXDocument(unittest.TestCase):

    def setUp(self):
        self.doc = LaTeXDocument("test.tex")
        self.test_content = "Test Content"

    def test_initialization(self):
        self.assertEqual(self.doc.filename, "test.tex")
        self.assertEqual(self.doc.content, [])

    def test_add_line(self):
        self.doc.add_line(self.test_content)
        self.assertIn(self.test_content, self.doc.content)

    def test_add_section(self):
        self.doc.add_section("Test Section")
        self.assertIn("\\section{Test Section}", self.doc.content)

    def test_add_subsection(self):
        self.doc.add_subsection("Test Subsection")
        self.assertIn("\\subsection{Test Subsection}", self.doc.content)

    def test_add_paragraph(self):
        self.doc.add_paragraph("Test Paragraph")
        self.assertIn("\\paragraph{Test Paragraph}", self.doc.content)

    def test_add_newpage(self):
        self.doc.add_newpage()
        self.assertIn("\\newpage", self.doc.content)

    def test_add_single_plot(self):
        self.doc.add_single_plot("TestContent/plot.png", "Caption", "Short Caption")
        self.assertIn(
            "\\includegraphics[width=0.5\\linewidth]{TestContent/plot.png}",
            self.doc.content,
        )

    def test_add_two_panel_plot(self):
        self.doc.add_two_panel_plot(
            "TestContent/plot1.png", "TestContent/plot2.png", "Caption", "Short Caption"
        )
        self.assertIn(
            "\\includegraphics[width=0.5\\linewidth]{TestContent/plot1.png}",
            self.doc.content,
        )
        self.assertIn(
            "\\includegraphics[width=0.5\\linewidth]{TestContent/plot2.png}",
            self.doc.content,
        )

    """
    def test_add_three_panel_plot(self):
        self.doc.add_three_panel_plot(
            "TestContent/plot1.png",
            "TestContent/plot2.png",
            "TestContent/plot3.png",
            "Caption",
        )
        self.assertIn(
            "\\includegraphics[width=0.45\\textwidth]{TestContent/plot1.png}",
            self.doc.content,
        )
        self.assertIn(
            "\\includegraphics[width=0.45\\textwidth]{TestContent/plot3.png}",
            self.doc.content,
        )
    """

    def test_generate_tex_main_doc(self):
        self.doc.add_line(self.test_content)
        self.doc.generate_tex(main_doc=True)
        with open("test.tex", "r") as file:
            content = file.read()
        self.assertIn("\\begin{document}", content)
        self.assertIn(self.test_content, content)

    def test_generate_tex_not_main_doc(self):
        self.doc.add_line(self.test_content)
        self.doc.generate_tex(main_doc=False)
        with open("test.tex", "r") as file:
            content = file.read()
        self.assertNotIn("\\begin{document}", content)
        self.assertIn(self.test_content, content)

    def test_compile_pdf(self):
        try:
            self.doc.compile_pdf()
        except Exception as e:
            self.fail(f"compile_pdf method failed with an exception {e}")

    def tearDown(self):
        if os.path.exists("test.tex"):
            os.remove("test.tex")


if __name__ == "__main__":
    unittest.main()
