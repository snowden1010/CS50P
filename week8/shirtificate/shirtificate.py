from fpdf import FPDF, Align

class PDF(FPDF):
    def header(self):
        text = "CS50 shirtificate"

        self.set_font("helvetica",style="", size=50)
        # self.set_auto_page_break(auto=True, 10)
        self.cell(0, 90, text=text, border=0, align="C", center=True)

    def text_overlay(self, image_src, text):
        self.set_xy(10, 150)
        self.set_font("helvetica", "", 26)
        self.set_text_color(255,255,255)

        self.image(image_src, x=Align.C, y=90, w=180)
        self.cell(w=0, h=10, text=text, border=0, align="C")

if __name__ == "__main__":
    name = input("Name: ")
    pdf = PDF(orientation="P", format="A4")
    pdf.add_page()
    pdf.header()
    image, text = "shirtificate.png", f"{name} took CS50"
    pdf.text_overlay(image_src=image, text=text)
    pdf.output("shirtificate.pdf")
